# E5 - Avaliação de Aprendizagem

Material de apoio para a E5, tirado do texto multimodal do Moodle do módulo M14.
O módulo tem um `.md` com o texto, as fórmulas transcritas e as imagens na pasta
`imagens/`.

| Módulo | Texto | Assunto |
|---|---|---|
| M14 | [M14-texto.md](<M14 - Redes Fechadas de Filas/M14-texto.md>) | Redes fechadas de filas, taxas de visita, MVA (tempo de resposta, vazão, população, utilização) |

O enunciado da questão e o andamento da resolução ficam em
[E5-andamento.md](E5-andamento.md).

## Resumo do método (rede fechada, MVA)

1. **Taxas de visita:** sem fila X. Assume V₁ = 1 e resolve uma equação por fila.
2. **Ponto de partida:** nᵢ(0) = 0, ou uma população nᵢ(N − 1) já conhecida.
3. **Tempo de resposta:** wᵢ(N) = Sᵢ × (1 + nᵢ(N − 1)).
4. **Vazão da rede:** d₀(N) = N / Σ (wⱼ(N) × Vⱼ).
5. **Vazão da fila:** dᵢ(N) = d₀(N) × Vᵢ.
6. **População:** nᵢ(N) = wᵢ(N) × dᵢ(N). Conferência: Σ nᵢ(N) ≈ N.
7. **Utilização:** uᵢ = dᵢ(N) × Sᵢ.

## Exemplo resolvido

Rede 1 → 2 (0,7), 1 → 3 (0,3), 2 e 3 voltam para 1; S = 2, 5, 4; N = 3:
n₁(3) = 0,7672, n₂(3) = 1,8478, n₃(3) = 0,3856 (M14).
