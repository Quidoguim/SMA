# Como rodar e testar o simulador do T1

`simulador_rede.py` generaliza o motor do M6 (mesma lógica de eventos e mesmo
gerador MCL) pra carregar a topologia de um arquivo `.yml`, em vez de vir
escrita no código Python. O único requisito externo é o PyYAML:

```bash
pip install pyyaml
```

## Rodando a rede de validação do enunciado

```bash
python3 simulador_rede.py modelo_validacao.yml
```

`modelo_validacao.yml` descreve a rede pedida na entrega: Fila 1 (G/G/1,
chegadas entre 2 e 4, atendimento entre 1 e 2, capacidade ilimitada) roteando
20% pra Fila 2 e 80% pra Fila 3; Fila 2 (G/G/2/5, atendimento entre 4 e 6)
roteando 30% de volta pra Fila 1, 50% pra Fila 3 e 20% saindo da rede; Fila 3
(G/G/2/10, atendimento entre 5 e 15) roteando 70% de volta pra Fila 2 e 30%
saindo da rede. Primeiro cliente chega em 2,0, simulação para ao consumir
100.000 números aleatórios (mesmo critério do M4/M6). A saída mostra, para
cada fila: número de aleatórios usados, tempo global da simulação, clientes
perdidos e a tabela de tempo acumulado/probabilidade por estado.

## Descrevendo outra rede de filas

Crie outro `.yml` no mesmo formato — mesmas chaves do simulador do módulo 3
(`arrivals`/`queues`/`network`), documentadas no cabeçalho de
`simulador_rede.py`:

```yaml
arrivals:
   Q1: 2.0                # instante da 1a chegada externa (só filas com
                            # chegada externa própria precisam disso)

queues:
   Q1:
      servers: 1
      # sem "capacity" -> fila ilimitada
      minArrival: 2.0
      maxArrival: 4.0
      minService: 1.0
      maxService: 2.0
   Q2:
      servers: 2
      capacity: 5
      minService: 4.0
      maxService: 6.0

network:
-  source: Q1
   target: Q2
   probability: 0.2         # resto (0.8) sai da rede depois de atendido em Q1
```

Sobre `network`: cada aresta `source -> target` com sua `probability`. A
probabilidade que faltar até somar 1.0, por fila de origem, é a chance do
cliente sair da rede depois de atendido ali. A soma declarada não pode passar
de 1.0, e uma aresta apontando pra fila inexistente é rejeitada — ambos os
casos levantam `ValueError`. Aceita qualquer topologia, inclusive ciclos
entre filas (a rede de validação tem um: Fila 2 ↔ Fila 3).

Quantos aleatórios consumir vem de `--aleatorios` na linha de comando, ou de
`rndnumbersPerSeed` no `.yml`, ou 100.000 por padrão. A semente do gerador é
`--seed` (padrão 1). As chaves `rndnumbers`/`seeds` do formato do módulo 3
são ignoradas por este script — ficam no arquivo só pra permitir rodar o
mesmo `.yml` no `simulator.jar` (ver abaixo).

## Conferindo a implementação

`modelo_validacao.yml` já roda direto no `simulator.jar` do módulo 3 (que
também está neste diretório), bastando prefixar o arquivo com a linha
`!PARAMETERS` exigida por ele:

```bash
{ echo "!PARAMETERS"; cat modelo_validacao.yml; } > /tmp/teste_jar.yml
java -jar simulator.jar run /tmp/teste_jar.yml
```

Rodamos essa conferência durante o desenvolvimento: com a mesma topologia, os
resultados do `simulador_rede.py` (PRNG próprio, validado no M4/M6) batem de
perto com os do `simulator.jar` (PRNG do módulo 3) — probabilidades por
estado e número de perdas na mesma faixa em todas as filas, o que era
esperado (gerador diferente, mesma lógica de rede) e serve de sanidade pra
topologia e pro motor de simulação.

Como conferência adicional, `simular_rede` com uma única fila sem `network`
reproduz o resultado do M4; com duas filas em tandem reproduz o do M6 (mesma
lógica de evento, mesmo gerador).
