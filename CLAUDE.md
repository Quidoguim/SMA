# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository purpose

Coursework repository for the "Simulação e Métodos Analíticos" (SMA) discipline. Each deliverable ("módulo") lives in its own top-level folder named after the module (e.g. `M4 - Desenvolvimento de Simulador para uma Fila`), containing the source code plus the submitted `.docx`/`.pdf` writeup for that module. New modules are added as separate sibling folders, not merged into existing ones.

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
