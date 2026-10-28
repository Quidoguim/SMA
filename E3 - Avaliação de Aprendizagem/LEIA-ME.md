# E3 - Avaliação de Aprendizagem

Material de apoio para a E3, tirado do texto multimodal do Moodle do módulo M12.
O módulo tem um `.md` com o texto, as fórmulas transcritas e as imagens na pasta
`imagens/`.

| Módulo | Texto | Assunto |
|---|---|---|
| M12 | [M12-texto.md](<M12 - Cadeias de Markov/M12-texto.md>) | Cadeias de Markov (CTMC), matriz de transição, gerador infinitesimal, πQ = 0, resolução do sistema e normalização |

O enunciado da questão e o andamento da resolução ficam em
[E3-andamento.md](E3-andamento.md). A resolução escrita à mão, entregue no Moodle
em 28/10/2026, está em [E3.pdf](E3.pdf).

## Resumo do método (CTMC)

1. **Modelo:** um estado para cada situação do sistema e uma seta com a taxa de cada
   transição. Taxa é o inverso do tempo; todas na mesma unidade.
2. **Matriz de transição:** linha = estado de origem, coluna = estado de destino,
   valor = taxa. Sem transição = 0.
3. **Gerador infinitesimal Q:** cada elemento da diagonal recebe o valor que faz a
   linha somar **zero** (o negativo da soma das taxas que saem daquele estado).
4. **Sistema:** π · Q = 0. Cada **coluna** de Q vira uma equação: soma de
   Pᵢ × (valor da linha i naquela coluna) = 0.
5. **Resolução:** dar um valor arbitrário positivo a uma variável (ex.: P₂ = 1) e
   isolar as outras, uma equação por vez. Uma equação sobra e serve de conferência.
6. **Normalização:** somar todas as proporções e dividir cada uma pela soma; as
   probabilidades somam 1 (100%).

## Exemplo resolvido

Laboratório com 3 máquinas e falta de luz (estados 0, 1, 2, 3, OFF), com λ = 10,
μ = 2, σ = 0,25 e τ = 6 por hora: P₂ = 1, P₃ = 1,6, P₁ = 0,465, P₀ = 0,1696,
P_OFF = 0,1347, soma 3,3693, probabilidades 5,03%, 13,80%, 29,68%, 47,49% e 4% (M12).
