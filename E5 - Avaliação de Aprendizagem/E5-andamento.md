# E5 - Andamento da resolução

Anotações para continuar a E5 em outra máquina. Prazo: **quarta, 11/11/2026, 23:59**
(sala de entrega do Moodle "E5 | Avaliação de Aprendizagem | 691"). O sistema
bloqueia o envio depois das 23h59.

## Regras de entrega

- Resolução **à mão livre**, em papel (ou tablet com caneta, desde que desenhada à
  mão, não digitada nem copiada), digitalizada em **um único PDF**.
- Tem que mostrar o **desenvolvimento** até o resultado; só a resposta, mesmo certa,
  não vale.
- Resolução no formato de LLM, e não no formato usado no material da disciplina,
  não vale.
- Resolver a proposta **sorteada** pelo Moodle (a de outra situação é zerada).

## Enunciado sorteado — situação 3, rede fechada

![Rede sorteada](<M14 - Redes Fechadas de Filas/imagens/00-rede-sorteada-situacao-3.jpg>)

> Assuma a rede de filas de espera acima, com tempos de serviço **S1 = 0,25,
> S2 = 1,5, S3 = 1,25, S4 = 0,5**.
>
> Sendo as populações médias com 19 clientes **n1(19) = 1,7003, n2(19) = 2,9660 e
> n4(19) = 5,7771**, quando tivermos **20 clientes** circulando na rede, qual fila
> estará menos sobrecarregada? Isto é, qual fila terá a **menor utilização**?
>
> Além de indicar a fila, indique numericamente qual é a probabilidade de utilização
> da fila. Para fins de cálculo das taxas de visita, assuma **V1 = 1**. Note que
> n3(19) não foi informado propositalmente, visto que a descoberta deste valor faz
> parte da avaliação da questão.

Leitura do desenho:

```
fila 1 → fila 2 : 0,2
fila 1 → fila 4 : 0,5
fila 1 → fila 3 : 0,3
fila 2 → fila 4 : (sem número na seta)
fila 3 → fila 1 : (sem número na seta)
fila 4 → fila 1 : (sem número na seta)
```

## Critérios de avaliação

| Parte | Pontos |
|---|---|
| Cálculo da população média anterior (n3(19)) | 20 |
| Cálculo da taxa de visita | 10 |
| Cálculo do tempo de resposta | 20 |
| Cálculo da vazão | 20 |
| Cálculo da utilização | 10 |

(O Moodle lista 80 pontos; os outros 20 devem ser da resposta final.)

## Como vamos resolver

Mesmo formato da E4: um passo de cada vez, cada valor calculado à mão e conferido
antes de seguir. No papel, seguir a ordem do exemplo do
[M14-texto.md](<M14 - Redes Fechadas de Filas/M14-texto.md>).

Diferença para a E4: a rede **já é fechada**, então **não tem fila X**. E não
precisa iterar N = 1, 2, ..., 20: o enunciado já dá a população com N = 19, então
basta **uma iteração** (de 19 para 20).

Fórmulas (M14, MVA):

- nᵢ(N) somam N → n3(19) = 19 − n1(19) − n2(19) − n4(19)
- wᵢ(20) = Sᵢ × (1 + nᵢ(19))
- d₀(20) = 20 / Σ (wⱼ(20) × Vⱼ)
- dᵢ(20) = d₀(20) × Vᵢ
- uᵢ = dᵢ(20) × Sᵢ
- (conferência) nᵢ(20) = wᵢ(20) × dᵢ(20); a soma tem que dar ≈ 20

## Roteiro (a preencher conforme for conferido)

- [ ] **Passo 1 — desenho:** copiar a rede e escrever o número nas setas sem número.
- [x] **Passo 2 — taxas de visita:** V1 = 1; uma equação por fila; resolver.
      Conferência: a equação da fila 1 fecha.
- [x] **Passo 3 — população anterior:** n3(19).
- [x] **Passo 4 — tempo de resposta:** w1(20) a w4(20).
- [x] **Passo 5 — vazão:** d₀(20), depois d1(20) a d4(20).
- [x] **Passo 6 — utilização:** u1 a u4 (todas abaixo de 1).
- [x] **Passo 7 — resposta:** menor u (fila e valor). Conferência opcional: n(20).

### Feito até agora

**Passo 1 — desenho (montado, falta passar para o papel)**

Copiar a rede como está. Escrever **1** nas três setas sem número: a fila 2 só tem
uma saída (vai 100% para a 4), e o mesmo vale para a 3 (volta 100% para a 1) e
para a 4 (volta 100% para a 1). Sem fila X.

**Passo 2 — taxas de visita (conferido, 10/11)**

Uma equação por fila: soma de (fração da seta que chega × V de quem manda).

```
V1 = 1                        (dado pelo enunciado)
V2 = 0,2 × V1                 → V2 = 0,2 × 1 = 0,2
V3 = 0,3 × V1                 → V3 = 0,3 × 1 = 0,3
V4 = (0,5 × V1) + (1 × V2)    → V4 = (0,5 × 1) + (1 × 0,2) = 0,7
```

Conferência: V1 = (1 × V3) + (1 × V4) = (1 × 0,3) + (1 × 0,7) = **1** ✓

Resumo: V1 = 1 · V2 = 0,2 · V3 = 0,3 · V4 = 0,7.

**Passo 3 — população anterior (conferido, 10/11)**

Com 19 clientes, a soma das populações dá 19:

```
n1(19) + n2(19) + n3(19) + n4(19) = 19
n3(19) = 19 − 1,7003 − 2,9660 − 5,7771 = 8,5566
```

**n3(19) = 8,5566** ✓

**Passo 4 — tempo de resposta (conferido, 10/11)**

Teorema da Chegada: quem chega com 20 clientes na rede encontra, em média, a
população de quando havia 19. wᵢ(20) = Sᵢ × (1 + nᵢ(19)).

```
w1(20) = S1 × (1 + n1(19)) = 0,25 × (1 + 1,7003) = 0,25 × 2,7003 = 0,6751
w2(20) = S2 × (1 + n2(19)) = 1,5  × (1 + 2,9660) = 1,5  × 3,9660 = 5,9490
w3(20) = S3 × (1 + n3(19)) = 1,25 × (1 + 8,5566) = 1,25 × 9,5566 = 11,9458
w4(20) = S4 × (1 + n4(19)) = 0,5  × (1 + 5,7771) = 0,5  × 6,7771 = 3,3886
```

**Passo 5 — vazão (conferido, 10/11)**

Primeiro a vazão da rede inteira, depois a de cada fila.

```
d0(20) = 20 / ((w1 × V1) + (w2 × V2) + (w3 × V3) + (w4 × V4))
d0(20) = 20 / ((0,6751 × 1) + (5,9490 × 0,2) + (11,9458 × 0,3) + (3,3886 × 0,7))
d0(20) = 20 / (0,6751 + 1,1898 + 3,5837 + 2,3720)
d0(20) = 20 / 7,8206 = 2,5573

d1(20) = d0(20) × V1 = 2,5573 × 1   = 2,5573
d2(20) = d0(20) × V2 = 2,5573 × 0,2 = 0,5115
d3(20) = d0(20) × V3 = 2,5573 × 0,3 = 0,7672
d4(20) = d0(20) × V4 = 2,5573 × 0,7 = 1,7901
```

**Passo 6 — utilização (conferido, 10/11)**

uᵢ = dᵢ(20) × Sᵢ (mesma fórmula da rede aberta). Todas têm que ficar abaixo de 1.

```
u1 = d1(20) × S1 = 2,5573 × 0,25 = 0,6393
u2 = d2(20) × S2 = 0,5115 × 1,5  = 0,7673
u3 = d3(20) × S3 = 0,7672 × 1,25 = 0,9590
u4 = d4(20) × S4 = 1,7901 × 0,5  = 0,8951
```

Todas abaixo de 1. (u2 sem arredondar o d2 dá 0,7672; diferença de arredondamento.)

**Passo 7 — resposta (conferido, 10/11)**

Comparando u1 = 0,6393, u2 = 0,7673, u3 = 0,9590, u4 = 0,8951, a menor é a
**fila 1, com utilização de 0,6393 (63,93%)**. É a fila menos sobrecarregada com
20 clientes na rede.

(No papel, escrever "fila 1", não "fila u1": u1 é a utilização, a fila é a 1.)

Falta: passar a limpo à mão e entregar o PDF até 11/11/2026 23:59.

Conferência opcional, como no exemplo do M14: nᵢ(20) = wᵢ(20) × dᵢ(20); a soma
tem que dar ≈ 20.

**Revisão do [E5.pdf](E5.pdf) (2 páginas, 10/11)**

- Página 1 (desenho com 1 nas setas 2 → 4, 3 → 1, 4 → 1): certa.
- Página 2: todos os valores certos (V, n3(19), w, d0, d, u e resposta fila 1, 63,93%).
- **Corrigir:** no d0, "(11,9458 · 03)" está sem vírgula; o certo é 0,3.
- Ordem de leitura: d0 aparece no quadro de cima antes dos w (que ele usa), e u antes
  dos d. Numerar os quadros na ordem V → n3(19) → w → d0 → dᵢ → u → resposta, ou
  reorganizar.
- Sugestões: escrever n1(19) + n2(19) + n3(19) + n4(19) = 19 antes do n3; no V4,
  substituir V2 por 0,2; na conferência, (1 · V3) + (1 · V4); linha
  20 / (0,6751 + 1,1898 + 3,5837 + 2,3720) antes do 7,8206; anotar "todas u < 1";
  um título por bloco (taxas de visita, população anterior, tempo de resposta, vazão,
  utilização), já que é assim que os critérios pontuam.
