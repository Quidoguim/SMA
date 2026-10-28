# E3 - Andamento da resolução

Anotações para continuar a E3 em outra máquina. Prazo: **quarta, 28/10/2026, 23:59**
(sala de entrega do Moodle "E3 | Avaliação de Aprendizagem | Turma 691"). Não são
aceitas entregas com atraso.

## Regras de entrega

- Resolução **à mão livre**, em papel (ou tablet com caneta, desde que desenhada à
  mão, não digitada nem copiada), digitalizada em **um único PDF**.
- Tem que mostrar o **desenvolvimento** até o resultado; só a resposta, mesmo certa,
  não vale.
- Resolução no formato de LLM, e não no formato usado no material da disciplina,
  não vale.
- Resolver a proposta **sorteada** pelo Moodle (a de outra situação é zerada).

## Enunciado sorteado — situação 5, biruta

> A biruta de sinalização é um instrumento usado em aeroportos, heliportos e
> aeródromos para mostrar o sentido do vento e orientar pilotos na decolagem e na
> aterrissagem.
>
> Construa uma cadeia de Markov assumindo, de forma simplificada, que a biruta pode
> apontar para 4 direções: **Norte (N), Sul (S), Leste (L) e Oeste (O)**. Ocorrem as
> seguintes mudanças de estado, com as respectivas frequências:
>
> - De **Norte** para: Sul (4 vezes por hora), Oeste (6 vezes por hora)
> - De **Sul** para: Leste (4 vezes por hora), Oeste (2 vezes por hora)
> - De **Leste** para: Norte (1 vez por hora)
> - De **Oeste** para: Norte (4 vezes por hora), Leste (2 vezes por hora)
>
> Dado que as frequências das mudanças de estado são regidas por distribuições
> exponenciais, **qual é a probabilidade de a biruta apontar para o Norte?**
>
> Mostre passo a passo a solução numérica para encontrar as probabilidades dos
> estados da cadeia de Markov, ou seja, construa o gerador infinitesimal e resolva o
> sistema de equações a fim de encontrar a distribuição de probabilidade dos estados
> da biruta.

## Critérios de avaliação

| Parte | Pontos |
|---|---|
| Montagem do modelo da Cadeia de Markov | 10 |
| Matriz de transição / gerador infinitesimal | 20 |
| Montagem do sistema de equações | 20 |
| Resolução do sistema de equações | 30 |
| Cálculo das probabilidades | 20 |

## Como vamos resolver

Mesmo formato da E2: um passo de cada vez, cada valor calculado à mão e conferido
antes de seguir. No papel, seguir a ordem do exemplo do laboratório no
[M12-texto.md](<M12 - Cadeias de Markov/M12-texto.md>): diagrama, matriz de
transição, gerador infinitesimal, πQ = 0, sistema, valor arbitrário, normalização.

Taxas já estão em "vezes por hora" (todas na mesma unidade), não precisa converter.

## Roteiro (a preencher conforme for conferido)

- [x] **Passo 1 — modelo:** desenhar os 4 estados (N, S, L, O) e as setas com as
      taxas do enunciado.
- [x] **Passo 2 — matriz de transição:** linha = estado de origem, coluna = destino.
- [x] **Passo 3 — gerador infinitesimal Q:** diagonal = ajuste para cada linha somar
      zero.
- [x] **Passo 4 — sistema de equações:** (P_N P_S P_L P_O) × Q = 0, uma equação por
      coluna.
- [x] **Passo 5 — resolução:** escolher um valor arbitrário para uma variável e achar
      as outras; usar a equação que sobrar para conferir.
- [x] **Passo 6 — probabilidades:** somar as proporções, dividir cada uma pela soma,
      conferir que dá 100%, e responder P(Norte).

### Feito até agora (conferido)

**Passo 1 — modelo (conferido em 27/10)**

4 estados (N, S, L, O) e 7 setas, todas com taxa em vezes por hora:

```
N → S : 4      S → L : 4      L → N : 1      O → N : 4
N → O : 6      S → O : 2                     O → L : 2
```

Ajuste para a versão a limpo: no esboço, o rótulo "1 vez p/ hora" ficou encostado
no arco de fora (O → N), e o arco de dentro (L → N) ficou sem número. O 1 é do
L → N; o arco O → N fica só com o 4. A versão a limpo (`Cadeia de Markov.pdf`, nesta
pasta) já está certa: as 7 setas estão com o número no lugar.

**Passo 2 — matriz de transição (conferido em 27/10)**

Ordem N, S, L, O nas linhas (origem) e nas colunas (destino). Arquivo
`Matriz de transição.pdf`, nesta pasta.

```
       N   S   L   O
N   [  0   4   0   6 ]
S   [  0   0   4   2 ]
L   [  1   0   0   0 ]
O   [  4   0   2   0 ]
```

Conferências: 7 números diferentes de zero (7 setas); cada linha tem tantos números
quantas setas saem do estado (N 2, S 2, L 1, O 2).

**Passo 3 — gerador infinitesimal (conferido em 27/10)**

Diagonal = −(soma das taxas que saem do estado):

- N: −(4 + 6) = −10
- S: −(4 + 2) = −6
- L: −(1) = −1
- O: −(4 + 2) = −6

```
        N    S    L    O
N   [ −10    4    0    6 ]
S   [   0   −6    4    2 ]
L   [   1    0   −1    0 ]
O   [   4    0    2   −6 ]
```

Conferência: cada linha soma 0.

**Passo 4 — sistema de equações (conferido em 27/10)**

(P_N P_S P_L P_O) × Q = (0 0 0 0), uma equação por coluna:

```
(1) coluna N:  −10·P_N + 1·P_L + 4·P_O = 0
(2) coluna S:    4·P_N − 6·P_S         = 0
(3) coluna L:    4·P_S − 1·P_L + 2·P_O = 0
(4) coluna O:    6·P_N + 2·P_S − 6·P_O = 0
```

Conferência: termos positivos = setas que chegam (N 2, S 1, L 2, O 2).

**Passo 5 — resolução (em andamento)**

1. Condição inicial: **P_S = 1**
2. Calcular P_N (equação 2): 4·P_N − 6·1 = 0 → 4·P_N = 6 → **P_N = 1,5**

3. Calcular P_O (equação 4): 6·1,5 + 2·1 − 6·P_O = 0 → 9 + 2 − 6·P_O = 0 →
   11 = 6·P_O → **P_O = 11 ÷ 6 = 1,8333** (atenção: (−11) ÷ (−6) é positivo)
4. Calcular P_L (equação 1): −10·1,5 + P_L + 4·1,8333 = 0 → −15 + P_L + 7,3333 = 0
   → P_L − 7,6667 = 0 → **P_L = 7,6667** (com o valor completo de P_O na
   calculadora; usando 1,8333 arredondado dá 7,6668)

5. Conferência (equação 3): 4·1 − 7,6667 + 2·1,8333 = 4 − 7,6667 + 3,6666 =
   −0,0001 ≈ 0 ✓ (com 7,6668 dava −0,0002; com os valores completos da
   calculadora dá 0 exato)

Passo 5 concluído.

**Passo 6 — probabilidades (conferido em 27/10)**

P = Σ Pⱼ = 1,5 + 1 + 7,6667 + 1,8333 = **12**

| Estado | Conta | Probabilidade |
|---|---|---|
| N | 1,5 ÷ 12 | 0,1250 = 12,50% |
| S | 1 ÷ 12 | 0,0833 = 8,33% |
| L | 7,6667 ÷ 12 | 0,6389 = 63,89% |
| O | 1,8333 ÷ 12 | 0,1528 = 15,28% |

Conferência: 0,1250 + 0,0833 + 0,6389 + 0,1528 = 1,0000 = 100% ✓

Resposta: a probabilidade de a biruta apontar para o Norte é de **12,50%**.

**Entregue em 28/10/2026** no Moodle, em um único PDF escrito à mão:
[E3.pdf](E3.pdf). A versão entregue usou P_L = 7,6668 e a soma 12,0001; a resposta
final, 12,50%, é a mesma.
