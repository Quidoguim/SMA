# E4 - Avaliação de Aprendizagem

Material de apoio para a E4, tirado do texto multimodal do Moodle do módulo M13.
O módulo tem um `.md` com o texto, as fórmulas transcritas e as imagens na pasta
`imagens/`.

| Módulo | Texto | Assunto |
|---|---|---|
| M13 | [M13-texto.md](<M13 - Redes Abertas de Filas/M13-texto.md>) | Redes abertas de filas, fila auxiliar, taxas de visita, vazão, utilização, tempo de resposta e população |

O enunciado da questão e o andamento da resolução ficam em
[E4-andamento.md](E4-andamento.md).

## Resumo do método (rede aberta)

1. **Fechar a rede:** fila auxiliar X recebe todas as saídas e alimenta as filas
   com entrada externa, cada uma com a fração Lᵢ / Σ L. Vₓ = 1.
2. **Taxas de visita:** para cada fila, Vᵢ = soma de (fração que chega × V de quem
   manda). Resolver o sistema. Conferência: o que sai para X soma 1.
3. **Vazão:** dᵢ = Vᵢ × Σ L.
4. **Utilização:** uᵢ = dᵢ × Sᵢ (tem que dar menor que 1).
5. **Tempo de resposta:** wᵢ = Sᵢ / (1 − uᵢ).
6. **População:** nᵢ = uᵢ / (1 − uᵢ).

## Exemplo resolvido

Entrada 2 e 3 cli/u.t. nas filas 1 e 2; 1 → 2 (0,8), 1 → 3 (0,2), 3 → 1 (0,5):
V₁ = 0,4444, V₂ = 0,9555, V₃ = 0,0888 (M13).
