# Simulador de rede de filas por eventos discretos, com topologia genérica
# carregada a partir de um arquivo .yml. Extensão do simulador do M6 (que já
# suportava roteamento probabilístico entre filas, mas com a topologia fixa
# no próprio código Python) para aceitar qualquer rede descrita em YAML, no
# mesmo estilo de arquivo usado no simulador do módulo 3 (arrivals/queues/
# network), o que permite inclusive usar o `model.yml` de exemplo do módulo 3
# como entrada de teste.
#
# ---------------------------------------------------------------------------
# COMO USAR
# ---------------------------------------------------------------------------
#   python3 simulador_rede.py <arquivo.yml> [--aleatorios N] [--seed S]
#
# Formato do arquivo .yml (mesmas chaves do simulador do módulo 3):
#
#   arrivals:              # instante da PRIMEIRA chegada externa de cada
#      Q1: 2.0             # fila que recebe clientes de fora da rede
#
#   queues:
#      Q1:
#         servers: 1        # número de servidores (c)
#         capacity: 5       # capacidade total (fila + atendimento). Omita
#                            # esta chave para capacidade ilimitada (K = ∞)
#         minArrival: 2.0   # intervalo entre chegadas externas (uniforme).
#         maxArrival: 4.0   # Omita as duas chaves se a fila só recebe
#                            # clientes vindos de outras filas da rede
#         minService: 1.0   # intervalo de atendimento (uniforme)
#         maxService: 2.0
#
#   network:                # roteamento: saída de `source` vira chegada em
#   -  source: Q1            # `target` com probabilidade `probability`. A
#      target: Q2            # probabilidade que faltar pra somar 1.0, por
#      probability: 0.2      # fila de origem, é a chance do cliente sair da
#                            # rede depois de atendido em `source`.
#
#   rndnumbersPerSeed: 100000   # opcional: quantos aleatórios consumir antes
#                                # de encerrar a simulação (padrão 100000,
#                                # ou use --aleatorios na linha de comando)
#
# As chaves `rndnumbers`/`seeds` do simulador do módulo 3 são ignoradas por
# este script (ele gera seus próprios aleatórios com o gerador congruente
# linear validado nos módulos M4/M6) — podem ficar no arquivo só para
# permitir testar o mesmo .yml no `simulator.jar` do módulo 3.
# ---------------------------------------------------------------------------

import argparse
import math
from collections import defaultdict
from dataclasses import dataclass, field

import yaml

SAIDA = "SAIR"  # destino especial: cliente deixa a rede


def verifica_hull_dobell(a, c, M):
    # condições de Hull-Dobell pra garantir período completo do MCL
    cond1 = math.gcd(c, M) == 1

    fatores_primos_M = set()
    n = M
    d = 2
    while d * d <= n:
        while n % d == 0:
            fatores_primos_M.add(d)
            n //= d
        d += 1
    if n > 1:
        fatores_primos_M.add(n)

    cond2 = all((a - 1) % p == 0 for p in fatores_primos_M)
    cond3 = (M % 4 != 0) or ((a - 1) % 4 == 0)

    return cond1, cond2, cond3, fatores_primos_M


class GeradorMCL:
    # Xn+1 = (a*Xn + c) mod M, normalizado em (0,1)

    def __init__(self, seed, a, c, M):
        self.a = a
        self.c = c
        self.M = M
        self.previous = seed
        self.count_used = 0

    def next_random(self):
        self.previous = (self.a * self.previous + self.c) % self.M
        self.count_used += 1
        return self.previous / self.M

    def uniform(self, low, high):
        u = self.next_random()
        return low + u * (high - low)


A = 1103515245
C = 12345
M = 2 ** 31


@dataclass
class Fila:
    id: str
    num_servidores: int
    atendimento_min: float
    atendimento_max: float
    capacidade: int = None  # None = capacidade ilimitada
    chegada_min: float = None
    chegada_max: float = None
    primeira_chegada: float = None
    destinos: dict = field(default_factory=dict)

    def __post_init__(self):
        soma = sum(self.destinos.values())
        if soma > 1.0 + 1e-9:
            raise ValueError(
                f"Fila {self.id}: soma das probabilidades de roteamento "
                f"({soma}) não pode passar de 1.0"
            )
        tabela = list(self.destinos.items())
        resto = 1.0 - soma
        if resto > 1e-9:
            tabela.append((SAIDA, resto))
        self.tabela_roteamento = tabela or [(SAIDA, 1.0)]


def carregar_modelo(caminho):
    # lê um .yml no estilo do simulador do módulo 3 e monta a lista de Filas
    with open(caminho, encoding="utf-8") as arq:
        dados = yaml.safe_load(arq)

    arrivals = dados.get("arrivals") or {}
    network = dados.get("network") or []

    destinos_por_origem = defaultdict(dict)
    for aresta in network:
        destinos_por_origem[aresta["source"]][aresta["target"]] = aresta["probability"]

    filas = []
    for fid, cfg in dados["queues"].items():
        filas.append(Fila(
            id=fid,
            num_servidores=cfg["servers"],
            capacidade=cfg.get("capacity"),
            atendimento_min=cfg["minService"],
            atendimento_max=cfg["maxService"],
            chegada_min=cfg.get("minArrival"),
            chegada_max=cfg.get("maxArrival"),
            primeira_chegada=arrivals.get(fid),
            destinos=destinos_por_origem.get(fid, {}),
        ))

    max_aleatorios = dados.get("rndnumbersPerSeed", 100_000)
    return filas, max_aleatorios


def simular_rede(filas, max_aleatorios, seed=1, a=A, c=C, m=M):
    # roda a simulação da rede até usar max_aleatorios números e devolve os
    # resultados de cada fila. Mesma lógica de eventos do M4/M6, generalizada
    # para topologia arbitrária e capacidade opcionalmente ilimitada.

    tabela_filas = {f.id: f for f in filas}
    for f in filas:
        for destino, _ in f.tabela_roteamento:
            if destino != SAIDA and destino not in tabela_filas:
                raise ValueError(
                    f"Fila {f.id}: roteamento aponta para fila desconhecida '{destino}'"
                )

    rng = GeradorMCL(seed, a, c, m)

    clock = 0.0
    estado = {f.id: 0 for f in filas}
    times = {f.id: defaultdict(float) for f in filas}
    perdas = {f.id: 0 for f in filas}
    fila_espera = {f.id: 0 for f in filas}
    departures = {f.id: [None] * f.num_servidores for f in filas}
    next_arrival = {f.id: f.primeira_chegada for f in filas if f.chegada_min is not None}

    should_stop = False

    def servidor_livre(fid):
        for s, d in enumerate(departures[fid]):
            if d is None:
                return s
        return None

    def entra_cliente(fid):
        nonlocal should_stop
        f = tabela_filas[fid]
        if f.capacidade is None or estado[fid] < f.capacidade:
            estado[fid] += 1
            s = servidor_livre(fid)
            if s is not None:
                if not should_stop:
                    t_atend = rng.uniform(f.atendimento_min, f.atendimento_max)
                    if rng.count_used >= max_aleatorios:
                        should_stop = True
                    departures[fid][s] = clock + t_atend
            else:
                fila_espera[fid] += 1  # servidores ocupados, cliente espera
        else:
            perdas[fid] += 1  # fila cheia, cliente é bloqueado

    def escolhe_destino(fid):
        nonlocal should_stop
        tab = tabela_filas[fid].tabela_roteamento
        if len(tab) == 1:
            return tab[0][0]
        u = rng.next_random()
        if rng.count_used >= max_aleatorios:
            should_stop = True
        acumulado = 0.0
        for destino, p in tab:
            acumulado += p
            if u < acumulado:
                return destino
        return tab[-1][0]  # guarda contra arredondamento de ponto flutuante

    while not should_stop:
        # próximo evento = a chegada externa ou saída mais próxima, em toda a rede
        candidatos = [(t, 'chegada_externa', fid, None) for fid, t in next_arrival.items()]
        for fid, deps in departures.items():
            for s, d in enumerate(deps):
                if d is not None:
                    candidatos.append((d, 'saida', fid, s))
        tempo_evento, tipo_evento, fid, servidor = min(candidatos, key=lambda x: x[0])

        for fid2 in estado:
            times[fid2][estado[fid2]] += tempo_evento - clock
        clock = tempo_evento

        if tipo_evento == 'chegada_externa':
            entra_cliente(fid)
            if not should_stop:
                f = tabela_filas[fid]
                t_entre = rng.uniform(f.chegada_min, f.chegada_max)
                if rng.count_used >= max_aleatorios:
                    should_stop = True
                next_arrival[fid] = clock + t_entre

        else:
            estado[fid] -= 1
            destino = escolhe_destino(fid)
            if destino != SAIDA:
                entra_cliente(destino)

            if fila_espera[fid] > 0:
                fila_espera[fid] -= 1
                if not should_stop:
                    f = tabela_filas[fid]
                    t_atend = rng.uniform(f.atendimento_min, f.atendimento_max)
                    if rng.count_used >= max_aleatorios:
                        should_stop = True
                    departures[fid][servidor] = clock + t_atend
                else:
                    departures[fid][servidor] = None
            else:
                departures[fid][servidor] = None

        if rng.count_used >= max_aleatorios:
            should_stop = True

    tempo_global = clock
    resultado_filas = {}
    for f in filas:
        estado_max = f.capacidade if f.capacidade is not None else max(times[f.id].keys(), default=0)
        lista_times = [times[f.id][i] for i in range(estado_max + 1)]
        probabilidades = [t / tempo_global for t in lista_times]
        resultado_filas[f.id] = {
            'num_servidores': f.num_servidores,
            'K': f.capacidade,
            'times': lista_times,
            'probabilidades': probabilidades,
            'perdas': perdas[f.id],
        }

    return {
        'filas': resultado_filas,
        'tempo_global': tempo_global,
        'aleatorios_usados': rng.count_used,
    }


def imprimir_resultados_rede(nome_rede, resultado):
    print("=" * 70)
    print(f"Resultados da simulação: {nome_rede}")
    print("=" * 70)
    print(f"Números aleatórios usados .... {resultado['aleatorios_usados']}")
    print(f"Tempo global da simulação .... {resultado['tempo_global']:.4f}")

    for fid, r in resultado['filas'].items():
        K = r['K']
        rotulo_capacidade = f", capacidade={K}" if K is not None else " (capacidade ilimitada)"
        print("-" * 70)
        print(f"Fila: {fid}  (servidores={r['num_servidores']}{rotulo_capacidade})")
        print(f"Clientes perdidos (bloqueados) {r['perdas']}")
        print(f"{'Estado':<8}{'Tempo acumulado':<20}{'Probabilidade':<15}")
        for i, (t, p) in enumerate(zip(r['times'], r['probabilidades'])):
            print(f"{i:<8}{t:<20.4f}{p * 100:<14.4f}%")
        soma_tempos = sum(r['times'])
        soma_probs = sum(r['probabilidades'])
        print(f"Soma dos tempos acumulados ... {soma_tempos:.4f} "
              f"(deve ser igual ao tempo global)")
        print(f"Soma das probabilidades ...... {soma_probs * 100:.4f}%")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Simulador de rede de filas genérico (YAML)")
    parser.add_argument("modelo", help="caminho do arquivo .yml com a descrição da rede")
    parser.add_argument("--aleatorios", type=int, default=None,
                         help="quantos números pseudoaleatórios consumir (padrão: "
                              "rndnumbersPerSeed do .yml, ou 100000)")
    parser.add_argument("--seed", type=int, default=1, help="semente do gerador (padrão: 1)")
    args = parser.parse_args()

    cond1, cond2, cond3, fatores = verifica_hull_dobell(A, C, M)
    print("Verificação das condições de Hull-Dobell (período completo):")
    print(f"  mdc(c, M) = 1 ..................... {cond1}")
    print(f"  (a-1) divisível pelos fatores primos de M {sorted(fatores)} ..... {cond2}")
    print(f"  (a-1) divisível por 4 (pois M múltiplo de 4) ..... {cond3}")
    print(f"  M = {M} (período completo garante até M números distintos)")
    print()

    filas, max_aleatorios_yml = carregar_modelo(args.modelo)
    max_aleatorios = args.aleatorios if args.aleatorios is not None else max_aleatorios_yml

    resultado = simular_rede(filas, max_aleatorios=max_aleatorios, seed=args.seed)
    imprimir_resultados_rede(args.modelo, resultado)
