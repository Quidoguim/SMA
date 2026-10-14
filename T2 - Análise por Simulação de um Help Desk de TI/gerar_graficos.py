# Gera os gráficos de probabilidade dos estados das filas do T2 (PNG), na pasta
# graficos/. Para cada fila (Q1, Q2 e Q3) saem dois gráficos de colunas:
#
#   prob_estados_atual_Qn.png        só o modelo atual
#   prob_estados_comparacao_Qn.png   modelo atual x modelo melhorado
#
# As probabilidades vêm da simulação com a semente 1 e 100.000 aleatórios (as
# mesmas das abas por fila da planilha). O estado é o número de chamados na fila
# (esperando + em atendimento); nas filas de capacidade finita, o estado K é "fila
# cheia", em que o chamado que chega é perdido. Cores: atual em azul e melhorado em
# laranja em todos os gráficos.
#
#   python3 gerar_graficos.py [--atual modelo_atual.yml]
#                             [--melhorado modelo_melhorado.yml]
#                             [--saida graficos]
#
# Requisitos: pyyaml e matplotlib (pip install pyyaml matplotlib).

import argparse
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import Patch
from matplotlib.ticker import FuncFormatter, MultipleLocator

from analise_indices import kendall
from simulador_rede import carregar_modelo, simular_rede

NOMES = {"Q1": "N1 – Triagem", "Q2": "N2 – Especialista", "Q3": "N3 – Desenvolvimento"}

SUPERFICIE, TINTA, TINTA_2 = "#fcfcfb", "#0b0b0b", "#52514e"
MUDO, GRADE, BASE = "#898781", "#e1e0d9", "#c3c2b7"
COR_ATUAL, COR_MELHORADO = "#2a78d6", "#eb6834"

LARGURA_POL, ALTURA_POL, DPI = 8, 4.5, 200
ESPESSURA_MAX_PX = 46  # coluna fina: no máximo ~23 px em tela de 96 dpi

plt.rcParams["font.family"] = ["Segoe UI", "Arial", "DejaVu Sans"]


def pct(v, casas=1):
    return f"{v:.{casas}f}".replace(".", ",") + "%"


def grafico(fid, filas, series, subtitulo, arquivo):
    # filas: Fila do modelo (pra capacidade); series: [(rótulo, probs, cor)]
    f = filas[fid]
    n_estados = max(len(p) for _, p, _ in series)
    probs = [[100 * p[i] if i < len(p) else 0.0 for i in range(n_estados)] for _, p, _ in series]
    topo = max(max(p) for p in probs)

    fig = plt.figure(figsize=(LARGURA_POL, ALTURA_POL), dpi=DPI, facecolor=SUPERFICIE)
    esq, base, larg, alt = 0.085, 0.19, 0.89, 0.60
    ax = fig.add_axes([esq, base, larg, alt], facecolor=SUPERFICIE)

    # espessura da coluna limitada em pixels, pra gráficos com poucos estados
    slot_px = larg * LARGURA_POL * DPI / n_estados
    n = len(series)
    largura = min(0.8 / n - 0.04, ESPESSURA_MAX_PX / slot_px)
    passo = largura + 0.04  # 0,04 de vão entre colunas vizinhas
    deslocamentos = [(k - (n - 1) / 2) * passo for k in range(n)]
    xs = range(n_estados)

    for (rotulo, _, cor), valores, d in zip(series, probs, deslocamentos):
        ax.bar([x + d for x in xs], valores, width=largura, color=cor, linewidth=0, zorder=3)

    # rótulos só nos pontos que contam a história: o pico de cada série e a fila cheia.
    # Com duas séries, o rótulo da esquerda termina na borda direita da sua coluna e o
    # da direita começa na borda esquerda da dela, pra não se encostarem.
    for k, (valores, d) in enumerate(zip(probs, deslocamentos)):
        alvos = {max(range(n_estados), key=lambda i: valores[i])}
        if f.capacidade is not None:
            alvos.add(f.capacidade)
        if n == 2:
            alinhamento = "right" if k == 0 else "left"
            deslocamento_x = d + (largura / 2 if k == 0 else -largura / 2)
        else:
            alinhamento, deslocamento_x = "center", d
        for i in sorted(alvos):
            ax.text(i + deslocamento_x, valores[i] + topo * 0.02, pct(valores[i]),
                    ha=alinhamento, va="bottom", fontsize=8.5, color=TINTA)

    # eixos
    passo_y = 10 if topo > 25 else 5
    limite = (int(topo * 1.18 / passo_y) + 1) * passo_y
    ax.set_ylim(0, limite)
    ax.set_xlim(-0.6, n_estados - 0.4)
    ax.yaxis.set_major_locator(MultipleLocator(passo_y))
    ax.yaxis.set_major_formatter(FuncFormatter(lambda v, _: f"{v:.0f}%"))
    ax.yaxis.grid(True, color=GRADE, linewidth=0.8, zorder=0)
    ax.set_axisbelow(True)
    for lado in ("top", "right", "left"):
        ax.spines[lado].set_visible(False)
    ax.spines["bottom"].set_color(BASE)
    ax.tick_params(axis="y", length=0, colors=MUDO, labelsize=9)
    ax.tick_params(axis="x", length=0, colors=TINTA_2, labelsize=9.5, pad=6)
    ax.set_xticks(list(xs))
    ax.set_xticklabels([f"{i}\n(cheia)" if i == f.capacidade else str(i) for i in xs])
    ax.set_xlabel("Estado: número de chamados na fila (esperando + em atendimento)",
                  fontsize=9.5, color=TINTA_2, labelpad=8)

    # título, subtítulo e legenda (legenda só quando há duas séries)
    fig.text(esq, 0.935, f"{fid} · {NOMES[fid]} ({kendall(f.num_servidores, f.capacidade)})",
             fontsize=14, fontweight="bold", color=TINTA, va="center")
    fig.text(esq, 0.875, subtitulo, fontsize=10.5, color=TINTA_2, va="center")
    if n > 1:
        fig.legend([Patch(facecolor=cor, linewidth=0) for _, _, cor in series],
                   [r for r, _, _ in series], loc="center right",
                   bbox_to_anchor=(0.975, 0.905), ncol=n, frameon=False, fontsize=10.5,
                   labelcolor=TINTA, handlelength=1.0, handleheight=1.0, columnspacing=1.6)

    fig.savefig(arquivo, dpi=DPI, facecolor=SUPERFICIE)
    plt.close(fig)


def main():
    parser = argparse.ArgumentParser(description="Gráficos de probabilidade dos estados (T2)")
    parser.add_argument("--atual", default="modelo_atual.yml")
    parser.add_argument("--melhorado", default="modelo_melhorado.yml")
    parser.add_argument("--saida", default="graficos")
    args = parser.parse_args()

    filas_atual, aleatorios = carregar_modelo(args.atual)
    filas_melhorado, _ = carregar_modelo(args.melhorado)
    sim_atual = simular_rede(filas_atual, aleatorios, seed=1)
    sim_melhorado = simular_rede(filas_melhorado, aleatorios, seed=1)
    por_id = {f.id: f for f in filas_atual}

    pasta = Path(args.saida)
    pasta.mkdir(exist_ok=True)
    for fid in por_id:
        atual = sim_atual["filas"][fid]["probabilidades"]
        melhorado = sim_melhorado["filas"][fid]["probabilidades"]
        grafico(fid, por_id, [("Modelo atual", atual, COR_ATUAL)],
                "Probabilidade de cada estado, modelo atual (semente 1, 100.000 aleatórios)",
                pasta / f"prob_estados_atual_{fid}.png")
        grafico(fid, por_id, [("Modelo atual", atual, COR_ATUAL),
                              ("Modelo melhorado", melhorado, COR_MELHORADO)],
                "Probabilidade de cada estado, atual × melhorado (semente 1)",
                pasta / f"prob_estados_comparacao_{fid}.png")
    print(f"Gráficos gerados em {pasta}/")


if __name__ == "__main__":
    main()
