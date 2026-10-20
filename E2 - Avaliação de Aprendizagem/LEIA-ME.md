# E2 - Avaliação de Aprendizagem

Material de apoio para a E2, tirado dos textos multimodais do Moodle dos módulos
M10 e M11. Cada módulo tem um `.md` com o texto, as fórmulas transcritas e as
imagens na pasta `imagens/`.

| Módulo | Texto | Assunto |
|---|---|---|
| M10 | [M10-texto.md](<M10 - Processo de Nascimento e Morte/M10-texto.md>) | processo de nascimento e morte, intensidade de tráfego, M/M/1/∞ e M/M/C/K (método dos pesos) |
| M11 | [M11-texto.md](<M11 - Cálculo dos Índices de Desempenho/M11-texto.md>) | perda de clientes, população, vazão, utilização e tempo de resposta |

## Resumo das fórmulas

Taxa é o inverso do tempo: atender um cliente em 20 min dá μ = 3 por hora.
λ e μ precisam estar na mesma unidade de tempo.

**Intensidade de tráfego:** ρ = λ / μ. Com ρ < 1 existe solução estacionária;
com ρ ≥ 1 a fila infinita é instável.

**M/M/1/∞**

- π₀ = 1 − λ/μ
- πᵢ = πᵢ₋₁ · (λ/μ) = π₀ · (λ/μ)ⁱ

**M/M/C/K (método dos pesos)**

1. W₀ = 1
2. Wᵢ = Wᵢ₋₁ · λ / (min(i, C) · μ), para i = 1 … K
3. πᵢ = Wᵢ / Σⱼ Wⱼ (normaliza para somar 1)

**Índices de desempenho** (somatórios de j = 0 até K; μⱼ = min(j, C) · μ)

| Índice | Fórmula |
|---|---|
| Perda | λ · π_K (chegada × probabilidade de estar cheio) |
| População média | N = Σ πⱼ · j |
| Vazão | D = Σ πⱼ · μⱼ |
| Utilização | U = Σ πⱼ · min(j, C) / C (com 1 servidor: 1 − π₀) |
| Tempo de resposta | W = N / D |

Conferência: λ − perda (por unidade de tempo) = vazão D.

## Exemplos resolvidos

- M/M/1/∞ com λ = 10, μ = 20: π₀ = 50%, π₁ = 25%, π₂ = 12,5% … (M10)
- M/M/1/4 e M/M/2/4 com λ = 5, μ = 10 (M10)
- M/M/3/3 do servidor com 3 threads: λ = 156,25 req/h, μ = 62,5 req/h,
  perda = 353,75 req/dia, N = 1,7947, D = 112,1688 req/h, U = 59,82%,
  W = 0,016 h (M11)
