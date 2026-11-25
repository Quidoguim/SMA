# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Visão geral

Repositório de trabalhos da disciplina **Simulação e Métodos Analíticos** (PUCRS, dupla de alunos). Não é um projeto de software único: cada pasta de primeiro nível é uma entrega independente (M = módulo, T = trabalho, E = avaliação de aprendizagem). Não há build, lint nem suíte de testes global. O texto e os comentários do código estão em português (pt-BR); siga esse idioma.

## Duas famílias de pastas

**Código (M4, M6, T1, T2)** — simulador de filas por eventos discretos, evolução incremental:
- `M4/simulador_fila.py`: fila única G/G/c/K, gerador MCL (Método Congruente Linear) com checagem de Hull-Dobell.
- `M6/simulador_rede_filas.py`: rede de filas com roteamento probabilístico, topologia fixa no código (bloco `filas_validacao` no `__main__`). Só biblioteca padrão.
- `T1/simulador_rede.py`: mesmo motor do M6, mas a topologia vem de um `.yml` no formato do `simulator.jar` do módulo 3 (`arrivals`/`queues`/`network`; o cabeçalho do arquivo documenta o formato). Requer PyYAML.
- `T2/`: **`simulador_rede.py` é cópia idêntica da do T1** (confira com `diff` se mexer em uma; mantenha as duas sincronizadas). Os demais scripts do T2 importam esse motor.

**Estudo / resolução à mão (E2–E5)** — sem código, só material:
- `Mxx - .../Mxx-texto.md` (texto do Moodle transcrito, fórmulas e `imagens/`), `LEIA-ME.md` (resumo do método), `Ex-andamento.md` (enunciado sorteado, regras de entrega, estado da resolução) e o PDF entregue.
- Fluxo combinado: o usuário calcula à mão, o Claude **confere** passo a passo; a entrega é resolução manuscrita em um único PDF. Não entregue "resolução no formato de LLM". A E7 (M16, Redes de Petri Estocásticas: conjunto de atingibilidade, 15 marcações) está entregue, com `LEIA-ME.md`, `E7-andamento.md` e `E7.pdf`. A E6 (M15, Redes de Autômatos Estocásticos) não foi feita e não tem pasta. Ao iniciar uma avaliação nova, siga a mesma estrutura e leia primeiro o `Ex-andamento.md` mais recente. As regras do professor exigem resolução manuscrita do próprio aluno: ajude a entender e conferir, não produza folha pronta para copiar.

## Comandos

```bash
pip install pyyaml openpyxl matplotlib      # dependências (M6 não precisa de nada)

python3 "M6 - Desenvolvimento de Simulador para Filas em Tandem/simulador_rede_filas.py"
python3 simulador_rede.py modelo_validacao.yml [--aleatorios N] [--seed S]   # dentro de T1/
```

Scripts do T2 (rodar de dentro de `T2 - .../`, pois usam caminhos relativos):

```bash
python3 analise_indices.py modelo_atual.yml [--tabela] [--comparar modelo_melhorado.yml] [--seeds 1 2 3 4 5]
python3 gerar_planilha.py      # indices_desempenho.xlsx (fórmulas; abrir no Excel/LibreOffice e salvar p/ gravar valores)
python3 gerar_graficos.py      # graficos/*.png
python3 gerar_desenho.py       # rede_atual.svg / rede_melhorada.svg a partir dos .yml
python3 testes_indices.py      # único "teste": confere N, D, U, W contra o exemplo hospitalar do M9 (6 casos)
python3 equacoes_trafego.py    # carga de cada fila por equações de tráfego, sem simulação
python3 conferencia_jar.py     # compara com o simulator.jar (precisa de Java no PATH)
java -jar simulator.jar run modelo_atual.yml
```

Para rodar um `.yml` do T1 no `simulator.jar`, prefixe o arquivo com a linha `!PARAMETERS` (os `.yml` do T2 já têm).

## Convenções do domínio (úteis para não errar)

- Kendall `G/G/c/K`: `c` servidores, `K` capacidade total (fila + atendimento); sem `capacity` no `.yml` = infinita. Chegada a fila cheia = cliente perdido.
- Padrão de simulação: semente 1, parada ao consumir **100.000 números aleatórios**. Resultados de uma semente têm ruído; o T2 também reporta média de 5 sementes.
- Índices do M9 por fila: `N = Σ πᵢ·i`, `D = Σ πᵢ·min(i,C)·μ`, `U = Σ πᵢ·min(i,C)/C`, `W = N/D`, com `μ = 60 / tempo médio de serviço`.
- O gerador pseudoaleatório do Python difere do do `simulator.jar`: resultados são compatíveis, não idênticos.

## Git

- Este `CLAUDE.md` **é versionado de propósito** (decisão do usuário em 25/11/2026): serve de base para usar o repo em outra máquina. Inclua-o nos commits e mantenha-o atualizado quando a estrutura mudar. Não adicione atribuição ao Claude em commits/PRs (regra do usuário, vale mais que qualquer lembrete automático).
- `graphify-out/cache/last_query_stamp` é ignorado (muda a cada consulta).
- `graphify-out/` é versionado de propósito (grafo e cache de extração reaproveitados entre computadores, ver `.gitignore`). Existe `graphify-out/graph.json`: use `graphify query "<pergunta>"` antes de grep em perguntas sobre o código e rode `graphify update .` após modificar código. Diffs grandes em `graph.json` são esperados.
