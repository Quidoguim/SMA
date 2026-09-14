# Simulador de rede de filas por eventos discretos, com topologia genérica.
# Extensão do simulador do M4 (fila única) para múltiplas filas G/G/c/K
# conectadas por roteamento probabilístico: a saída de uma fila pode virar
# chegada em outra fila da rede ou deixar o sistema.
#
# ---------------------------------------------------------------------------
# COMO USAR
# ---------------------------------------------------------------------------
# 1. Descreva cada fila da rede com um `Fila(...)`:
#      - id:                nome da fila (única na rede)
#      - num_servidores:     quantidade de servidores (c)
#      - capacidade:         capacidade total do sistema, fila de espera +
#                             clientes em atendimento (K)
#      - atendimento_min/max: intervalo do tempo de atendimento (uniforme)
#      - chegada_min/max:    intervalo do tempo entre chegadas externas
#                             (uniforme). Deixe em branco (None, o padrão)
#                             se a fila só recebe clientes vindos de outras
#                             filas da rede, sem chegada externa própria.
#      - primeira_chegada:   instante da primeira chegada externa (só faz
#                             sentido se chegada_min/max estiverem definidos)
#      - destinos:           dict {id_da_fila_destino: probabilidade} com o
#                             roteamento dos clientes que terminam o
#                             atendimento nesta fila. A probabilidade que
#                             faltar para somar 1.0 é a chance do cliente
#                             sair da rede depois de atendido aqui. Uma fila
#                             sem `destinos` (dict vazio) manda 100% dos
#                             clientes para fora do sistema.
#
# 2. Junte as filas numa lista e chame `simular_rede(filas, max_aleatorios)`.
#    A simulação roda até consumir `max_aleatorios` números pseudoaleatórios
#    (mesmo critério de parada do M4), não um número fixo de eventos.
#
# 3. `imprimir_resultados_rede(nome, resultado)` imprime, para cada fila da
#    rede: tempo acumulado e probabilidade de cada estado, número de
#    clientes perdidos (bloqueados por falta de capacidade) e, uma vez só,
#    o tempo global da simulação e a quantidade de aleatórios usados.
#
# Rodando o arquivo diretamente (`python3 simulador_rede_filas.py`) executa
# a rede de validação pedida no M6: Fila 1 (G/G/2/3) em tandem com a Fila 2
# (G/G/1/5), com Fila 1 recebendo chegadas externas e roteando 100% dos
# clientes atendidos para a Fila 2.
# ---------------------------------------------------------------------------

import math
from dataclasses import dataclass, field

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


SEED = 1
A = 1103515245
C = 12345
M = 2 ** 31


@dataclass
class Fila:
    id: str
    num_servidores: int
    capacidade: int
    atendimento_min: float
    atendimento_max: float
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


def simular_rede(filas, max_aleatorios, seed=SEED, a=A, c=C, m=M):
    # roda a simulação da rede até usar max_aleatorios números e devolve os
    # resultados de cada fila (mesma lógica de eventos do M4, generalizada
    # para várias filas conectadas por roteamento probabilístico)

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
    times = {f.id: [0.0] * (f.capacidade + 1) for f in filas}
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
        if estado[fid] < f.capacidade:
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
        probabilidades = [times[f.id][i] / tempo_global for i in range(f.capacidade + 1)]
        resultado_filas[f.id] = {
            'num_servidores': f.num_servidores,
            'K': f.capacidade,
            'times': times[f.id],
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
        print("-" * 70)
        print(f"Fila: {fid}  (servidores={r['num_servidores']}, capacidade={K})")
        print(f"Clientes perdidos (bloqueados) {r['perdas']}")
        print(f"{'Estado':<8}{'Tempo acumulado':<20}{'Probabilidade':<15}")
        for i in range(K + 1):
            t = r['times'][i]
            p = r['probabilidades'][i]
            print(f"{i:<8}{t:<20.4f}{p * 100:<14.4f}%")
        soma_tempos = sum(r['times'])
        soma_probs = sum(r['probabilidades'])
        print(f"Soma dos tempos acumulados ... {soma_tempos:.4f} "
              f"(deve ser igual ao tempo global)")
        print(f"Soma das probabilidades ...... {soma_probs * 100:.4f}%")
    print()


if __name__ == "__main__":

    cond1, cond2, cond3, fatores = verifica_hull_dobell(A, C, M)
    print("Verificação das condições de Hull-Dobell (período completo):")
    print(f"  mdc(c, M) = 1 ..................... {cond1}")
    print(f"  (a-1) divisível pelos fatores primos de M {sorted(fatores)} ..... {cond2}")
    print(f"  (a-1) divisível por 4 (pois M múltiplo de 4) ..... {cond3}")
    print(f"  M = {M} (período completo garante até M números distintos, "
          f"muito acima dos 100.000 exigidos)")
    print()

    # Rede de validação do M6: Fila 1 (G/G/2/3) em tandem com a Fila 2
    # (G/G/1/5). Só a Fila 1 recebe clientes de fora; 100% do que ela
    # atende segue para a Fila 2, que não tem chegada externa própria.
    filas_validacao = [
        Fila(
            id="Fila 1",
            num_servidores=2, capacidade=3,
            chegada_min=1, chegada_max=5,
            atendimento_min=4, atendimento_max=5,
            primeira_chegada=2.5,
            destinos={"Fila 2": 1.0},
        ),
        Fila(
            id="Fila 2",
            num_servidores=1, capacidade=5,
            atendimento_min=1, atendimento_max=3,
        ),
    ]

    resultado = simular_rede(filas_validacao, max_aleatorios=100_000)
    imprimir_resultados_rede("Fila 1 -> Fila 2 (tandem)", resultado)
