"""
15 - Procesos Estacionarios
Un proceso es estacionario cuando sus distribuciones no cambian con el
tiempo. Aqui se calcula la distribucion estacionaria de una cadena de
Markov resolviendo pi = pi * P por iteracion de potencias.
"""


def estacionaria(P, iters=100):
    n = len(P)
    pi = [1 / n] * n
    for _ in range(iters):
        pi = [sum(pi[i] * P[i][j] for i in range(n)) for j in range(n)]
    return pi


if __name__ == "__main__":
    P = [[0.7, 0.3], [0.4, 0.6]]
    pi = estacionaria(P)
    print(f"Distribucion estacionaria: {[round(x, 3) for x in pi]}")
