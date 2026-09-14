# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

Coursework repository for the "Simulação e Métodos Analíticos" (SMA) discipline. Each deliverable ("módulo") lives in its own top-level folder named after the module (e.g. `M4 - Desenvolvimento de Simulador para uma Fila`), containing the source code plus the submitted `.docx`/`.pdf` writeup for that module. New modules are added as separate sibling folders, not merged into existing ones. Once a module has been submitted, treat its folder as historical — later fixes/improvements land in the next module's folder, not by rewriting a past one, so the repo keeps an honest history of how the coursework evolved.

## Git commits

Do not add `Co-Authored-By` or other AI-attribution trailers to commits or PR descriptions in this repository.

## Running the code

Each module's script is standalone Python (stdlib only, no dependencies, no build step). Run directly:

```bash
python "M4 - Desenvolvimento de Simulador para uma Fila/simulador_fila.py"
```

There is no test suite, linter, or package manager configured in this repo.

## Architecture (M4 — queue simulator)

`simulador_fila.py` is a discrete-event simulator for a G/G/c/K queue (c = 1 or 2 servers, K = total system capacity including service):

- `GeradorMCL`: linear congruential generator (Xn+1 = (a·Xn + c) mod M) used as the sole source of randomness for both inter-arrival and service times (uniform distributions via `.uniform(low, high)`). `verifica_hull_dobell` checks the Hull-Dobell conditions so the generator's period is full before it's trusted for the run.
- `simular_fila`: the event loop. It tracks the next arrival time and one pending departure time per server, always advancing the clock to the nearest of these candidate events, accumulating time-in-state (`times[]`) for computing steady-state probabilities. Arrivals when the system is at capacity `K` count as `perdas` (blocked/lost customers); arrivals when all servers are busy but capacity remains join `fila_espera` (waiting line). The simulation runs until a fixed number of random draws (`max_aleatorios`) is consumed, not a fixed wall-clock time.
- `imprimir_resultados`: formats the per-state probability table and sanity-check sums (accumulated time and probabilities should each total the global simulation time / 100%).
- The `__main__` block runs two scenarios back-to-back (G/G/1/5 and G/G/2/5) sharing the same arrival/service parameter set (`PARAMS_COMUNS`).

Simulation parameters (arrival/service ranges, server count, capacity K, RNG seed/multiplier/increment/modulus) are passed as plain function arguments to `simular_fila` — there is no config file.

## Architecture (M6 — queue network simulator)

`simulador_rede_filas.py` generalizes M4's engine from a single G/G/c/K queue to a network of them connected by probabilistic routing (any topology, including cycles). It duplicates `GeradorMCL`/`verifica_hull_dobell` from M4 rather than importing across module folders, keeping each module self-contained per the repo convention above.

- `Fila`: a dataclass describing one queue — `id`, `num_servidores`, `capacidade` (K), `atendimento_min/max`, and optionally `chegada_min/max` + `primeira_chegada` (omit all three if the queue has no external arrival stream, only routed-in customers). `destinos` is a `{fila_id: probabilidade}` dict describing where customers go after being served here; whatever probability doesn't sum to 1.0 is the implicit chance of leaving the network (`SAIDA`). Validated in `__post_init__` (raises if probabilities exceed 1.0 or point at an unknown queue).
- `simular_rede(filas, max_aleatorios, ...)`: same event-loop shape as M4's `simular_fila` (find the earliest candidate event across *every* queue's external arrival and every busy server's departure, advance the clock, accumulate `times[fid][estado]` for **all** queues over that interval — not just the one whose event fired — then apply the event), extended with:
  - `escolhe_destino`: when a queue's departure has more than one possible destination, draws one random number to pick it via cumulative probability; a queue with a single destination (including the common "always exits" case) consumes no draw at all.
  - Departures routed to another queue re-enter it through the same `entra_cliente` logic used for external arrivals (capacity check → free server or wait line → loss if full), so a full downstream queue blocks/loses that customer independently of the upstream queue.
  - Every additional random draw within one event is guarded by `if not should_stop`, mirroring M4's stop-mid-event semantics — the outer loop can only be mid-event when `should_stop` flips from a draw earlier in that same iteration, since it's guaranteed `False` at the top of every iteration.
- Self-loop routing (a queue routing back to itself) isn't specially handled — fine for the tandem/feed-forward topologies used so far, but note it before extending to a network with cycles through the same queue.
- Sanity check: running `simular_rede` with a single `Fila` and no `destinos` reproduces M4's `simular_fila` output exactly, draw-for-draw, given the same parameters and seed (no routing draw is consumed when there's only one possible destination).
- `imprimir_resultados_rede` prints the shared `tempo_global`/`aleatorios_usados` once, then each queue's state/probability table and loss count.
