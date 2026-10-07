# Como rodar e analisar o T2

Análise por simulação de uma rede de filas própria: o atendimento de chamados
de um help desk de TI, com três níveis (N1, N2 e N3) e retorno de chamados
entre eles. Os scripts usam o simulador do T1 (`simulador_rede.py`, mesmo motor
do M6) e calculam os índices de desempenho do M9. Requisitos: Python 3 e

```bash
pip install pyyaml openpyxl
```

## O modelo

Unidade de tempo: minutos. Cada cliente é um chamado.

| Fila | Papel | Kendall | Chegadas externas | Atendimento |
|---|---|---|---|---|
| Q1 | N1 - triagem | G/G/2 (capacidade ilimitada) | entre 4 e 8 | entre 6 e 10 |
| Q2 | N2 - especialista | G/G/2/10 | não tem | entre 20 e 40 |
| Q3 | N3 - desenvolvimento | G/G/1/5 | não tem | entre 30 e 60 |

Roteamento (o que falta pra somar 1 é chamado resolvido, que sai da rede):
Q1 → Q2 com 0,45; Q2 → Q3 com 0,30; Q2 → Q1 com 0,10 (faltou informação);
Q3 → Q2 com 0,20 (correção devolvida). O primeiro chamado chega em 6,0.

**Melhoria** (`modelo_melhorado.yml`): só o roteamento Q1 → Q2 cai de 0,45 para
0,30, ou seja, o N1 passa a resolver 70% dos chamados no primeiro contato (base
de conhecimento e treinamento). Servidores e capacidades não mudam.

## Arquivos

- `modelo_atual.yml` e `modelo_melhorado.yml`: as duas redes, no formato do
  simulador do módulo 3.
- `simulador_rede.py`: simulador por eventos discretos (cópia do T1).
- `analise_indices.py`: simula e calcula população (N), vazão (D), utilização
  (U) e tempo de resposta (W).
- `gerar_planilha.py`: gera `indices_desempenho.xlsx`.
- `indices_desempenho.xlsx`: planilha de cálculo dos índices, com fórmulas.
- `testes_indices.py`: confere o cálculo dos índices contra o exemplo do M9.
- `simulator.jar`: simulador do módulo 3, usado pra conferir os resultados.

## Calculando os índices

```bash
python3 analise_indices.py modelo_atual.yml
python3 analise_indices.py modelo_atual.yml --tabela
python3 analise_indices.py modelo_atual.yml --comparar modelo_melhorado.yml
python3 analise_indices.py modelo_atual.yml --comparar modelo_melhorado.yml --seeds 1 2 3 4 5
```

Sem opções, simula com a semente 1 e 100.000 aleatórios (mesmo critério do M9) e
mostra, por fila: perdas, N, D, U e W. `--tabela` detalha por estado, como nas
tabelas do módulo. `--comparar` põe os dois modelos lado a lado com a variação
percentual. `--seeds` repete com várias sementes e mostra média e desvio padrão.

As fórmulas do M9, para cada fila (`K` = capacidade, `C` = servidores, `π_i` =
probabilidade do estado `i`):

- `N = Σ π_i · i`
- `D = Σ π_i · min(i, C) · μ`
- `U = Σ π_i · min(i, C) / C`
- `W = N / D`

`μ` é a taxa de atendimento de um servidor, em chamados por hora: `60 / tempo
médio de atendimento` (média entre o mínimo e o máximo). Por isso `D` sai em
chamados/hora e `W` em horas, que o script mostra em minutos.

## Planilha

```bash
python3 gerar_planilha.py
```

Gera `indices_desempenho.xlsx` com uma aba de comparação, uma de parâmetros,
uma por fila e modelo (tempo por estado → probabilidade, N, D, U e W, todos
como fórmulas do Excel) e uma com os resultados de 5 sementes. Azul é valor que
veio do simulador ou do `.yml`, preto é fórmula, verde é ligação entre abas e
amarelo é o parâmetro alterado na melhoria. Se for gerada de novo, abra no
Excel ou LibreOffice e salve, pra os valores calculados ficarem gravados no
arquivo.

## Conferindo a implementação

```bash
python3 testes_indices.py
```

Usa os tempos por estado do exemplo hospitalar do M9 (semente 1) e confere N,
D, U e W das seis tabelas do módulo (triagem, consultórios e laboratório, antes
e depois das melhorias). Os seis casos batem.

Os dois modelos também rodam direto no `simulator.jar` do módulo 3 (os
arquivos já têm a linha `!PARAMETERS`):

```bash
java -jar simulator.jar run modelo_atual.yml
```

Os geradores de números aleatórios são diferentes, então os números não são
idênticos aos do `simulador_rede.py`, mas são compatíveis: perdas no Q2 do
modelo atual são ~2.060 aqui (semente 1) e ~2.260 no `simulator.jar`, contra
uma média de ~2.250 em 5 sementes (desvio padrão de ~130).
