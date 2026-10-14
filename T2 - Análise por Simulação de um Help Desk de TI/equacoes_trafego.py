# Confere a carga de cada fila pelas equações de tráfego, sem simulação: a taxa
# de chegada total de cada fila é a chegada externa mais o que as outras filas
# mandam pra ela pelo roteamento,
#
#   lambda_i = externa_i + soma_j( p_ji * lambda_j )
#
# um sistema linear que o script resolve. Com a capacidade da fila (c * mu), a
# carga é rho = lambda_i / (c * mu): acima de 1 a fila não dá conta do que chega,
# satura e perde chamados. A conta ignora as perdas por fila cheia (que aliviam
# as filas seguintes), então só vale como referência; o script mostra ao lado a
# utilização medida na simulação (média de 5 sementes) pra comparar.
#
#   python3 equacoes_trafego.py [modelo.yml ...]
#
# Sem argumentos usa modelo_atual.yml e modelo_melhorado.yml. Taxas em chamados
# por hora.

import sys

from analise_indices import analisar, media_entre_seeds, taxa_atendimento
from simulador_rede import carregar_modelo

SEEDS = [1, 2, 3, 4, 5]


def resolver(matriz, termos):
    # eliminação de Gauss com pivô parcial
    n = len(termos)
    a = [linha[:] + [termos[i]] for i, linha in enumerate(matriz)]
    for col in range(n):
        pivo = max(range(col, n), key=lambda r: abs(a[r][col]))
        a[col], a[pivo] = a[pivo], a[col]
        for r in range(n):
            if r != col:
                fator = a[r][col] / a[col][col]
                a[r] = [x - fator * y for x, y in zip(a[r], a[col])]
    return [a[i][n] / a[i][i] for i in range(n)]


def conferir(modelo):
    filas, _ = carregar_modelo(modelo)
    ids = [f.id for f in filas]
    n = len(filas)
    externa = [60 / ((f.chegada_min + f.chegada_max) / 2) if f.chegada_min is not None else 0.0
               for f in filas]
    # (I - P^T) lambda = externa, com P[i][j] = probabilidade de i mandar pra j
    matriz = [[(1.0 if i == j else 0.0) for j in range(n)] for i in range(n)]
    for i, f in enumerate(filas):
        for destino, p in f.destinos.items():
            matriz[ids.index(destino)][i] -= p
    chegada = resolver(matriz, externa)
    media, _ = media_entre_seeds([analisar(modelo, s)[0] for s in SEEDS])

    print(f"{modelo}: equações de tráfego x utilização simulada (média de {len(SEEDS)} sementes)")
    print(f"{'Fila':<6}{'Chegada (cham/h)':>18}{'Capacidade (cham/h)':>21}{'Carga':>8}{'U simulada':>12}")
    for f, lam in zip(filas, chegada):
        capacidade = f.num_servidores * taxa_atendimento(f.atendimento_min, f.atendimento_max)
        print(f"{f.id:<6}{lam:>18.3f}{capacidade:>21.3f}{lam / capacidade:>8.2f}"
              f"{media[f.id]['U']:>12.2f}")
    print()


if __name__ == "__main__":
    for modelo in sys.argv[1:] or ["modelo_atual.yml", "modelo_melhorado.yml"]:
        conferir(modelo)
