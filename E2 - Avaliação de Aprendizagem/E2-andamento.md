# E2 - Andamento da resolução

Anotações para continuar a E2 em outra máquina. Prazo: **quarta, 21/10/2026, 23:59**
(as duas salas de entrega do Moodle, código 691). A entrega é à mão, digitalizada,
**um PDF por questão**, cada um na sua sala.

## Como estamos resolvendo

Um passo de cada vez: cada valor é calculado à mão (com calculadora) e conferido
antes de seguir para o próximo. No papel, cada linha mostra a fórmula, a conta e o
resultado, no formato dos exemplos do M10/M11 (diagrama de estados, tabela dos πᵢ,
soma, complemento).

Regras de precisão (critério da nota máxima):

- decimal com **6 casas** e a porcentagem do lado, ex.: `0,146484 = 14,65%`;
- **arredondar**, não cortar (dígito seguinte 5 ou mais sobe o anterior);
- na calculadora, multiplicar sempre o valor **completo** da tela, sem redigitar o
  arredondado, para o erro não acumular até o π₁₀.

---

## Questão 1 — cafeteria Bauducco, M/M/1/∞ (concluída)

> 1 funcionário, clientes não são perdidos, chegam em média **15 clientes/h** e são
> atendidos em média **24 clientes/h**, chegadas e atendimentos exponenciais.
>
> 1. Probabilidade de chegar na fila e encontrá-la com **mais de 10 clientes**,
>    passo a passo. **[30 pts]**
> 2. **Tempo de serviço máximo (em minutos)** para a fila continuar respeitando a
>    hipótese da estacionariedade. Demonstrar e dissertar. **[20 pts]**

### Ideia (em palavras simples)

- πᵢ = fração do tempo em que a fila tem i clientes; todas somam 100%.
- ρ = λ/μ = quão ocupado o atendente fica.
- π₀ = 1 − ρ (fila vazia); πᵢ = πᵢ₋₁ · ρ (cada cliente a mais é menos provável, sempre
  na mesma proporção ρ — "escadinha").
- "Mais de 10" são infinitos estados (11, 12, …): soma de 0 a 10 e tira de 1
  (complemento).

### Feito até agora (conferido)

**Passo 1 — modelo e ρ**

> M/M/1/∞ (chegada e atendimento exponenciais, 1 servidor, capacidade infinita)
> ρ = λ/μ = 15/24 = 0,625 < 1 → sistema estável (existe solução estacionária)

Desenhar o diagrama de estados igual a `M10 .../imagens/06-mm1-infinito-diagrama.png`:
estados 0, 1, 2, …, 10, 11, … com λ = 15 nas setas para a direita e μ = 24 para a esquerda.

**Passos 2 a 4 — probabilidades**

| Estado | Cálculo | πᵢ |
|---|---|---|
| π₀ | 1 − 0,625 | 0,375000 = 37,50% |
| π₁ | 0,375000 · 0,625 | 0,234375 = 23,44% |
| π₂ | 0,234375 · 0,625 | 0,146484 = 14,65% |
| π₃ | 0,146484 · 0,625 | 0,091553 = 9,16% |
| π₄ | 0,091553 · 0,625 | 0,057220 = 5,72% |
| π₅ | 0,057220 · 0,625 | 0,035763 = 3,58% |
| π₆ | 0,035763 · 0,625 | 0,022352 = 2,24% |
| π₇ | 0,022352 · 0,625 | 0,013970 = 1,40% |
| π₈ | 0,013970 · 0,625 | 0,008731 = 0,87% |
| π₉ | 0,008731 · 0,625 | 0,005457 = 0,55% |
| π₁₀ | 0,005457 · 0,625 | 0,003411 = 0,34% |

(Vários valores tinham sido cortados em vez de arredondados — 14,64%, 9,15%, 3,57%,
2,23%, 1,39%, 0,54%, 0,33%; os valores acima já estão arredondados.)

**Passos 5 a 7 — soma, complemento e conferência (Pergunta 1 concluída)**

> P(N ≤ 10) = π₀ + π₁ + … + π₁₀ = 0,994316 = 99,43%
> P(N > 10) = 1 − P(N ≤ 10) = 1 − 0,994316 = **0,005684 = 0,5684%**
> Conferência pela forma fechada πᵢ = π₀ · ρⁱ: P(N > 10) = ρ¹¹ = 0,625¹¹ = 0,005684 ✓

Interpretação: um cliente que chega tem cerca de 0,57% de chance (≈ 1 em 176) de
encontrar mais de 10 clientes na fila — raro, porque o funcionário dá conta (ρ = 0,625).

Obs.: o "intervalo de 1 hora" do enunciado só define a unidade das taxas; a
probabilidade pedida é a estacionária, não precisa multiplicar por tempo.

### Pergunta 2 — concluída

Tabela de teste (λ = 15 fixo; μ = 60 ÷ tempo; ρ = 15 ÷ μ):

| Tempo por cliente | μ (clientes/h) | ρ | Estável (ρ < 1)? |
|---|---|---|---|
| 2,5 min | 24 | 0,625 | sim |
| 3 min | 20 | 0,75 | sim |
| 3,5 min | 17,142857 | 0,875 | sim |
| 4 min | 15 | 1 | não (ρ = 1 também é instável) |
| 5 min | 12 | 1,25 | não |

Demonstração:

> Hipótese da estacionariedade: ρ = λ/μ < 1
> λ = 15 clientes/h ⇒ 15/μ < 1 ⇒ μ > 15 clientes/h
> Tempo de serviço = 1/μ ⇒ 1/μ < 1/15 h = 60/15 min = 4 min
> Para ρ = 1 (μ = 15, tempo = 4 min) o sistema é instável, então o limite não é incluído.
> **Resposta:** o tempo de serviço precisa ser **menor que 4 minutos** por cliente.

Dissertação (texto próprio, revisado):

> Sempre que ρ < 1, o atendente atende mais rápido do que os clientes chegam, e a fila
> se mantém estável. Se o funcionário levar 4 minutos ou mais por cliente, ρ ≥ 1 e a
> fila vai aumentar mais do que ele dá conta. Hoje ele leva 2,5 min por cliente, então
> tem 1,5 min de folga até o seu limite.

### Roteiro usado na Pergunta 2

Roteiro do raciocínio (dissertativo, o racional vale nota):

1. Hipótese da estacionariedade: só existe solução estacionária com ρ < 1
   (`M10 .../imagens/04-intensidade-trafego.png`).
2. Transformar em condição sobre μ, com λ = 15 fixo: ρ = λ/μ < 1 ⇒ μ > λ.
3. Converter taxa em tempo: tempo de serviço = 1/μ (em horas) × 60 = minutos.
4. Discutir o limite: com o tempo exatamente igual ao limite, ρ = 1, e o sistema
   também é instável. A resposta é "**menor que** X minutos".
5. Fechar com a interpretação: o funcionário precisa atender, em média, mais rápido do
   que os clientes chegam.

### Exemplo de referência (outros números: λ = 12, μ = 20)

Mesmo roteiro aplicado em outro caso, para comparar o formato:

- ρ = 12/20 = 0,6 < 1 → estável.
- π₀ = 0,400000; π₁ = 0,240000; π₂ = 0,144000; π₃ = 0,086400; π₄ = 0,051840;
  π₅ = 0,031104; π₆ = 0,018662; π₇ = 0,011197; π₈ = 0,006718; π₉ = 0,004031;
  π₁₀ = 0,002419.
- P(N ≤ 10) = 0,996372 → P(N > 10) = 1 − 0,996372 = 0,003628 ≈ 0,3628%
  (confere com 0,6¹¹ ≈ 0,003628).
- Pergunta 2: μ > 12 ⇒ 1/μ < 1/12 h = 5 min → tempo de serviço **menor que 5 minutos**.

---

## Questão 2 — cafeteria Bauducco, M/M/3/4 (concluída)

> 3 funcionários, capacidade 4 clientes (quem chega com a fila cheia é perdido),
> chegam em média **15 clientes/h** e são atendidos em média **10 clientes/h**,
> exponenciais.
>
> 1. **Perda de clientes por hora**, passo a passo, 4 casas ou mais. **[20 pts]**
> 2. **Tempo de resposta em minutos**, mostrando também o cálculo de **N** e **D**.
>    Resposta fora de minutos vale nota parcial. **[30 pts]**

Material de base: método dos pesos do M10 (Wᵢ = Wᵢ₋₁ · λ / (min(i, C) · μ),
normalização πᵢ = Wᵢ / ΣW) e índices do M11 (perda = λ · π_K, N, D, W = N/D). O
exemplo M/M/3/3 do servidor com 3 threads no `M11-texto.md` é o mais parecido.

### Feito até agora (conferido)

**Passo 1 — modelo, estados e taxas**

> M/M/3/4: chegada e atendimento exponenciais, C = 3 funcionários, capacidade K = 4
> (quem chega com 4 clientes no sistema é perdido). λ = 15 clientes/h, μ = 10 clientes/h
> por funcionário. Estados 0 a 4.

Diagrama: estados 0, 1, 2, 3, 4; λ = 15 em todas as setas para a direita; para a
esquerda, a taxa de saída do estado i é min(i, C) · μ (número de funcionários ocupados
× taxa de cada um — multiplica por μ uma vez só):

| Estado i | min(i, 3) | Taxa de saída μᵢ = min(i, 3) · 10 |
|---|---|---|
| 1 | 1 | 10 |
| 2 | 2 | 20 |
| 3 | 3 | 30 |
| 4 | 3 | 30 |

**Passo 2 — pesos**

| Peso | Cálculo | Valor |
|---|---|---|
| W₀ | — | 1 |
| W₁ | 1 · 15/10 | 1,5 |
| W₂ | 1,5 · 15/20 | 1,125 |
| W₃ | 1,125 · 15/30 | 0,5625 |
| W₄ | 0,5625 · 15/30 | 0,28125 |

> ΣW = 1 + 1,5 + 1,125 + 0,5625 + 0,28125 = 4,46875

(W₄ e ΣW tinham sido cortados em 0,2812 e 4,4687; os valores acima são exatos.)

**Passo 3 — probabilidades (normalização)**

| Estado | Cálculo | πᵢ |
|---|---|---|
| π₀ | 1 / 4,46875 | 0,223776 |
| π₁ | 1,5 / 4,46875 | 0,335664 |
| π₂ | 1,125 / 4,46875 | 0,251748 |
| π₃ | 0,5625 / 4,46875 | 0,125874 |
| π₄ | 0,28125 / 4,46875 | 0,062937 |

> Soma = 0,999999 ≈ 1 (a diferença de 0,000001 é só o arredondamento da 6ª casa)

**Passo 4 — perda por hora (Pergunta 1 concluída)**

> Cliente é perdido quando chega com a fila cheia (estado 4 = K).
> Perda = λ · π₄ = 15 · 0,062937 = **0,944055 clientes/h** (≈ 0,9441)

Interpretação: perde-se, em média, quase 1 cliente por hora — 6,29% de quem chega.

**Passo 5 — população média**

> N = Σ πⱼ · j = (0,223776 · 0) + (0,335664 · 1) + (0,251748 · 2) + (0,125874 · 3) + (0,062937 · 4)
> N = 0 + 0,335664 + 0,503496 + 0,377622 + 0,251748 = **1,468530 clientes**

**Passo 6 — vazão**

> D = Σ πⱼ · μⱼ = (0,223776 · 0) + (0,335664 · 10) + (0,251748 · 20) + (0,125874 · 30) + (0,062937 · 30)
> D = 0 + 3,356640 + 5,034960 + 3,776220 + 1,888110 = **14,055930 clientes/h**
> Conferência: λ − perda = 15 − 0,944055 = 14,055945 ≈ D ✓ (diferença só de arredondamento)

**Passo 7 — tempo de resposta (Pergunta 2 concluída)**

> W = N / D = 1,468530 / 14,055930 = 0,104478 h
> W = 0,104478 · 60 = **6,268657 minutos** (≈ 6 min 16 s)

Interpretação: cada cliente fica, em média, 6,27 min na cafeteria. Só o atendimento
leva 1/μ = 60/10 = 6 min, então a espera média na fila é de uns 0,27 min (≈ 16 s).

## Checklist da entrega

- [ ] Questão 1 passada a limpo à mão (modelo, diagrama, ρ, tabela π₀–π₁₀, soma,
      complemento, conferência ρ¹¹; Pergunta 2 com tabela, demonstração e texto).
- [ ] Questão 2 passada a limpo à mão (modelo, diagrama com taxas, pesos, ΣW,
      probabilidades e validação, perda, N, D com conferência, W em horas e minutos).
- [ ] Um PDF por questão, enviado na sala certa (Questão 1 / Questão 2, código 691),
      até 21/10/2026 23:59.
