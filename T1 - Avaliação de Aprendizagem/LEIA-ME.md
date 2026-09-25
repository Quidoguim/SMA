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

Testes feitos durante o desenvolvimento:

- **Regressão exata contra M4 e M6**: descrevendo os mesmos parâmetros do M4
  (fila única) e do M6 (duas filas em tandem) num `.yml` e rodando com
  `--seed 1`, `simulador_rede.py` reproduz os resultados desses módulos
  número por número (mesmo tempo global, mesmos tempos acumulados por
  estado) — a generalização pra YAML não alterou a lógica de simulação já
  aprovada nas entregas anteriores.
- **Estatística contra o `simulator.jar`** (mesma topologia, PRNG diferente,
  100.000 aleatórios): tanto na rede de validação deste módulo quanto no
  `model.yml` de exemplo do módulo 3 (4 filas, com realimentação Q2→Q1 e uma
  fila de capacidade ilimitada), as probabilidades por estado, o número de
  perdas e o tempo global batem de perto entre as duas ferramentas — no
  `model.yml`, por exemplo, perdas na Fila 2 ficaram em 1.246 aqui contra uma
  média de 1.248,8 no `simulator.jar` (5 sementes), e o tempo global divergiu
  menos de 0,2%.
- **Números fixos idênticos nos dois simuladores** (`rndnumbers` em vez de
  gerador): numa fila isolada, os dois batem 100% exato (mesmo tempo global,
  mesmos tempos por estado) — confirma que a lógica de evento de uma fila
  única é idêntica à do `simulator.jar`. Com roteamento entre filas os
  números exatos divergem (a ordem em que cada implementação decide sortear
  o roteamento vs. o atendimento da fila destino vs. o próximo cliente da
  fila de origem é uma escolha interna do `simulator.jar`, que é só um
  `.jar` fechado) — isso não é um bug, é esperado, e por isso a validação de
  rede usa comparação estatística (muitos aleatórios), não número a número.
- **Casos de erro**: roteamento pra fila inexistente e soma de
  probabilidades acima de 1.0 são rejeitados com `ValueError`, como
  esperado.

`modelo_validacao.yml` roda direto no `simulator.jar` do módulo 3 (que também
está neste diretório), bastando prefixar o arquivo com a linha
`!PARAMETERS` exigida por ele:

```bash
{ echo "!PARAMETERS"; cat modelo_validacao.yml; } > /tmp/teste_jar.yml
java -jar simulator.jar run /tmp/teste_jar.yml
```

O `model.yml` de exemplo do módulo 3 já tem essa linha e roda direto tanto no
`simulator.jar` quanto no `simulador_rede.py` (`python3 simulador_rede.py
model.yml`) — o loader ignora a tag `!PARAMETERS`, que não é YAML padrão.
