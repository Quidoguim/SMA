# E7 - Avaliação de Aprendizagem

Material de apoio para a E7, do módulo M16 (Redes de Petri Estocásticas). O enunciado e a conferência
da resolução ficam em [E7-andamento.md](E7-andamento.md).

## Resumo do método (conjunto de atingibilidade)

1. **Estrutura:** grafo bipartido de lugares (círculos), transições (barras) e arcos. Lugar de entrada
   tem arco para a transição; lugar de saída recebe arco da transição.
2. **Marcação:** número de tokens em cada lugar; M0 é a marcação inicial.
3. **Habilitada:** transição pode disparar quando **todos** os lugares de entrada têm pelo menos 1 token.
4. **Disparo:** remove 1 token de cada lugar de entrada e coloca 1 em cada lugar de saída. Se um lugar é
   entrada e saída da mesma transição, o token volta.
5. **Conflito:** com várias habilitadas, escolhe-se uma (não determinístico); a árvore de atingibilidade
   explora todas.
6. **Atingibilidade (RS):** a partir de M0, listar as marcações imediatamente atingíveis; repetir com as
   novas até não aparecer nenhuma. Pode ser feito como árvore ou como tabela de marcações.

Fonte: texto multimodal do M16 (Prof. Rafael Chanin), Moodle PUCRS.
Quiz do M16: 1 pergunta; resposta certa: "Um token é removido de cada lugar de entrada e adicionado a
cada lugar de saída."
