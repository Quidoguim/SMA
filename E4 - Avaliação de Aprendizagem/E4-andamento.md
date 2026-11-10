# E4 - Andamento da resolução

Anotações para continuar a E4 em outra máquina. Prazo: **quarta, 04/11/2026, 23:59**
(sala de entrega do Moodle "E4 | Avaliação de Aprendizagem | T. 691"). O sistema
bloqueia o envio depois das 23h59.

## Regras de entrega

- Resolução **à mão livre**, em papel (ou tablet com caneta, desde que desenhada à
  mão, não digitada nem copiada), digitalizada em **um único PDF**.
- Tem que mostrar o **desenvolvimento** até o resultado; só a resposta, mesmo certa,
  não vale.
- Resolução no formato de LLM, e não no formato usado no material da disciplina,
  não vale.
- Resolver a proposta **sorteada** pelo Moodle (a de outra situação é zerada).

## Enunciado sorteado — situação 3, rede aberta

![Rede sorteada](<M13 - Redes Abertas de Filas/imagens/00-rede-sorteada-situacao-3.jpg>)

> Dada a rede de filas de espera a seguir, assuma **S1 = 0,1, S2 = 0,2, S3 = 0,15,
> S4 = 0,05** e responda:
>
> 1. Qual fila possui o **maior tempo de resposta**? Isto é, em qual fila os clientes
>    passam mais tempo até conseguirem ser finalmente atendidos? Além de indicar a
>    fila em questão, indique numericamente quanto tempo os clientes levam em média
>    nesta fila.
> 2. Qual é a fila com a **menor população média**? Além de indicar a fila em
>    questão, indique numericamente quantos clientes em média tem esta fila.

Leitura do desenho (a conferir no Passo 1):

```
entrada externa: 4 cl/h na fila 1, 1 cl/h na fila 3
fila 1 → fila 2 : 0,2        fila 1 → fila 3 : 0,8
fila 2 → fila 4 : (sem número na seta)
fila 3 → fila 4 : 0,5        fila 3 → sai    : 0,5
fila 4 → fila 2 : 0,4        fila 4 → sai    : 0,6
```

## Critérios de avaliação

| Parte | Pontos |
|---|---|
| Cálculo das taxas de visita | 20 |
| Cálculo da vazão | 20 |
| Cálculo da utilização | 20 |
| Cálculo do tempo de resposta | 10 |
| Cálculo da população | 10 |

(O Moodle lista só esses 80 pontos; os outros 20 devem ser das respostas às duas
perguntas.)

## Como vamos resolver

Mesmo formato da E2 e da E3: um passo de cada vez, cada valor calculado à mão e
conferido antes de seguir. No papel, seguir a ordem do exemplo do
[M13-texto.md](<M13 - Redes Abertas de Filas/M13-texto.md>): fechar a rede com a
fila X, taxas de visita, vazão, utilização, tempo de resposta, população.

Fórmulas (M13):

- dᵢ = Vᵢ × Σ Lⱼ
- uᵢ = dᵢ × Sᵢ
- wᵢ = Sᵢ / (1 − uᵢ)
- nᵢ = uᵢ / (1 − uᵢ)

Unidade: as chegadas estão em clientes por hora, então os Sᵢ ficam em horas por
cliente e os wᵢ saem em horas.

## Roteiro (a preencher conforme for conferido)

- [ ] **Passo 1 — fechar a rede:** redesenhar com a fila auxiliar X; achar Σ L e a
      fração da entrada externa que vai para cada fila.
- [ ] **Passo 2 — taxas de visita:** Vₓ = 1; uma equação por fila (V₁, V₂, V₃, V₄);
      resolver. Conferência: o que sai para X soma 1.
- [ ] **Passo 3 — vazão:** d₁ a d₄.
- [ ] **Passo 4 — utilização:** u₁ a u₄ (conferir que todas ficam abaixo de 1).
- [ ] **Passo 5 — tempo de resposta:** w₁ a w₄.
- [ ] **Passo 6 — população:** n₁ a n₄.
- [ ] **Passo 7 — respostas:** maior w (fila e valor) e menor n (fila e valor).

### Feito até agora (conferido)

**Passo 1 — fechar a rede (04/11)**

- Σ L = 4 + 1 = **5 cl/h**
- X manda para a fila 1: 4/5 = 0,8; para a fila 3: 1/5 = 0,2
- Seta 2 → 4 vale **1** (única saída da fila 2: 100% vai para a fila 4)
- Saídas que vão para X: fila 3 (0,5) e fila 4 (0,6)

Desenho: copiar a rede e acrescentar a fila X embaixo, com setas tracejadas
das saídas (3 e 4) para X e de X para as entradas (1 e 3), como no exemplo do M13.

**Passo 2 — taxas de visita (montado, falta resolver)**

Uma equação por fila: soma de (fração da seta que chega × V de quem manda).

```
Vx = 1
V1 = (4/5 × Vx)
V2 = (0,2 × V1) + (0,4 × V4)
V3 = (1/5 × Vx) + (0,8 × V1)
V4 = (1 × V2) + (0,5 × V3)
```

Conferência: (0,5 × V3) + (0,6 × V4) = 1 (tudo que sai volta para X).

- **V1 = 4/5 × 1 = 0,8** (conferido)
- **V3 = (1/5 × 1) + (0,8 × 0,8) = 0,2 + 0,64 = 0,84** (conferido; no primeiro
  rascunho faltou somar o 0,2 e tinha dado 0,64)
- **V2** (conferido): V2 = 0,16 + 0,4 × (V2 + 0,42) → V2 = 0,16 + 0,4·V2 + 0,168
  → V2 − 0,4·V2 = 0,328 → 0,6·V2 = 0,328 → **V2 = 0,328 ÷ 0,6 = 0,5467**
  (V2 é 1·V2, então 1·V2 − 0,4·V2 = 0,6·V2. No papel, uma igualdade por linha, sem
  encadear "= 0,328 = 0,328 / 0,6".)
- **V4 = 0,5467 + 0,42 = 0,9667** (conferido)
- Conferência: (0,5 × 0,84) + (0,6 × 0,9667) = 0,42 + 0,5800 = **1,0000** ✓
  (no rascunho tinha saído 1,0166: erro na multiplicação 0,6 × 0,9667)

Resumo: V1 = 0,8 · V2 = 0,5467 · V3 = 0,84 · V4 = 0,9667. Passo 2 concluído.

**Passo 3 — vazão (conferido):** dᵢ = Vᵢ × Σ L = Vᵢ × 5 (em cl/h).

| Fila | Conta | d (cl/h) |
|---|---|---|
| 1 | 0,8 × 5 | 4 |
| 2 | 0,5467 × 5 | 2,7335 |
| 3 | 0,84 × 5 | 4,2 |
| 4 | 0,9667 × 5 | 4,8335 |

(Com os V completos daria 2,7333 e 4,8333; diferença de arredondamento, tanto faz.
No papel, escrever d2, d3, d4, não V2, V3, V4.)

**Passo 4 — utilização (conferido):** uᵢ = dᵢ × Sᵢ.

| Fila | Conta | u |
|---|---|---|
| 1 | 4 × 0,1 | 0,4 = 40% |
| 2 | 2,7335 × 0,2 | 0,5467 = 54,67% |
| 3 | 4,2 × 0,15 | 0,63 = 63% |
| 4 | 4,8335 × 0,05 | 0,2417 = 24,17% |

Todas abaixo de 1: rede estável, dá para seguir.

**Passos 5 e 6 — tempo de resposta e população (conferidos):**
wᵢ = Sᵢ / (1 − uᵢ) e nᵢ = uᵢ / (1 − uᵢ).

| Fila | 1 − u | w (h) | n (clientes) |
|---|---|---|---|
| 1 | 0,6 | 0,1 ÷ 0,6 = 0,1667 | 0,4 ÷ 0,6 = 0,6667 |
| 2 | 0,4533 | 0,2 ÷ 0,4533 = 0,4412 | 0,5467 ÷ 0,4533 = 1,2060 |
| 3 | 0,37 | 0,15 ÷ 0,37 = 0,4054 | 0,63 ÷ 0,37 = 1,7027 |
| 4 | 0,7583 | 0,05 ÷ 0,7583 = 0,0659 | 0,2417 ÷ 0,7583 = 0,3187 |

Conferência extra (Lei de Little, n = d × w): fila 2: 2,7335 × 0,4412 = 1,206 ✓.

**Passo 7 — respostas (conferido)**

1. Maior tempo de resposta: comparando w1 = 0,1667, w2 = 0,4412, w3 = 0,4054,
   w4 = 0,0659, a maior é a **fila 2, com 0,4412 h (≈ 26,47 min)**.
2. Menor população média: comparando n1 = 0,6667, n2 = 1,2060, n3 = 1,7027,
   n4 = 0,3187, a menor é a **fila 4, com 0,3187 clientes**.

Falta: passar a limpo à mão e entregar o PDF até 04/11/2026 23:59.

**Revisão do [E4.pdf](E4.pdf) (3 páginas, 04/11)**

- Página 1 (rede fechada com X, frações 0,8 e 0,2, seta 2 → 4 = 1): certa.
- Página 2: valores de V, d e u certos. **Corrigir a conferência**: está
  "0,42 + 0,6 · 0,9667 = 1,0166"; o certo é 0,42 + 0,5800 = 1,0000. Sugestões:
  escrever ΣL = 4 + 1 = 5 cl/h antes do dᵢ = Vᵢ · 5 e anotar que todas as u < 1.
- Página 3: w, n e as duas respostas certas.

Segunda versão (04/11): conferência refeita e "todas u < 1, rede estável"
acrescentado. Ficou um detalhe: "0,42 · 0,5800 = 1,0000" está com sinal de vezes
entre 0,42 e 0,5800; o certo é "+".
