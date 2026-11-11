<!-- converted from M6 - Desenvolvimento de Simulador para Filas em Tandem.docx -->

Disciplina: SIMULAÇÃO E MÉTODOS ANALÍTICOS
Unidade de Aprendizagem: UA2 | FUNDAMENTOS DE SIMULAÇÃO POR COMPUTADOR
Módulo de Aprendizagem: M6 | SIMULAÇÃO DE FILAS EM TANDEM
Estudantes: Guilherme Guimarães Santos e Jully Anne Seyffert da Silva Jara



Entrega | Filas em Tandem

Registre neste espaço sua resposta! 
| Link para o código fonte do grupo: |
| --- |
| https://github.com/Quidoguim/SMA |
| G/G/2/3, chegadas entre 1..5, atendimento entre 4..5: |
| Resultados da simulação — Fila 1 (G/G/2/3), rede em tandem com a Fila 2 Números pseudoaleatórios utilizados na simulação da rede: 100.000 Tempo global da simulação (rede completa): 100.650,77 Clientes perdidos (bloqueados) na Fila 1: 395 Distribuição de probabilidades por estado (tempo acumulado / probabilidade): Estado 0: 1.119,77 (1,1125%) Estado 1: 49.594,92 (49,2743%) Estado 2: 43.530,68 (43,2492%) Estado 3: 6.405,40 (6,3640%) Análise: Com chegadas externas entre 1 e 5 (média 3) e atendimento entre 4 e 5 (média 4,5) em 2 servidores, a carga oferecida é ρ ≈ 3/(2×4,5) ≈ 0,33, ou seja, o sistema é estável. Ainda assim, como a capacidade é pequena (K = 3), a fila passa a maior parte do tempo com 1 ou 2 clientes (92,52%) e chega a ficar cheia em 6,36% do tempo, gerando 395 perdas por falta de vaga — essas perdas não chegam a alimentar a Fila 2. |
| G/G/1/5, atendimento entre 1..3: |
| Resultados da simulação — Fila 2 (G/G/1/5), alimentada 100% pela saída da Fila 1 Números pseudoaleatórios utilizados na simulação da rede: 100.000 (mesma execução da Fila 1, ver acima) Tempo global da simulação (rede completa): 100.650,77 Clientes perdidos (bloqueados) na Fila 2: 0 Distribuição de probabilidades por estado (tempo acumulado / probabilidade): Estado 0: 33.990,49 (33,7707%) Estado 1: 60.236,85 (59,8474%) Estado 2: 6.413,65 (6,3722%) Estado 3: 9,79 (0,0097%) Estado 4: 0,00 (0,0000%) Estado 5: 0,00 (0,0000%) Análise: A Fila 2 não tem chegada externa própria: seus clientes são exatamente os que saem atendidos da Fila 1. Com atendimento rápido (média 2, entre 1 e 3) e um único servidor, ela dá conta tranquilamente do fluxo recebido — fica vazia ou com 1 cliente em 93,62% do tempo, quase não acumula fila (6,37% com 2 clientes e apenas 0,01% com 3) e não perde nenhum cliente por falta de capacidade (K = 5). |
