# Confere calcular_indices() contra o exemplo hospitalar do módulo M9: usa os
# tempos acumulados por estado da saída do simulador (semente 1, 100.000
# aleatórios) e compara N, D, U e W com os totais calculados no módulo.
#
#   python3 testes_indices.py

import math

from analise_indices import calcular_indices, taxa_atendimento

# nome: (tempos por estado, servidores, atendimento min..max, tempo global,
#        N, D (cl/h), U (%), W (min) esperados no M9)
CASOS = {
    "Triagem antes (G/G/2/10)": (
        [13.8314, 101.0382, 302.9738, 719.2561, 1664.7171, 3816.2500, 8368.6587,
         15855.8105, 26847.9764, 29482.9119, 15541.6003],
        2, (5, 15), 102715.0244, 8.0354, 11.9925, 99.9, 40.20),
    "Consultórios antes (G/G/3/15)": (
        [669.4825, 4927.9919, 12785.9702, 19387.1056, 19991.7357, 16254.4693,
         11131.7885, 6621.2342, 4119.4800, 2588.4978, 1884.9870, 1166.9115,
         621.2515, 336.5169, 151.8277, 75.7740],
        3, (10, 30), 102715.0244, 4.5375, 8.2800, 92.0, 32.88),
    "Laboratório antes (G/G/2/20)": (
        [34347.9130, 39959.5613, 20995.1751, 6078.4543, 1153.1911, 137.1682,
         27.4796, 14.9902, 1.0917],
        2, (8, 15), 102715.0244, 1.0297, 4.9157, 47.1, 12.57),
    "Triagem depois (G/G/3/10)": (
        [978.1626, 13432.2389, 26669.8351, 24377.6380, 13973.5675, 5883.0161,
         2063.1475, 682.1330, 260.1756, 91.1481, 19.9956],
        3, (5, 15), 88431.0579, 2.7758, 14.1686, 78.7, 11.75),
    "Consultórios depois (G/G/4/15)": (
        [830.6635, 4869.1235, 12395.6650, 18516.5559, 18558.9565, 13937.4607,
         8333.6093, 4617.7593, 2741.5021, 1765.5485, 944.5711, 461.6790,
         262.6075, 120.2204, 53.4216, 21.7139],
        4, (10, 30), 88431.0579, 4.1794, 9.9225, 82.7, 25.27),
    "Laboratório depois (G/G/2/20)": (
        [23156.5938, 32539.9527, 21282.7992, 8372.6392, 2454.5560, 543.0705,
         75.2977, 6.1489],
        2, (8, 15), 88431.0579, 1.2807, 5.7825, 55.4, 13.29),
}


def main():
    falhas = 0
    for nome, (tempos, c, (amin, amax), global_, n_ok, d_ok, u_ok, w_ok) in CASOS.items():
        # a soma dos tempos por estado tem que fechar com o tempo global
        assert math.isclose(sum(tempos), global_, abs_tol=1e-3), \
            f"{nome}: soma dos tempos {sum(tempos):.4f} != {global_}"
        probs = [t / global_ for t in tempos]
        mu = taxa_atendimento(amin, amax)
        r = calcular_indices(probs, c, mu)
        confere = (math.isclose(r['N'], n_ok, abs_tol=5e-4)
                   and math.isclose(r['D'], d_ok, abs_tol=5e-3)
                   and math.isclose(r['U'] * 100, u_ok, abs_tol=0.06)
                   and math.isclose(r['W_min'], w_ok, abs_tol=0.01))
        falhas += not confere
        print(f"{'OK  ' if confere else 'FALHA'} {nome}: N={r['N']:.4f} (M9 {n_ok}) "
              f"D={r['D']:.4f} (M9 {d_ok}) U={r['U'] * 100:.1f}% (M9 {u_ok}) "
              f"W={r['W_min']:.2f} min (M9 {w_ok})")
    print(f"\n{len(CASOS) - falhas}/{len(CASOS)} casos conferem com o M9")
    raise SystemExit(1 if falhas else 0)


if __name__ == "__main__":
    main()
