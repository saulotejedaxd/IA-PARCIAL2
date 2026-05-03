"""
13 - Busqueda de Temple Simulado (Simulated Annealing)
Acepta empeoramientos con probabilidad exp(dE/T) que decrece con
la temperatura. Permite escapar optimos locales.
"""
import math
import random


def temple_simulado(f, x0, vecinos, T0=100.0, alpha=0.95, max_iter=2000):
    actual = x0
    mejor = x0
    T = T0
    for _ in range(max_iter):
        cand = random.choice(vecinos(actual))
        delta = f(cand) - f(actual)
        if delta > 0 or random.random() < math.exp(delta / max(T, 1e-9)):
            actual = cand
            if f(actual) > f(mejor):
                mejor = actual
        T *= alpha
    return mejor, f(mejor)


if __name__ == "__main__":
    f = lambda x: -(x - 7) ** 2 + 50
    vecinos = lambda x: [x - 1, x + 1]
    sol, val = temple_simulado(f, random.randint(-50, 50), vecinos)
    print(f"Optimo x={sol}  f(x)={val}")
