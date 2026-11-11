# Graph Report - SMA  (2026-11-11)

## Corpus Check
- 30 files · ~462,035 words
- Verdict: corpus is large enough that graph structure adds value.

## Summary
- 406 nodes · 840 edges · 8 communities
- Extraction: 85% EXTRACTED · 14% INFERRED · 1% AMBIGUOUS · INFERRED: 118 edges (avg confidence: 0.85)
- Token cost: 490,711 input · 0 output

## Community Hubs (Navigation)
- Redes de Filas e Índices (M11/M13/M14)
- Simuladores M4/M6/T1 e Relatórios
- Cadeias de Markov (M12/E3)
- T2 Análise e Planilha
- Teoria Nascimento e Morte (M10)
- T2 Gargalo e Gráficos
- E2 Resolução Cafeteria
- Gerador MCL e Simulador de Rede

## God Nodes (most connected - your core abstractions)
1. `Probabilidade de estado π` - 27 edges
2. `Taxas de visita (Vi)` - 19 edges
3. `Tempo de resposta` - 18 edges
4. `Mean-Value Analysis (MVA)` - 18 edges
5. `M12 — Cadeias de Markov (texto)` - 17 edges
6. `Utilização` - 17 edges
7. `Vazão` - 17 edges
8. `Cadeias de Markov` - 16 edges
9. `Fila M/M/C/K` - 16 edges
10. `População média` - 15 edges

## Surprising Connections (you probably didn't know these)
- `M6 - Desenvolvimento de Simulador para Filas em Tandem (PDF)` --semantically_similar_to--> `M6 Entrega Filas em Tandem (convertido)`  [INFERRED] [semantically similar]
  M6 - Desenvolvimento de Simulador para Filas em Tandem/M6 - Desenvolvimento de Simulador para Filas em Tandem.pdf → graphify-out/converted/M6 - Desenvolvimento de Simulador para Filas em Tandem_6469c9e5.md
- `T1 - Relatorio Final (PDF)` --semantically_similar_to--> `T1 Relatorio Final - Simulador para Rede de Filas (convertido)`  [INFERRED] [semantically similar]
  T1 - Simulador para Rede de Filas/T1 - Relatório Final.pdf → graphify-out/converted/T1 - Relatório Final_d1cadb55.md
- `Rede fechada de filas` --semantically_similar_to--> `Fila M/M/C/K`  [INFERRED] [semantically similar]
  E4 - Avaliação de Aprendizagem/M13 - Redes Abertas de Filas/M13-texto.md → E2 - Avaliação de Aprendizagem/M10 - Processo de Nascimento e Morte/imagens/12-solucao-mmck.png
- `M4 - Desenvolvimento de Simulador para uma Fila (PDF)` --semantically_similar_to--> `M4 Entrega Fila Simples (convertido)`  [INFERRED] [semantically similar]
  M4 - Desenvolvimento de Simulador para uma Fila/M4 - Desenvolvimento de Simulador para uma Fila.pdf → graphify-out/converted/M4 - Desenvolvimento de Simulador para uma Fila_9e60a648.md
- `Método dos pesos (M/M/C/K)` --semantically_similar_to--> `Normalização (Σπ = 1)`  [INFERRED] [semantically similar]
  E2 - Avaliação de Aprendizagem/LEIA-ME.md → E3 - Avaliação de Aprendizagem/M12 - Cadeias de Markov/M12-texto.md

## Import Cycles
- None detected.

## Hyperedges (group relationships)
- **lambda e mu definem rho** — concept_taxa_nascimento_lambda, concept_taxa_morte_mu, concept_intensidade_trafego [EXTRACTED 1.00]
- **Pipeline de resolução CTMC: matriz → Q → πQ=0 → normalização** — concept_matriz_transicao, concept_gerador_infinitesimal_q, concept_equacao_pi_q_zero, e3___avalia__o_de_aprendizagem_valor_arbitrario, concept_normalizacao_soma_pi [EXTRACTED 1.00]
- **Análise M/M/C/K: pesos, probabilidades e índices** — e2___avalia__o_de_aprendizagem_metodo_dos_pesos, concept_probabilidade_estado_pi, e2___avalia__o_de_aprendizagem_indices_desempenho, concept_fila_mmck [EXTRACTED 1.00]
- **Quatro índices de desempenho calculados a partir de π_j** — e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_imagens_04_formulas_indices_formula_n, e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_imagens_04_formulas_indices_formula_d, e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_imagens_04_formulas_indices_formula_u, e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_imagens_04_formulas_indices_formula_w, concept_probabilidade_estado_pi [EXTRACTED 1.00]
- **Exemplo do laboratório: M/M/3/3 + estado OFF + matriz de transição** — e3___avalia__o_de_aprendizagem_m12___cadeias_de_markov_imagens_03_laboratorio_mm33, e3___avalia__o_de_aprendizagem_m12___cadeias_de_markov_imagens_04_laboratorio_falta_de_luz, e3___avalia__o_de_aprendizagem_m12___cadeias_de_markov_imagens_07_matriz_transicao [EXTRACTED 1.00]
- **Pipeline do estado estacionario: Q simbolico -> Q numerico -> pi Q = 0 -> sistema -> resolucao -> normalizacao** — e3___avalia__o_de_aprendizagem_m12___cadeias_de_markov_imagens_08_gerador_infinitesimal_simbolico_q_simbolico, e3___avalia__o_de_aprendizagem_m12___cadeias_de_markov_imagens_09_gerador_infinitesimal_numerico_q_numerico, e3___avalia__o_de_aprendizagem_m12___cadeias_de_markov_imagens_10_vetor_vezes_q_produto_p_q, e3___avalia__o_de_aprendizagem_m12___cadeias_de_markov_imagens_11_sistema_equacoes_sistema, e3___avalia__o_de_aprendizagem_m12___cadeias_de_markov_imagens_12_resolucao_sistema_resolucao, e3___avalia__o_de_aprendizagem_m12___cadeias_de_markov_imagens_13_normalizacao_probabilidades_finais [EXTRACTED 1.00]
- **Solução estacionária de CTMC: Q, πQ=0 e Σπ=1** — concept_gerador_infinitesimal_q, concept_equacao_pi_q_zero, concept_normalizacao_soma_pi, concept_probabilidade_estado_pi [EXTRACTED 1.00]
- **Método dos pesos para M/M/C/K** — e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_imagens_12_solucao_mmck_peso_wi, e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_imagens_14_formula_pesos_mmck_min_i_c, e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_imagens_12_solucao_mmck_normalizacao, concept_probabilidade_estado_pi, concept_fila_mmck [EXTRACTED 1.00]
- **Derivacao da distribuicao estacionaria M/M/1** — concept_probabilidade_estado_pi, e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_imagens_07_interativo_mm1_3_pi0, e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_imagens_07_interativo_mm1_4_demonstracao, concept_serie_geometrica [EXTRACTED 1.00]
- **Pipeline de solução M/M/C/K: pesos → normalização → índices** — e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_m10_texto_metodo_dos_pesos, e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_m11_texto_perda_de_clientes, e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_m11_texto_populacao_media_n, e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_m11_texto_vazao_d, e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_m11_texto_tempo_de_resposta_w [EXTRACTED 1.00]
- **Evolucao do simulador M4 -> M6 -> T1 (mesmo motor de eventos e gerador MCL)** — m4_desenvolvimento_de_simulador_para_uma_fila_simulador_fila, m6_desenvolvimento_de_simulador_para_filas_em_tandem_simulador_rede_filas, t1_simulador_para_rede_de_filas_simulador_rede, m6___desenvolvimento_de_simulador_para_filas_em_tandem_leia_me_gerador_mcl, m6___desenvolvimento_de_simulador_para_filas_em_tandem_leia_me_criterio_parada_aleatorios [EXTRACTED 1.00]
- **Estrategia de validacao do T1 (regressao exata + comparacao estatistica com simulator.jar)** — t1___simulador_para_rede_de_filas_leia_me_regressao_m4_m6, t1___simulador_para_rede_de_filas_leia_me_validacao_estatistica, t1___simulador_para_rede_de_filas_simulator_jar, t1___simulador_para_rede_de_filas_modelo_exemplo_m3, t1___simulador_para_rede_de_filas_modelo_validacao [EXTRACTED 1.00]
- **T2 help desk queueing network Q1 -> Q2 -> Q3 with feedback** — concept_t2_fila_q1_triagem, concept_t2_fila_q2_especialista, concept_t2_fila_q3_desenvolvimento [EXTRACTED 1.00]
- **Conferência dos resultados por três caminhos (testes M9, simulator.jar, equações de tráfego)** — t2_análise_por_simulação_de_um_help_desk_de_ti_testes_indices, t2_análise_por_simulação_de_um_help_desk_de_ti_conferencia_jar, t2_análise_por_simulação_de_um_help_desk_de_ti_equacoes_trafego, t2___an_lise_por_simula__o_de_um_help_desk_de_ti_leia_me_simulator_jar [EXTRACTED 1.00]
- **Resolução da Questão 2 da E2** — e2___avalia__o_de_aprendizagem_e2_andamento_questao_2_cafeteria_mm34, e2___avalia__o_de_aprendizagem_e2_andamento_perda_por_hora_q2, e2___avalia__o_de_aprendizagem_e2_andamento_n_e_d_q2, e2___avalia__o_de_aprendizagem_e2_andamento_tempo_resposta_q2, e2___avalia__o_de_aprendizagem_e2___q2_resolucao_manuscrita_q2 [INFERRED 0.85]
- **Exemplo resolvido M/M/1/4** — e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_imagens_11_mm14_diagrama_diagrama_mm14, e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_imagens_15_exemplo_mm14_1_exemplo_pesos, e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_imagens_15_exemplo_mm14_2_exemplo_probabilidades, e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_imagens_11_mm14_diagrama_fila_mm14 [INFERRED 0.85]
- **Exemplo resolvido M/M/2/4** — e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_imagens_16_exemplo_mm24_1_exemplo_pesos, e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_imagens_16_exemplo_mm24_2_exemplo_probabilidades, e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_imagens_16_exemplo_mm24_1_fila_mm24, e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_imagens_14_formula_pesos_mmck_formula_pesos_mmck [INFERRED 0.85]
- **Condição de estacionariedade ρ = λ/μ < 1** — e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_m10_texto_taxa_de_chegada_lambda, e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_m10_texto_taxa_de_servico_mu, e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_m10_texto_intensidade_de_trafego, e2___avalia__o_de_aprendizagem_m10___processo_de_nascimento_e_morte_m10_texto_hipotese_da_estacionariedade, e2___avalia__o_de_aprendizagem_e2_andamento_tempo_servico_maximo [INFERRED 0.85]
- **Rede de validacao T1 com ciclo Fila 2 <-> Fila 3** — t1___simulador_para_rede_de_filas_modelo_validacao, graphify_out_converted_t1___relat_rio_final_d1cadb55_fila1_gg1, graphify_out_converted_t1___relat_rio_final_d1cadb55_fila2_gg25, graphify_out_converted_t1___relat_rio_final_d1cadb55_fila3_gg210, t1___simulador_para_rede_de_filas_leia_me_rede_com_ciclos [INFERRED 0.85]
- **Análise do gargalo Q2 e da melhoria no N1** — t2___an_lise_por_simula__o_de_um_help_desk_de_ti_leia_me_gargalo_q2, t2___an_lise_por_simula__o_de_um_help_desk_de_ti_leia_me_melhoria_resolucao_primeiro_contato, t2___an_lise_por_simula__o_de_um_help_desk_de_ti_modelo_atual, t2___an_lise_por_simula__o_de_um_help_desk_de_ti_modelo_melhorado, graphify_out_converted_indices_desempenho_56417cf8_comparacao [INFERRED 0.85]
- **Current vs improved state-probability comparison across Q1, Q2, Q3** — t2___an_lise_por_simula__o_de_um_help_desk_de_ti_graficos_prob_estados_comparacao_q1_chart, t2___an_lise_por_simula__o_de_um_help_desk_de_ti_graficos_prob_estados_comparacao_q2_chart, t2___an_lise_por_simula__o_de_um_help_desk_de_ti_graficos_prob_estados_comparacao_q3_chart, concept_t2_melhoria_roteamento_triagem [INFERRED 0.85]
- **Resolução completa do exemplo M/M/3/3** — e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_imagens_02_exemplo_1_servidor_3_threads, e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_imagens_02_exemplo_2_modelo_mm33, e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_imagens_02_exemplo_4_calculo_pi, e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_imagens_03_perda_clientes_perda, e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_imagens_05_populacao_media_n_1_7947, e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_imagens_06_vazao_d_112_1688, e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_imagens_07_utilizacao_u_0_5982, e2___avalia__o_de_aprendizagem_m11___c_lculo_dos__ndices_de_desempenho_imagens_08_tempo_resposta_w_0_016 [INFERRED 0.95]
- **Conceitos da solucao estacionaria de CTMC: Q, pi Q = 0, normalizacao, pi** — concept_gerador_infinitesimal_q, concept_equacao_pi_q_zero, concept_normalizacao_soma_pi, concept_probabilidade_estado_pi [INFERRED 0.95]
- **Pipeline de solução de rede aberta (fila auxiliar, taxas de visita, vazão, utilização, tempo de resposta, população)** — concept_fila_auxiliar, concept_taxas_de_visita, concept_vazao, concept_utilizacao, concept_tempo_resposta, concept_populacao_media [EXTRACTED 1.00]
- **Conjunto de material da E4 (M13, LEIA-ME, andamento, PDF entregue)** — e4___avalia__o_de_aprendizagem_m13___redes_abertas_de_filas_m13_texto, e4___avalia__o_de_aprendizagem_leia_me, e4___avalia__o_de_aprendizagem_e4_andamento, e4_avaliação_de_aprendizagem_e4_avalia_o_de_aprendizagem_e4 [EXTRACTED 1.00]
- **Cadeia de fórmulas MVA (w, d0, d, n, u)** — concept_tempo_resposta, concept_vazao, concept_populacao_media, concept_utilizacao, concept_mva_analise_valores_medios [EXTRACTED 0.95]
- **Calculo dos indices de desempenho em rede aberta (vazao, utilizacao, tempo de resposta)** — e4___avalia__o_de_aprendizagem_m13___redes_abertas_de_filas_imagens_06_vazao, e4___avalia__o_de_aprendizagem_m13___redes_abertas_de_filas_imagens_07_utilizacao, e4___avalia__o_de_aprendizagem_m13___redes_abertas_de_filas_imagens_08_tempo_de_resposta, e4___avalia__o_de_aprendizagem_m13___redes_abertas_de_filas_imagens_09_resumo_formulas [EXTRACTED 1.00]
- **Obtencao das taxas de visita via fila auxiliar** — e4___avalia__o_de_aprendizagem_m13___redes_abertas_de_filas_imagens_04_exemplo_fila_auxiliar, e4___avalia__o_de_aprendizagem_m13___redes_abertas_de_filas_imagens_05_exemplo_taxas_de_visita, concept_fila_auxiliar, concept_taxas_de_visita [EXTRACTED 1.00]
- **Derivação das taxas de visita (rede, equações, V1=1)** — e5_avaliacao_de_aprendizagem_m14_redes_fechadas_de_filas_imagens_01_rede_exemplo_taxas_de_visita_jpg_rede, e5_avaliacao_de_aprendizagem_m14_redes_fechadas_de_filas_imagens_02_equacoes_taxas_de_visita_jpg_equacoes, e5_avaliacao_de_aprendizagem_m14_redes_fechadas_de_filas_imagens_03_assumir_v1_igual_1_jpg_passo [EXTRACTED 1.00]
- **Iteracoes MVA N=1,2,3 do exemplo M14** — e5___avalia__o_de_aprendizagem_m14___redes_fechadas_de_filas_imagens_06_exemplo_mva_n1, e5___avalia__o_de_aprendizagem_m14___redes_fechadas_de_filas_imagens_08_exemplo_mva_n2, e5___avalia__o_de_aprendizagem_m14___redes_fechadas_de_filas_imagens_09_exemplo_mva_n3 [EXTRACTED 1.00]

## Communities (8 total, 0 thin omitted)

### Community 0 - "Redes de Filas e Índices (M11/M13/M14)"
Cohesion: 0.06
Nodes (77): Cadeias de Markov em tempo contínuo, Tempo/demanda de servico S_i, Estabilidade estacionária (u < 1), Fila auxiliar X, Lei de Little, Mean-Value Analysis (MVA), Perda de clientes, População média (+69 more)

### Community 1 - "Simuladores M4/M6/T1 e Relatórios"
Cohesion: 0.05
Nodes (45): M4 Entrega Fila Simples (convertido), Cenario G/G/1/5 (chegadas 2..5, atendimento 3..5), Cenario G/G/2/5 (chegadas 2..5, atendimento 3..5), M4 Entrega Fila Simples - Preenchido (convertido), M6 Entrega Filas em Tandem (convertido), Fila 1 G/G/2/3 (tandem), Fila 2 G/G/1/5 (tandem, alimentada 100% pela Fila 1), T1 Relatorio Final - Simulador para Rede de Filas (convertido) (+37 more)

### Community 2 - "Cadeias de Markov (M12/E3)"
Cohesion: 0.06
Nodes (56): Cadeias de Markov, Equação πQ = 0, Escalas de tempo CTMC / DTMC, Gerador infinitesimal Q, Matriz de transição de estados, Modelo Markoviano, Normalização (Σπ = 1), Slide: Modelo Markoviano (+48 more)

### Community 3 - "T2 Análise e Planilha"
Cohesion: 0.08
Nodes (34): indices_desempenho.xlsx (planilha de índices, convertida), Abas por fila (Atual_Qn / Melhorado_Qn: tempo por estado -> N, D, U, W), Aba Comparação (atual x melhorado), Aba Parâmetros (filas e roteamento), Aba Sementes (5 sementes, média e desvio), LEIA-ME (Como rodar e analisar o T2), Equações de tráfego (conferência sem simulação), Exemplo hospitalar do M9 (triagem, consultórios, laboratório) (+26 more)

### Community 4 - "Teoria Nascimento e Morte (M10)"
Cohesion: 0.08
Nodes (51): Fila M/M/1/∞, Fila M/M/C/K, Intensidade de tráfego ρ = λ/μ, Notacao de Kendall, Probabilidade de estado π, Processo de Nascimento e Morte, Serie geometrica (soma rho^i = 1/(1-rho)), Q1 Triagem N1 (G/G/2/inf) (+43 more)

### Community 5 - "T2 Gargalo e Gráficos"
Cohesion: 0.09
Nodes (27): Q2 Especialista N2 (G/G/2/10), Chart: Q2 Especialista state probabilities (current model), Chart: Q2 state probabilities current vs improved, Gráficos de probabilidade dos estados (graficos/), rede_atual.svg / rede_melhorada.svg (desenho da rede), Diagram: current queueing network (Modelo atual), Diagram: improved queueing network (Modelo melhorado), kendall() (+19 more)

### Community 6 - "E2 Resolução Cafeteria"
Cohesion: 0.09
Nodes (33): Resolução manuscrita E2 Questão 1 (M/M/1/∞), Resolução manuscrita E2 Questão 2 (M/M/3/4), Checklist da entrega (um PDF por questão, prazo 21/10/2026), Exemplo de referência M/M/1/∞ λ=12, μ=20, N = 1,468530 clientes; D = 14,055930 clientes/h, P(N > 10) = ρ¹¹ = 0,005684, Perda = λ·π₄ = 0,944055 clientes/h, Questão 1 — Cafeteria Bauducco M/M/1/∞ (λ=15, μ=24) (+25 more)

### Community 7 - "Gerador MCL e Simulador de Rede"
Cohesion: 0.15
Nodes (8): GeradorMCL, simular_rede(), entra_cliente(), servidor_livre(), GeradorMCL, simular_rede(), entra_cliente(), servidor_livre()

## Ambiguous Edges - Review These
- `Equação πQ = 0` → `π como autovetor do autovalor unitário (definição do slide)`  [AMBIGUOUS]
  E3 - Avaliação de Aprendizagem/M12 - Cadeias de Markov/imagens/06-equacao-piQ.jpg · relation: conceptually_related_to
- `Slide M12: Matriz de transição M do laboratório com OFF` → `Entrada (OFF,OFF)=τ na matriz do slide (provável erro; deveria ser 0 ou diagonal negativa)`  [AMBIGUOUS]
  E3 - Avaliação de Aprendizagem/M12 - Cadeias de Markov/imagens/07-matriz-transicao.jpg · relation: conceptually_related_to
- `Produto (P0 ... POFF) x Q = (0 ... 0)` → `Sistema de 5 equacoes de balanco (uma por coluna de Q)`  [AMBIGUOUS]
  E3 - Avaliação de Aprendizagem/M12 - Cadeias de Markov/imagens/11-sistema-equacoes.jpg · relation: implements
- `Sistema de 5 equacoes de balanco (uma por coluna de Q)` → `Resolucao por substituicao: fixa P2=1, obtem P3=1,6; P1=0,465; P0=0,1696; POFF=0,1347`  [AMBIGUOUS]
  E3 - Avaliação de Aprendizagem/M12 - Cadeias de Markov/imagens/12-resolucao-sistema.jpg · relation: references
- `Probabilidade de estado π` → `Demonstracao: 1/soma rho^i = 1 - rho`  [AMBIGUOUS]
  E2 - Avaliação de Aprendizagem/M10 - Processo de Nascimento e Morte/imagens/07-interativo-mm1-4.png · relation: conceptually_related_to
- `Lei de Little` → `Tempo de resposta w_i: Lei de Little e Teorema da Chegada`  [AMBIGUOUS]
  E4 - Avaliação de Aprendizagem/M13 - Redes Abertas de Filas/imagens/08-tempo-de-resposta.jpg · relation: references

## Knowledge Gaps
- **50 isolated node(s):** `Andrei Markov`, `Google: Internet como Cadeia de Markov`, `Cadeia de Markov.pdf (diagrama a limpo)`, `Critérios de avaliação E3 (modelo 10, matriz/Q 20, sistema 20, resolução 30, probabilidades 20)`, `Prof. Rafael Chanin` (+45 more)
  These have ≤1 connection - possible missing edges or undocumented components. (Counts symbols only; 88 node(s) total have ≤1 connection when file, concept and rationale nodes are included.)

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `Probabilidade de estado π` connect `Teoria Nascimento e Morte (M10)` to `Redes de Filas e Índices (M11/M13/M14)`, `Cadeias de Markov (M12/E3)`, `T2 Gargalo e Gráficos`?**
  _High betweenness centrality (0.560) - this node is a cross-community bridge._
- **Are the 2 inferred relationships involving `Taxas de visita (Vi)` (e.g. with `Rede sorteada situacao 3 (4 filas, entradas 4 cl/h e 1 cl/h)` and `Rede sorteada situação 3 (4 filas, probabilidades 0,2/0,5/0,3, retornos à fila 1)`) actually correct?**
  _`Taxas de visita (Vi)` has 2 INFERRED edges - model-reasoned connections that need verification._
- **What connects `Andrei Markov`, `Google: Internet como Cadeia de Markov`, `Cadeia de Markov.pdf (diagrama a limpo)` to the rest of the system?**
  _50 weakly-connected nodes found - possible documentation gaps or missing edges._
- **Should `Redes de Filas e Índices (M11/M13/M14)` be split into smaller, more focused modules?**
  _Cohesion score 0.06264199935086011 - nodes in this community are weakly interconnected._
- **Why does `Chart: Q2 state probabilities current vs improved` connect `T2 Gargalo e Gráficos` to `Teoria Nascimento e Morte (M10)`?**
  _High betweenness centrality (0.244) - this node is a cross-community bridge._

### Low-confidence Hints
_AMBIGUOUS edges — the extractor was unsure. Verify before acting on these._

- **What is the exact relationship between `Equação πQ = 0` and `π como autovetor do autovalor unitário (definição do slide)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `Slide M12: Matriz de transição M do laboratório com OFF` and `Entrada (OFF,OFF)=τ na matriz do slide (provável erro; deveria ser 0 ou diagonal negativa)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._