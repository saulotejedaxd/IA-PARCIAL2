"""
16 - Hipotesis de Markov: Procesos de Markov
P(X_t | X_{0:t-1}) = P(X_t | X_{t-1}). El futuro solo depende del estado
actual. Aqui se simula una cadena de Markov de tres estados.
"""
import random


def simular_cadena(estados, P, inicio, pasos=20):
    s = inicio
    historia = [s]
    for _ in range(pasos):
        r = random.random()
        acc = 0
        for j, p in enumerate(P[estados.index(s)]):
            acc += p
            if r < acc:
                s = estados[j]
                break
        historia.append(s)
    return historia


if __name__ == "__main__":
    estados = ["sol", "nub", "lluv"]
    P = [[0.7, 0.2, 0.1], [0.3, 0.5, 0.2], [0.2, 0.4, 0.4]]
    print("Trayectoria:", simular_cadena(estados, P, "sol", 15))
