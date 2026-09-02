# Simulador de fila G/G/c/K por eventos discretos.
# c = número de servidores (1 ou 2), K = capacidade total (fila + atendimento).
# Chegadas e atendimentos são uniformes, gerados pelo MCL (Método Congruente Linear).

import math


def verifica_hull_dobell(a, c, M):
    # condições de Hull-Dobell pra garantir período completo do MCL
    cond1 = math.gcd(c, M) == 1

    fatores_primos_M = set()
    n = M
    d = 2
    while d * d <= n:
        while n % d == 0:
            fatores_primos_M.add(d)
            n //= d
        d += 1
    if n > 1:
        fatores_primos_M.add(n)

    cond2 = all((a - 1) % p == 0 for p in fatores_primos_M)
    cond3 = (M % 4 != 0) or ((a - 1) % 4 == 0)

    return cond1, cond2, cond3, fatores_primos_M


class GeradorMCL:
    # Xn+1 = (a*Xn + c) mod M, normalizado em (0,1)

    def __init__(self, seed, a, c, M):
        self.a = a
        self.c = c
        self.M = M
        self.previous = seed
        self.count_used = 0

    def next_random(self):
        self.previous = (self.a * self.previous + self.c) % self.M
        self.count_used += 1
        return self.previous / self.M

    def uniform(self, low, high):
        u = self.next_random()
        return low + u * (high - low)


# M original (2^16) só dava 65536 valores antes de repetir, e a simulação
# precisa de 100.000 aleatórios -> aumentamos pra 2^31 (ainda satisfaz Hull-Dobell)
SEED = 1
A = 1103515245
C = 12345
M = 2 ** 31


def simular_fila(num_servidores, K, chegada_min, chegada_max,
                  atendimento_min, atendimento_max,
                  primeira_chegada, max_aleatorios,
                  seed=SEED, a=A, c=C, m=M):
    # roda a simulação até usar max_aleatorios números e devolve os resultados

    rng = GeradorMCL(seed, a, c, m)

    clock = 0.0
    estado = 0                # clientes no sistema (0..K)
    times = [0.0] * (K + 1)   # tempo acumulado em cada estado
    perdas = 0
    fila_espera = 0

    departures = [None] * num_servidores  # próxima saída de cada servidor, None = livre
    next_arrival = primeira_chegada       # 1º cliente chega em tempo fixo, sem RNG

    should_stop = False

    while not should_stop:
        # próximo evento = chegada ou a saída mais próxima
        candidatos = [(next_arrival, 'chegada', None)]
        for s in range(num_servidores):
            if departures[s] is not None:
                candidatos.append((departures[s], 'saida', s))
        tempo_evento, tipo_evento, servidor = min(candidatos, key=lambda x: x[0])

        times[estado] += tempo_evento - clock
        clock = tempo_evento

        if tipo_evento == 'chegada':
            if estado < K:
                estado += 1
                servidor_livre = None
                for s in range(num_servidores):
                    if departures[s] is None:
                        servidor_livre = s
                        break
                if servidor_livre is not None:
                    t_atend = rng.uniform(atendimento_min, atendimento_max)
                    if rng.count_used >= max_aleatorios:
                        should_stop = True
                    departures[servidor_livre] = clock + t_atend
                else:
                    fila_espera += 1  # servidores ocupados, cliente espera
            else:
                perdas += 1  # sistema cheio, cliente é bloqueado

            if not should_stop:
                t_entre = rng.uniform(chegada_min, chegada_max)
                if rng.count_used >= max_aleatorios:
                    should_stop = True
                next_arrival = clock + t_entre

        else:
            estado -= 1
            if fila_espera > 0:
                fila_espera -= 1
                if not should_stop:
                    t_atend = rng.uniform(atendimento_min, atendimento_max)
                    if rng.count_used >= max_aleatorios:
                        should_stop = True
                    departures[servidor] = clock + t_atend
                else:
                    departures[servidor] = None
            else:
                departures[servidor] = None

        if rng.count_used >= max_aleatorios:
            should_stop = True

    tempo_global = clock
    probabilidades = [times[i] / tempo_global for i in range(K + 1)]

    return {
        'num_servidores': num_servidores,
        'K': K,
        'times': times,
        'probabilidades': probabilidades,
        'perdas': perdas,
        'tempo_global': tempo_global,
        'aleatorios_usados': rng.count_used,
    }


def imprimir_resultados(nome_fila, resultado):
    K = resultado['K']
    print("=" * 70)
    print(f"Resultados da simulação: {nome_fila}")
    print("=" * 70)
    print(f"Número de servidores ......... {resultado['num_servidores']}")
    print(f"Capacidade do sistema (K) .... {K}")
    print(f"Números aleatórios usados .... {resultado['aleatorios_usados']}")
    print(f"Tempo global da simulação .... {resultado['tempo_global']:.4f}")
    print(f"Clientes perdidos (bloqueados)  {resultado['perdas']}")
    print("-" * 70)
    print(f"{'Estado':<8}{'Tempo acumulado':<20}{'Probabilidade':<15}")
    for i in range(K + 1):
        t = resultado['times'][i]
        p = resultado['probabilidades'][i]
        print(f"{i:<8}{t:<20.4f}{p*100:<14.4f}%")
    print("-" * 70)
    soma_tempos = sum(resultado['times'])
    soma_probs = sum(resultado['probabilidades'])
    print(f"Soma dos tempos acumulados ... {soma_tempos:.4f} "
          f"(deve ser igual ao tempo global)")
    print(f"Soma das probabilidades ...... {soma_probs*100:.4f}%")
    print()


if __name__ == "__main__":

    cond1, cond2, cond3, fatores = verifica_hull_dobell(A, C, M)
    print("Verificação das condições de Hull-Dobell (período completo):")
    print(f"  mdc(c, M) = 1 ..................... {cond1}")
    print(f"  (a-1) divisível pelos fatores primos de M {sorted(fatores)} ..... {cond2}")
    print(f"  (a-1) divisível por 4 (pois M múltiplo de 4) ..... {cond3}")
    print(f"  M = {M} (período completo garante até M números distintos, "
          f"muito acima dos 100.000 exigidos)")
    print()

    PARAMS_COMUNS = dict(
        chegada_min=2, chegada_max=5,
        atendimento_min=3, atendimento_max=5,
        primeira_chegada=3.0,
        max_aleatorios=100_000,
    )

    resultado_1 = simular_fila(num_servidores=1, K=5, **PARAMS_COMUNS)
    imprimir_resultados("G/G/1/5", resultado_1)

    resultado_2 = simular_fila(num_servidores=2, K=5, **PARAMS_COMUNS)
    imprimir_resultados("G/G/2/5", resultado_2)
