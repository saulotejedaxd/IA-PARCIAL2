"""
36 - Retropropagacion del Error
Algoritmo para ajustar pesos en una MLP minimizando MSE via gradiente
descendente. Aqui se entrena XOR y se reporta el error.
"""
import math
import random


def sig(x): return 1 / (1 + math.exp(-x))
def sig_d(y): return y * (1 - y)


def crear(capas):
    return [[[random.uniform(-1, 1) for _ in range(capas[i] + 1)]
             for _ in range(capas[i + 1])]
            for i in range(len(capas) - 1)]


def fwd(red, x):
    activaciones = [x]
    a = x
    for capa in red:
        a = [sig(neur[-1] + sum(w * v for w, v in zip(neur[:-1], a))) for neur in capa]
        activaciones.append(a)
    return activaciones


def entrenar(red, X, Y, lr=0.5, epochs=5000):
    for _ in range(epochs):
        for x, y in zip(X, Y):
            a = fwd(red, x)
            deltas = [[(a[-1][i] - y[i]) * sig_d(a[-1][i]) for i in range(len(y))]]
            for k in range(len(red) - 1, 0, -1):
                d = []
                for j in range(len(a[k])):
                    err = sum(red[k][m][j] * deltas[0][m] for m in range(len(red[k])))
                    d.append(err * sig_d(a[k][j]))
                deltas.insert(0, d)
            for k, capa in enumerate(red):
                for j, neur in enumerate(capa):
                    for i in range(len(neur) - 1):
                        neur[i] -= lr * deltas[k][j] * a[k][i]
                    neur[-1] -= lr * deltas[k][j]


if __name__ == "__main__":
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    Y = [[0], [1], [1], [0]]
    red = crear([2, 3, 1])
    entrenar(red, X, Y)
    for x in X:
        print(f"{x} -> {round(fwd(red, x)[-1][0], 3)}")
