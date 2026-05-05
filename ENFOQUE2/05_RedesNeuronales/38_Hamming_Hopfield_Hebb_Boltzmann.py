"""
38 - Hamming, Hopfield, Hebb, Boltzmann
- Hamming: red para clasificar por minima distancia de Hamming.
- Hopfield: red recurrente para memoria asociativa con pesos simetricos.
- Hebb: regla de aprendizaje "lo que dispara junto se conecta junto".
- Boltzmann: red estocastica con dinamica probabilistica (esquema).
"""
import math
import random


def hamming_clasificar(prototipos, x):
    return min(range(len(prototipos)),
               key=lambda i: sum(a != b for a, b in zip(prototipos[i], x)))


def hebb(prototipos):
    n = len(prototipos[0])
    W = [[0] * n for _ in range(n)]
    for p in prototipos:
        for i in range(n):
            for j in range(n):
                if i != j:
                    W[i][j] += p[i] * p[j]
    return W


def hopfield_actualizar(W, x, iters=10):
    x = list(x)
    n = len(x)
    for _ in range(iters):
        for i in range(n):
            s = sum(W[i][j] * x[j] for j in range(n))
            x[i] = 1 if s >= 0 else -1
    return x


def boltzmann_paso(W, x, T=1.0):
    n = len(x)
    i = random.randrange(n)
    s = sum(W[i][j] * x[j] for j in range(n))
    p = 1 / (1 + math.exp(-2 * s / T))
    x[i] = 1 if random.random() < p else -1
    return x


if __name__ == "__main__":
    protos = [[1, 1, -1, -1], [-1, -1, 1, 1]]
    print("Hamming (1,1,-1,1):", hamming_clasificar(protos, [1, 1, -1, 1]))
    W = hebb(protos)
    rec = hopfield_actualizar(W, [1, -1, -1, -1])
    print("Hopfield recupera:", rec)
    bz = list([1, -1, 1, -1])
    for _ in range(20):
        bz = boltzmann_paso(W, bz)
    print("Boltzmann tras 20 pasos:", bz)
