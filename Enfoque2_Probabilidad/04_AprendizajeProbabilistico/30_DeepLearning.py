"""
30 - Aprendizaje Profundo (Deep Learning)
Red feedforward con varias capas ocultas, activaciones ReLU y
clasificacion binaria via sigmoide. Entrenamiento por backprop.
"""
import math
import random


def relu(x):
    return max(0.0, x)


def relu_d(x):
    return 1.0 if x > 0 else 0.0


def sigmoide(x):
    return 1 / (1 + math.exp(-x))


def crear_red(estructura):
    return [[[random.uniform(-0.5, 0.5) for _ in range(estructura[i] + 1)]
             for _ in range(estructura[i + 1])]
            for i in range(len(estructura) - 1)]


def fwd(red, x):
    activaciones = [x]
    a = x
    for i, capa in enumerate(red):
        es_ultima = i == len(red) - 1
        nuevos = []
        for neurona in capa:
            z = neurona[-1] + sum(w * v for w, v in zip(neurona[:-1], a))
            nuevos.append(sigmoide(z) if es_ultima else relu(z))
        a = nuevos
        activaciones.append(a)
    return activaciones


def entrenar(red, X, Y, lr=0.05, epochs=2000):
    for _ in range(epochs):
        for x, y in zip(X, Y):
            acts = fwd(red, x)
            deltas = [[(acts[-1][0] - y) * acts[-1][0] * (1 - acts[-1][0])]]
            for i in range(len(red) - 1, 0, -1):
                capa, ant = red[i], acts[i]
                d_prev = []
                for j in range(len(red[i - 1])):
                    err = sum(capa[k][j] * deltas[0][k] for k in range(len(capa)))
                    d_prev.append(err * relu_d(ant[j]))
                deltas.insert(0, d_prev)
            for i, capa in enumerate(red):
                for j, neurona in enumerate(capa):
                    for k in range(len(neurona) - 1):
                        neurona[k] -= lr * deltas[i][j] * acts[i][k]
                    neurona[-1] -= lr * deltas[i][j]


if __name__ == "__main__":
    X = [[0, 0], [0, 1], [1, 0], [1, 1]]
    Y = [0, 1, 1, 0]  # XOR
    red = crear_red([2, 4, 4, 1])
    entrenar(red, X, Y)
    for x in X:
        print(f"{x} -> {round(fwd(red, x)[-1][0], 3)}")
