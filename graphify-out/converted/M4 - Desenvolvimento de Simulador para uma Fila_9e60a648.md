<!-- converted from M4 - Desenvolvimento de Simulador para uma Fila.docx -->

Disciplina: SIMULAÇÃO E MÉTODOS ANALÍTICOS
Unidade de Aprendizagem: UA2 | FUNDAMENTOS DE SIMULAÇÃO POR COMPUTADOR
Módulo de Aprendizagem: M4 | DESENVOLVIMENTO DE SIMULADOR PARA UMA FILA
Estudantes: Guilherme Guimarães Santos e Jully Anne Seyffert da Silva Jara



Entrega | Fila Simples

Registre neste espaço sua resposta! 
| Link para o código fonte do grupo: |
| --- |
| https://github.com/Quidoguim/SMA |
| G/G/1/5, chegadas entre 2...5, atendimento entre 3...5: |
| Resultados da simulação — G/G/1/5 Números pseudoaleatórios utilizados: 100.000 Tempo global da simulação: 186.922,01 Clientes perdidos (bloqueados): 6.528 Distribuição de probabilidades por estado (tempo acumulado / probabilidade): Estado 0: 3,00 (0,0016%) Estado 1: 36,28 (0,0194%) Estado 2: 245,45 (0,1313%) Estado 3: 8.347,13 (4,4656%) Estado 4: 98.539,02 (52,7166%) Estado 5: 79.751,13 (42,6655%) Análise: O tempo médio entre chegadas é 3,5 (intervalo [2,5]) e o tempo médio de atendimento é 4,0 (intervalo [3,5]). Como o atendimento é, em média, mais lento que as chegadas, ρ ≈ 4,0/3,5 ≈ 1,143 > 1, ou seja, o sistema é instável/saturado: ele passa cerca de 95,4% do tempo de simulação nos estados 4 e 5 (fila cheia ou quase cheia), o que resultou em 6.528 perdas de clientes por falta de vaga no sistema (K = 5). |
| G/G/2/5, chegadas entre 2...5, atendimento entre 3…5: |
| Resultados da simulação — G/G/2/5 Números pseudoaleatórios utilizados: 100.000 Tempo global da simulação: 175.234,14 Clientes perdidos (bloqueados): 0 Distribuição de probabilidades por estado (tempo acumulado / probabilidade): Estado 0: 11.106,09 (6,3379%) Estado 1: 128.103,58 (73,1042%) Estado 2: 35.911,44 (20,4934%) Estado 3: 113,03 (0,0645%) Estado 4: 0,00 (0,0000%) Estado 5: 0,00 (0,0000%) Análise: Com dois servidores, ρ ≈ 4,0/(2×3,5) ≈ 0,571 < 1, portanto o sistema é estável. Ele fica concentrado nos estados 0, 1 e 2 (praticamente 100% do tempo de simulação), com uma ocorrência residual do estado 3 (0,06%) e nenhuma passagem pelos estados 4 e 5. Não houve nenhuma perda de cliente. |
