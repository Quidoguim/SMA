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

## Questão 2 — cafeteria Bauducco, M/M/3/4 (não começada)

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
