# Índices de desempenho (população, vazão, utilização e tempo de resposta) das
# filas de uma rede descrita em .yml, calculados a partir da simulação feita
# por simulador_rede.py. Fórmulas do módulo M9, para cada fila (K = capacidade,
# C = servidores, pi_i = probabilidade do estado i, vinda da simulação):
#
#   população     N = soma(pi_i * i)                  i = 1..K
#   vazão         D = soma(pi_i * mu_i)               mu_i = min(i, C) * mu
#   utilização    U = soma(pi_i * min(i, C) / C)
#   tempo resp.   W = N / D
#
# mu é a taxa de atendimento de UM servidor, em clientes por hora, obtida do
# tempo médio de atendimento (em minutos): mu = 60 / ((min + max) / 2). Por isso
# D sai em clientes/hora e W em horas (multiplicamos por 60 pra mostrar minutos).
#
# ---------------------------------------------------------------------------
# COMO USAR
# ---------------------------------------------------------------------------
#   python3 analise_indices.py modelo.yml [--seeds 1 2 3] [--aleatorios N]
#                                         [--tabela] [--comparar outro.yml]
#
#   --seeds      sementes do gerador (padrão: 1). Com várias, mostra a média e o
#                desvio padrão entre elas.
#   --aleatorios quantos aleatórios consumir (padrão: rndnumbersPerSeed do .yml
#                ou 100000).
#   --tabela     imprime também a tabela por estado (probabilidade, N, D e U de
#                cada estado), como nos exemplos do M9. Só com uma semente.
#   --comparar   segundo .yml (ex.: o modelo melhorado): mostra os índices dos
#                dois lado a lado, com a variação percentual.
# ---------------------------------------------------------------------------

import argparse
import statistics

from simulador_rede import carregar_modelo, simular_rede


def taxa_atendimento(atendimento_min, atendimento_max):
    # mu de um servidor, em clientes/hora, a partir do tempo médio em minutos
    tempo_medio = (atendimento_min + atendimento_max) / 2
    return 60.0 / tempo_medio


def calcular_indices(probabilidades, servidores, mu):
    # probabilidades[i] = pi_i, i = 0..K (ou até o maior estado visto, se K = inf)
    linhas = []
    for i, pi in enumerate(probabilidades):
        ocupados = min(i, servidores)
        linhas.append({
            'estado': i,
            'prob': pi,
            'N': pi * i,
            'D': pi * ocupados * mu,
            'U': pi * ocupados / servidores,
        })
    n = sum(l['N'] for l in linhas)
    d = sum(l['D'] for l in linhas)
    u = sum(l['U'] for l in linhas)
    w_horas = n / d if d > 0 else float('nan')
    return {'linhas': linhas, 'N': n, 'D': d, 'U': u,
            'W_horas': w_horas, 'W_min': w_horas * 60}


def kendall(servidores, capacidade):
    # todas as filas são G/G/c/K; K = ∞ quando a capacidade é ilimitada
    return f"G/G/{servidores}/{capacidade if capacidade is not None else '∞'}"


def analisar(caminho, seed=1, aleatorios=None):
    # roda a simulação do .yml e devolve os índices de cada fila
    filas, aleatorios_yml = carregar_modelo(caminho)
    por_id = {f.id: f for f in filas}
    resultado = simular_rede(filas, aleatorios if aleatorios is not None else aleatorios_yml,
                             seed=seed)
    saida = {}
    for fid, r in resultado['filas'].items():
        f = por_id[fid]
        mu = taxa_atendimento(f.atendimento_min, f.atendimento_max)
        ind = calcular_indices(r['probabilidades'], r['num_servidores'], mu)
        ind.update({'kendall': kendall(r['num_servidores'], r['K']),
                    'mu': mu, 'perdas': r['perdas']})
        saida[fid] = ind
    return saida, resultado['tempo_global']


def imprimir_tabela_estados(fid, ind):
    print(f"Fila {fid} ({ind['kendall']}), mu = {ind['mu']:.4f} clientes/h")
    print(f"{'i':<5}{'prob (%)':>10}{'N':>10}{'D (cl/h)':>12}{'U':>10}")
    for l in ind['linhas']:
        print(f"{l['estado']:<5}{l['prob'] * 100:>10.2f}{l['N']:>10.4f}"
              f"{l['D']:>12.4f}{l['U']:>10.4f}")
    print(f"{'soma':<5}{100.0:>10.2f}{ind['N']:>10.4f}{ind['D']:>12.4f}{ind['U']:>10.4f}")
    print(f"U = {ind['U'] * 100:.1f}%   W = {ind['W_horas']:.4f} h = {ind['W_min']:.2f} min")
    print()


CABECALHO = (f"{'Fila':<6}{'Kendall':<12}{'mu (cl/h)':>10}{'Perdas':>9}{'N':>9}"
             f"{'D (cl/h)':>10}{'U (%)':>8}{'W (min)':>10}")


def imprimir_resumo(titulo, indices, tempo_global=None):
    print(titulo)
    if tempo_global is not None:
        print(f"Tempo global da simulação: {tempo_global:.4f} min")
    print(CABECALHO)
    for fid, ind in indices.items():
        print(f"{fid:<6}{ind['kendall']:<12}{ind['mu']:>10.2f}{ind['perdas']:>9}"
              f"{ind['N']:>9.4f}{ind['D']:>10.4f}{ind['U'] * 100:>8.1f}{ind['W_min']:>10.2f}")
    print()


def media_entre_seeds(lista):
    # lista de dicts {fila: indices}; devolve media e desvio padrão por fila/índice
    chaves = ['perdas', 'N', 'D', 'U', 'W_min']
    media, desvio = {}, {}
    for fid in lista[0]:
        base = lista[0][fid]
        valores = {c: [x[fid][c] for x in lista] for c in chaves}
        media[fid] = {**{c: statistics.mean(v) for c, v in valores.items()},
                      'kendall': base['kendall'], 'mu': base['mu']}
        desvio[fid] = {c: (statistics.stdev(v) if len(v) > 1 else 0.0)
                       for c, v in valores.items()}
    return media, desvio


def imprimir_resumo_seeds(titulo, seeds, media, desvio):
    print(f"{titulo} - média de {len(seeds)} sementes {seeds} (± desvio padrão)")
    print(f"{'Fila':<6}{'Kendall':<12}{'Perdas':>16}{'N':>16}{'D (cl/h)':>16}"
          f"{'U (%)':>14}{'W (min)':>16}")
    for fid, m in media.items():
        s = desvio[fid]
        print(f"{fid:<6}{m['kendall']:<12}"
              f"{m['perdas']:>9.0f} ±{s['perdas']:>4.0f}"
              f"{m['N']:>9.3f} ±{s['N']:>4.2f}"
              f"{m['D']:>9.3f} ±{s['D']:>4.2f}"
              f"{m['U'] * 100:>7.1f} ±{s['U'] * 100:>3.1f}"
              f"{m['W_min']:>9.1f} ±{s['W_min']:>4.1f}")
    print()


def imprimir_comparacao(media_a, media_b, rotulo_a, rotulo_b):
    print(f"Comparação: {rotulo_a} -> {rotulo_b}")
    print(f"{'Fila':<6}{'Índice':<10}{rotulo_a:>14}{rotulo_b:>14}{'Variação':>12}")
    nomes = [('perdas', 'Perdas', 1), ('N', 'N', 1), ('D', 'D (cl/h)', 1),
             ('U', 'U (%)', 100), ('W_min', 'W (min)', 1)]
    for fid in media_a:
        for chave, nome, escala in nomes:
            a, b = media_a[fid][chave] * escala, media_b[fid][chave] * escala
            var = f"{(b - a) / a * 100:+.1f}%" if a else "-"
            print(f"{fid:<6}{nome:<10}{a:>14.2f}{b:>14.2f}{var:>12}")
    print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Índices de desempenho (M9) de uma rede de filas")
    parser.add_argument("modelo", help=".yml com a rede")
    parser.add_argument("--seeds", type=int, nargs="+", default=[1])
    parser.add_argument("--aleatorios", type=int, default=None)
    parser.add_argument("--tabela", action="store_true",
                        help="imprime a tabela por estado (usa só a primeira semente)")
    parser.add_argument("--comparar", metavar="OUTRO.yml", default=None)
    args = parser.parse_args()

    def rodar(caminho):
        return [analisar(caminho, s, args.aleatorios) for s in args.seeds]

    runs_a = rodar(args.modelo)
    if len(args.seeds) == 1:
        indices, tempo = runs_a[0]
        imprimir_resumo(f"{args.modelo} (seed {args.seeds[0]})", indices, tempo)
        if args.tabela:
            for fid, ind in indices.items():
                imprimir_tabela_estados(fid, ind)
        media_a = indices
    else:
        media_a, desvio_a = media_entre_seeds([r[0] for r in runs_a])
        imprimir_resumo_seeds(args.modelo, args.seeds, media_a, desvio_a)

    if args.comparar:
        runs_b = rodar(args.comparar)
        if len(args.seeds) == 1:
            media_b = runs_b[0][0]
            imprimir_resumo(f"{args.comparar} (seed {args.seeds[0]})", media_b, runs_b[0][1])
        else:
            media_b, desvio_b = media_entre_seeds([r[0] for r in runs_b])
            imprimir_resumo_seeds(args.comparar, args.seeds, media_b, desvio_b)
        imprimir_comparacao(media_a, media_b, "atual", "melhorado")
