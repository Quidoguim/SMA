# Como rodar e testar o simulador do M6

`simulador_rede_filas.py` é um único arquivo Python 3, sem dependências além da
biblioteca padrão. Não precisa instalar nada.

## Rodando a rede de validação do enunciado

```bash
python3 "simulador_rede_filas.py"
```

Isso executa direto a rede pedida na entrega — Fila 1 (G/G/2/3, chegadas entre
1 e 5, atendimento entre 4 e 5) em tandem com a Fila 2 (G/G/1/5, atendimento
entre 1 e 3, sem chegada externa, recebendo 100% do que sai da Fila 1) — com
o primeiro cliente chegando em 2,5 e 100.000 números aleatórios. A saída
mostra, para cada fila: número de aleatórios usados, tempo global da
simulação, clientes perdidos e a tabela de tempo acumulado/probabilidade por
estado.

## Descrevendo outra rede de filas

Para testar outra topologia, edite o bloco `filas_validacao` no
`if __name__ == "__main__":` (ou importe o módulo e monte sua própria lista
de `Fila`s em outro script). Cada fila da rede é um `Fila(...)`:

```python
from simulador_rede_filas import Fila, simular_rede, imprimir_resultados_rede

filas = [
    Fila(
        id="Fila 1",                 # nome único da fila na rede
        num_servidores=2,            # c
        capacidade=3,                # K (fila de espera + em atendimento)
        chegada_min=1, chegada_max=5,  # chegada externa uniforme (omita as
        primeira_chegada=2.5,          # 3 linhas acima se a fila só recebe
                                        # clientes roteados de outra fila)
        atendimento_min=4, atendimento_max=5,
        destinos={"Fila 2": 1.0},    # 100% do que é atendido aqui vai pra Fila 2
    ),
    Fila(
        id="Fila 2",
        num_servidores=1,
        capacidade=5,
        atendimento_min=1, atendimento_max=3,
        # sem chegada_min/max/primeira_chegada -> só recebe roteamento
        # sem destinos -> 100% sai da rede depois de atendida aqui
    ),
]

resultado = simular_rede(filas, max_aleatorios=100_000)
imprimir_resultados_rede("minha rede", resultado)
```

Sobre o campo `destinos`: é um dict `{id_da_fila_destino: probabilidade}`. A
probabilidade que sobrar até completar 1.0 é a chance do cliente sair da rede
depois de atendido naquela fila — por isso uma fila terminal (sem para onde
rotear) simplesmente não define `destinos` (ou usa `{}`), e 100% dos clientes
saem do sistema ali. A soma das probabilidades declaradas não pode passar de
1.0, e um destino inexistente é rejeitado — ambos os casos levantam
`ValueError` na hora de montar a `Fila` ou de chamar `simular_rede`. O
roteamento aceita qualquer topologia, inclusive com mais de dois destinos por
fila ou ciclos entre filas (exceto uma fila apontando pra ela mesma, que não
foi testado).

A simulação para assim que consome `max_aleatorios` números pseudoaleatórios
no total (contados em toda a rede, não por fila) — mesmo critério de parada
usado no M4.

## Conferindo a implementação

`simulador_fila.py` do M4 e `simulador_rede_filas.py` do M6 compartilham a
mesma lógica de evento e o mesmo gerador de aleatórios (MCL). Como conferência
de sanidade: rodar `simular_rede` com uma única `Fila` (sem `destinos`) e os
mesmos parâmetros do M4 reproduz exatamente os resultados do M4 — nenhum
aleatório extra é consumido quando uma fila só tem um destino possível
(inclusive "sair da rede").
