# Gera o desenho da rede de filas do T2 em SVG (rede_atual.svg e
# rede_melhorada.svg), no estilo simples dos desenhos do M9: cada fila com sua
# sala de espera e servidor, notação de Kendall, intervalo de atendimento,
# servidores, capacidade, chegadas externas e probabilidades de roteamento.
# Os números vêm dos .yml, então o desenho não diverge dos modelos. No desenho
# da melhoria, as probabilidades que mudaram aparecem em vermelho, com o valor
# anterior entre parênteses.
#
#   python3 gerar_desenho.py [--atual modelo_atual.yml]
#                            [--melhorado modelo_melhorado.yml]
#
# O leiaute (Q1, Q2 e Q3 em linha, retornos em arco) é fixo pra topologia do
# help desk; os parâmetros e as probabilidades é que são lidos dos arquivos. O
# SVG abre em qualquer navegador e pode ser importado no Canva.
#
# Requisito: pyyaml (pip install pyyaml).

import argparse

from analise_indices import kendall
from simulador_rede import carregar_modelo

NOMES = {"Q1": "Triagem (N1)", "Q2": "Especialista (N2)", "Q3": "Desenvolvimento (N3)"}

W, H = 1200, 500
CY = 215                                  # altura do centro das filas
BX = {"Q1": 170, "Q2": 530, "Q3": 890}    # x da sala de espera de cada fila
BUF_W, BUF_H, RAIO = 120, 50, 30

COR, VERMELHO = "#1f3a5f", "#c00000"


def pt(p):
    return f"{p:.2f}".replace(".", ",")


def texto(x, y, conteudo, tam=16, peso="normal", cor=COR, ancora="middle"):
    return (f'<text x="{x}" y="{y}" font-size="{tam}" font-weight="{peso}" fill="{cor}" '
            f'text-anchor="{ancora}">{conteudo}</text>')


def rotulo(x, y, p, antes=None, ancora="middle", acima=False):
    # probabilidade da seta; se mudou, em vermelho com o valor anterior. Com
    # acima=True o valor anterior fica embaixo e o novo valor sobe (setas
    # horizontais), pra o texto não cair em cima da linha.
    if antes is None:
        return texto(x, y, pt(p), ancora=ancora)
    dy_valor, dy_antes = (-17, 0) if acima else (0, 17)
    return (texto(x, y + dy_valor, pt(p), peso="bold", cor=VERMELHO, ancora=ancora) + "\n"
            + texto(x, y + dy_antes, f"(antes {pt(antes)})", 13, cor=VERMELHO, ancora=ancora))


def seta(caminho):
    return f'<path d="{caminho}" fill="none" stroke="{COR}" stroke-width="2" marker-end="url(#ponta)"/>'


def fila_svg(fid, f, numero):
    bx = BX[fid]
    cx = bx + BUF_W + RAIO
    y0 = CY - BUF_H / 2
    partes = [f'<rect x="{bx}" y="{y0}" width="{BUF_W}" height="{BUF_H}" fill="none" '
              f'stroke="{COR}" stroke-width="2"/>']
    for k in (30, 60, 90):
        partes.append(f'<line x1="{bx + k}" y1="{y0}" x2="{bx + k}" y2="{y0 + BUF_H}" '
                      f'stroke="{COR}" stroke-width="2"/>')
    partes.append(f'<circle cx="{cx}" cy="{CY}" r="{RAIO}" fill="none" stroke="{COR}" stroke-width="2"/>')
    partes.append(texto(cx, CY + 7, numero, 22))

    # informações abaixo da fila
    centro = bx + (BUF_W + 2 * RAIO) / 2
    capacidade = "capacidade ilimitada" if f.capacidade is None else f"capacidade {f.capacidade}"
    servidores = "servidor" if f.num_servidores == 1 else "servidores"
    base = CY + 185
    partes += [
        texto(centro, base, f"{fid} – {NOMES[fid]}", 17, "bold"),
        texto(centro, base + 24, kendall(f.num_servidores, f.capacidade), 18),
        texto(centro, base + 48, f"atendimento: {f.atendimento_min:g}..{f.atendimento_max:g} min"),
        texto(centro, base + 70, f"{f.num_servidores} {servidores}, {capacidade}"),
    ]
    return "\n".join(partes)


def probabilidades(f):
    # {destino: p} mais a saída da rede ("SAI") com o que falta pra 1
    tabela = dict(f.destinos)
    tabela["SAI"] = 1.0 - sum(f.destinos.values())
    return tabela


def desenhar(filas, titulo, referencia=None):
    por_id = {f.id: f for f in filas}
    prob = {fid: probabilidades(f) for fid, f in por_id.items()}
    antes = {fid: probabilidades(f) for fid, f in referencia.items()} if referencia else None

    def anterior(origem, destino):
        # valor anterior da probabilidade, só se mudou
        if antes and abs(prob[origem].get(destino, 0) - antes[origem].get(destino, 0)) > 1e-9:
            return antes[origem].get(destino, 0)
        return None

    cx = {fid: BX[fid] + BUF_W + RAIO for fid in BX}
    q1 = por_id["Q1"]
    elementos = [f'<rect width="{W}" height="{H}" fill="white"/>', texto(40, 38, titulo, 20, "bold", ancora="start")]

    # chegadas externas em Q1
    elementos.append(seta(f"M 30,{CY} L {BX['Q1'] - 2},{CY}"))
    elementos.append(texto(100, CY - 32, "chegadas externas", 14))
    elementos.append(texto(100, CY - 14, f"{q1.chegada_min:g}..{q1.chegada_max:g} min", 14))

    # setas para frente: Q1 -> Q2 e Q2 -> Q3
    for o, d in (("Q1", "Q2"), ("Q2", "Q3")):
        x1, x2 = cx[o] + RAIO, BX[d] - 2
        elementos.append(seta(f"M {x1},{CY} L {x2},{CY}"))
        elementos.append(rotulo((x1 + x2) / 2, CY - 14, prob[o][d], anterior(o, d), acima=True))

    # saídas da rede: Q1 e Q2 descem, Q3 sai pela direita
    for o in ("Q1", "Q2"):
        elementos.append(seta(f"M {cx[o]},{CY + RAIO} L {cx[o]},{CY + RAIO + 55}"))
        elementos.append(rotulo(cx[o] + 10, CY + RAIO + 28, prob[o]["SAI"], anterior(o, "SAI"), "start"))
    x3 = cx["Q3"] + RAIO
    elementos.append(seta(f"M {x3},{CY} L {W - 30},{CY}"))
    elementos.append(rotulo((x3 + W - 30) / 2, CY - 14, prob["Q3"]["SAI"], anterior("Q3", "SAI"), acima=True))

    # retornos: Q2 -> Q1 por cima e Q3 -> Q2 por baixo
    ini, fim = cx["Q2"], BX["Q1"] + BUF_W / 2
    elementos.append(seta(f"M {ini},{CY - RAIO} C {ini},{CY - 150} {fim},{CY - 150} {fim},{CY - BUF_H / 2 - 2}"))
    elementos.append(rotulo((ini + fim) / 2, CY - 132, prob["Q2"]["Q1"], anterior("Q2", "Q1"), acima=True))
    ini, fim = cx["Q3"], BX["Q2"] + BUF_W / 2
    elementos.append(seta(f"M {ini},{CY + RAIO} C {ini},{CY + 150} {fim},{CY + 150} {fim},{CY + BUF_H / 2 + 2}"))
    elementos.append(rotulo((ini + fim) / 2, CY + 106, prob["Q3"]["Q2"], anterior("Q3", "Q2"), acima=True))

    for numero, fid in enumerate(("Q1", "Q2", "Q3"), start=1):
        elementos.append(fila_svg(fid, por_id[fid], str(numero)))

    ponta = ('<marker id="ponta" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="10" '
             f'markerHeight="10" markerUnits="userSpaceOnUse" orient="auto">'
             f'<path d="M0,0 L10,5 L0,10 z" fill="{COR}"/></marker>')
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
            f'viewBox="0 0 {W} {H}" font-family="Arial, Helvetica, sans-serif">\n'
            f'<defs>{ponta}</defs>\n' + "\n".join(elementos) + "\n</svg>\n")


def main():
    parser = argparse.ArgumentParser(description="Desenho da rede de filas do T2 (SVG)")
    parser.add_argument("--atual", default="modelo_atual.yml")
    parser.add_argument("--melhorado", default="modelo_melhorado.yml")
    args = parser.parse_args()

    atual, _ = carregar_modelo(args.atual)
    melhorado, _ = carregar_modelo(args.melhorado)
    referencia = {f.id: f for f in atual}

    with open("rede_atual.svg", "w", encoding="utf-8") as arq:
        arq.write(desenhar(atual, "Modelo atual"))
    with open("rede_melhorada.svg", "w", encoding="utf-8") as arq:
        arq.write(desenhar(melhorado, "Modelo melhorado", referencia))
    print("Desenhos gerados: rede_atual.svg e rede_melhorada.svg")


if __name__ == "__main__":
    main()
