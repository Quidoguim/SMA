# E7 - Andamento da resolução

**Status: entregue em 25/11/2026** (resolução manuscrita em `E7.pdf`).

Prazo: **hoje, 25/11/2026, 23:59** (sala de entrega do Moodle "E7 | Avaliação de Aprendizagem | 691";
na leitura das ~08h15 faltavam 15h45). O sistema bloqueia o envio depois das 23h59.

## Regras de entrega

- Resolução **à mão livre**, em papel (ou tablet com caneta, desenhada à mão), digitalizada em
  **um único PDF**, enviado no card "E7 | Avaliação de Aprendizagem".
- Tem que mostrar o **desenvolvimento**; só a resposta não vale.
- Resolução no formato de LLM, e não no formato usado no material da disciplina, não vale.
- A proposta tem que ser a sorteada pelo Moodle (só havia esta; as 3 situações citadas no texto
  não aparecem, só o modelo SPN abaixo).

## Enunciado

> Dado o modelo SPN a seguir, onde a marcação inicial é igual a **M0 (0, 1, 1, 1, 0, 0)**, mostre
> todas as marcações globais atingíveis a partir desta marcação inicial.

Critérios: todas as marcações atingíveis **[60 pts]**; apresentação correta de todas as
transições **[20 pts]**. (Os 20 restantes devem ser da resposta final / organização.)

Imagem da rede: `https://moodle.pucrs.br/pluginfile.php/5979033/mod_label/intro/Prancheta%2045_1.png`
(precisa estar logado no Moodle).

## Leitura do desenho

Ordem da marcação: **(P1, P2, P3, P4, P5, P6)**. Tokens iniciais em P2, P3 e P4.

| Transição | Entradas | Saídas |
|---|---|---|
| t1 | P1 | P2 |
| t2 | P1 | P4 |
| t3 | P2, P3 | P5, **P3** (P3 é devolvido) |
| t4 | P4, P3 | P6, **P3** (P3 é devolvido) |
| t5 | P5 | P1 |
| t6 | P6 | P1 |

Conferir no desenho: t3 e t4 têm duas setas com P3 (uma de ida e uma de volta). P3 funciona como
um recurso compartilhado: está sempre com 1 token e é disputado por t3 e t4.

## Conferência (feita pelo Claude, para o usuário comparar com a resolução dele)

Regra do M16: transição habilitada se **todos** os lugares de entrada têm pelo menos 1 token;
disparar remove 1 token de cada entrada e coloca 1 em cada saída.

15 marcações atingíveis:

| Marcação | (P1,P2,P3,P4,P5,P6) | Habilitadas → destino |
|---|---|---|
| M0 | (0,1,1,1,0,0) | t3 → M1; t4 → M2 |
| M1 | (0,0,1,1,1,0) | t4 → M3; t5 → M4 |
| M2 | (0,1,1,0,0,1) | t3 → M3; t6 → M5 |
| M3 | (0,0,1,0,1,1) | t5 → M6; t6 → M7 |
| M4 | (1,0,1,1,0,0) | t1 → M0; t2 → M8; t4 → M6 |
| M5 | (1,1,1,0,0,0) | t1 → M9; t2 → M0; t3 → M7 |
| M6 | (1,0,1,0,0,1) | t1 → M2; t2 → M10; t6 → M11 |
| M7 | (1,0,1,0,1,0) | t1 → M12; t2 → M1; t5 → M11 |
| M8 | (0,0,1,2,0,0) | t4 → M10 |
| M9 | (0,2,1,0,0,0) | t3 → M12 |
| M10 | (0,0,1,1,0,1) | t4 → M13; t6 → M4 |
| M11 | (2,0,1,0,0,0) | t1 → M5; t2 → M4 |
| M12 | (0,1,1,0,1,0) | t3 → M14; t5 → M5 |
| M13 | (0,0,1,0,0,2) | t6 → M6 |
| M14 | (0,0,1,0,2,0) | t5 → M7 |

Verificações: P3 tem sempre 1 token; os outros lugares somam sempre 2 tokens; não há marcação
sem transição habilitada (sem deadlock); todas as 15 voltam a M0 por algum caminho.

## Como montar no papel

Seguir o formato do texto multimodal do M16: (1) lista de lugares e transições com entradas/saídas,
(2) M0, (3) tabela ou árvore de atingibilidade, marcação por marcação, dizendo qual transição
dispara e a marcação resultante; marcação já vista é só ligada à anterior, (4) conjunto final RS
com as 15 marcações.
