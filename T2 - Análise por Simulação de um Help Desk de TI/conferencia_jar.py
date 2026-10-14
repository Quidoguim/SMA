# Confere os resultados do simulador_rede.py contra o simulator.jar do módulo 3.
# Roda cada modelo nos dois simuladores com as sementes 1 a 5 (100.000
# aleatórios cada) e compara as perdas e os índices N, D, U e W de cada fila. Os
# geradores de números aleatórios são diferentes, então os resultados não são
# idênticos: o critério é a diferença ficar dentro da variação esperada.
#
#   python3 conferencia_jar.py [modelo.yml ...]
#
# Sem argumentos usa modelo_atual.yml e modelo_melhorado.yml. Precisa de Java no
# PATH. Critérios: N, D, U e W diferem até 5% entre os dois simuladores; as
# perdas, que variam muito entre sementes, diferem até 2 desvios padrão da
# média do simulador_rede.py.

import re
import subprocess
import sys
import tempfile
from pathlib import Path

from analise_indices import analisar, calcular_indices, media_entre_seeds, taxa_atendimento
from simulador_rede import carregar_modelo

SEEDS = [1, 2, 3, 4, 5]
JAR = Path(__file__).with_name("simulator.jar")
TOLERANCIA_INDICES = 0.05
DESVIOS_PERDAS = 2


def rodar_jar(modelo):
    # troca a lista de sementes do .yml e devolve o relatório do simulator.jar
    texto = Path(modelo).read_text(encoding="utf-8")
    sementes = "seeds:\n" + "".join(f"- {s}\n" for s in SEEDS)
    texto, trocas = re.subn(r"seeds:\s*\n(?:\s*-\s*\d+\s*\n?)+", sementes, texto)
    if trocas != 1:
        raise ValueError(f"{modelo}: não encontrei a lista 'seeds' pra trocar")
    with tempfile.TemporaryDirectory() as tmp:
        arquivo = Path(tmp) / "modelo.yml"
        arquivo.write_text(texto, encoding="utf-8")
        saida = subprocess.run(["java", "-jar", str(JAR), "run", str(arquivo)],
                               capture_output=True, text=True, encoding="utf-8",
                               errors="replace", timeout=600)
    return saida.stdout


def ler_relatorio(texto):
    # com várias sementes o relatório do jar soma tempos e perdas entre elas
    filas, atual = {}, None
    for linha in texto.split("REPORT", 1)[1].splitlines():
        m = re.match(r"Queue:\s+(\w+)\s+\(", linha)
        if m:
            atual = filas.setdefault(m.group(1), {"tempos": [], "perdas": 0})
            continue
        m = re.match(r"\s*\d+\s+([\d.,]+)\s+[\d.,]+%", linha)
        if m and atual is not None:
            atual["tempos"].append(float(m.group(1).replace(",", ".")))
            continue
        m = re.match(r"Number of losses:\s+(\d+)", linha)
        if m and atual is not None:
            atual["perdas"] = int(m.group(1))
    return filas


def conferir(modelo):
    jar = ler_relatorio(rodar_jar(modelo))
    filas, _ = carregar_modelo(modelo)
    media, desvio = media_entre_seeds([analisar(modelo, s)[0] for s in SEEDS])
    print(f"{modelo}: simulator.jar x simulador_rede.py (média de {len(SEEDS)} sementes)")
    print(f"{'Fila':<6}{'Índice':<9}{'jar':>11}{'python':>11}{'diferença':>11}  resultado")
    total = falhas = 0
    for f in filas:
        tempos = jar[f.id]["tempos"]
        mu = taxa_atendimento(f.atendimento_min, f.atendimento_max)
        ind = calcular_indices([t / sum(tempos) for t in tempos], f.num_servidores, mu)
        do_jar = {"perdas": jar[f.id]["perdas"] / len(SEEDS), "N": ind["N"],
                  "D": ind["D"], "U": ind["U"], "W_min": ind["W_min"]}
        for chave, rotulo in [("perdas", "Perdas"), ("N", "N"), ("D", "D"), ("U", "U"), ("W_min", "W (min)")]:
            a, b = do_jar[chave], media[f.id][chave]
            if chave == "perdas":
                ok = abs(a - b) <= DESVIOS_PERDAS * desvio[f.id][chave]
                dif = f"{a - b:+.1f}"
            else:
                ok = b == 0 or abs(a - b) / b <= TOLERANCIA_INDICES
                dif = f"{(a - b) / b * 100:+.1f}%" if b else "0,0%"
            total += 1
            falhas += not ok
            print(f"{f.id:<6}{rotulo:<9}{a:>11.4f}{b:>11.4f}{dif:>11}  {'ok' if ok else 'FORA'}")
    print(f"{total - falhas}/{total} comparações dentro do critério\n")
    return falhas


if __name__ == "__main__":
    modelos = sys.argv[1:] or ["modelo_atual.yml", "modelo_melhorado.yml"]
    sys.exit(1 if sum(conferir(m) for m in modelos) else 0)
