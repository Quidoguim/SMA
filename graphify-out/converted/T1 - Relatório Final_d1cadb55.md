<!-- converted from T1 - Relatório Final.docx -->

Disciplina: SIMULAÇÃO E MÉTODOS ANALÍTICOS
Unidade de Aprendizagem: UA2 | FUNDAMENTOS DE SIMULAÇÃO POR COMPUTADOR
Módulo de Aprendizagem: M8 | DESENVOLVIMENTO DE SIMULADOR PARA REDE DE FILAS
Estudantes: Guilherme Guimarães Santos e Jully Anne Seyffert da Silva Jara



Entrega | Simulador para Rede de Filas

Registre neste espaço sua resposta! 
| Link para o código fonte do grupo: |
| --- |
| https://github.com/Quidoguim/SMA |
| Resultado da Fila 1: G/G/1, chegadas entre 2..4, atendimento entre 1..2: |
| Resultados da simulação — Fila 1 (G/G/1, capacidade ilimitada) Números pseudoaleatórios utilizados na simulação da rede: 100.000 Tempo global da simulação (rede completa): 50.750,10 Clientes perdidos (bloqueados) na Fila 1: 0 Distribuição de probabilidades por estado (tempo acumulado / probabilidade): Estado 0: 20.352,45 (40,1033%) Estado 1: 26.619,82 (52,4527%) Estado 2: 3.620,27 (7,1335%) Estado 3: 155,09 (0,3056%) Estado 4: 2,48 (0,0049%) Análise: Com chegadas externas entre 2 e 4 (média 3) e atendimento entre 1 e 2 (média 1,5) em 1 servidor, a carga oferecida é ρ ≈ 1,5/3 = 0,5 — sistema estável, e como não há limite de capacidade não há perdas. A fila passa a maior parte do tempo (92,55%) vazia ou com 1 cliente; estados acima de 2 clientes são raros (0,31%). |
| Resultado da Fila 2: G/G/2/5, atendimento entre 4..6: |
| Resultados da simulação — Fila 2 (G/G/2/5), rede com a Fila 1 e a Fila 3 Números pseudoaleatórios utilizados na simulação da rede: 100.000 Tempo global da simulação (rede completa): 50.750,10 Clientes perdidos (bloqueados) na Fila 2: 6 Distribuição de probabilidades por estado (tempo acumulado / probabilidade): Estado 0: 12.280,10 (24,1972%) Estado 1: 20.984,81 (41,3493%) Estado 2: 13.125,58 (25,8632%) Estado 3: 3.746,09 (7,3814%) Estado 4: 544,84 (1,0736%) Estado 5: 68,68 (0,1353%) Análise: A Fila 2 recebe 20% do que sai da Fila 1 e ainda realimenta a própria rede: 30% do que atende volta pra Fila 1 e 50% vai pra Fila 3, só 20% sai do sistema. Esse retorno constante mantém a fila naturalmente ocupada (75,5% do tempo com 2 ou mais clientes), mas com capacidade K=5 as perdas ficam baixas (6 em 100.000 aleatórios). |


| Resultado da Fila 3: G/G/2/10, atendimento entre 5..15: |
| --- |
| Resultados da simulação — Fila 3 (G/G/2/10), rede com a Fila 1 e a Fila 2 Números pseudoaleatórios utilizados na simulação da rede: 100.000 Tempo global da simulação (rede completa): 50.750,10 Clientes perdidos (bloqueados) na Fila 3: 11.583 Distribuição de probabilidades por estado (tempo acumulado / probabilidade): Estado 0: 3,51 (0,0069%) Estado 1: 2,79 (0,0055%) Estado 2: 3,92 (0,0077%) Estado 3: 5,45 (0,0107%) Estado 4: 3,09 (0,0061%) Estado 5: 3,99 (0,0079%) Estado 6: 7,72 (0,0152%) Estado 7: 64,69 (0,1275%) Estado 8: 2.905,58 (5,7253%) Estado 9: 15.874,26 (31,2793%) Estado 10: 31.875,11 (62,8080%) Análise: A Fila 3 recebe 80% do que sai da Fila 1 mais 70% do que sai da Fila 2 (que por sua vez recebe 50% de volta da própria Fila 3) — esse ciclo Fila 2 ↔ Fila 3 amplifica bastante o tráfego efetivo sobre a Fila 3. Resultado: a fila passa 94,1% do tempo com 8 clientes ou mais (praticamente cheia, K=10) e tem 11.583 perdas em 100.000 aleatórios, de longe a fila mais congestionada da rede. |
| Tempo total de simulação: |
| 50.750,10 (100.000 números pseudoaleatórios consumidos no total, contados em toda a rede) |


