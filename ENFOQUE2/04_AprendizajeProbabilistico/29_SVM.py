"""
29 - Maquinas de Vectores Soporte (SVM)
Encuentra el hiperplano de maximo margen. Aqui se implementa una SVM
lineal entrenada con descenso por sub-gradiente (hinge loss + L2).
Tambien se ilustra el truco del nucleo gaussiano.
"""
import math
import random


def entrenar_svm(X, y, lr=0.01, lam=0.01, epochs=1000):
    d = len(X[0])
    w = [0.0] * d
    b = 0.0
    for _ in range(epochs):
        i = random.randrange(len(X))
        margen = y[i] * (sum(w[k] * X[i][k] for k in range(d)) + b)
        if margen < 1:
            for k in range(d):
                w[k] += lr * (y[i] * X[i][k] - 2 * lam * w[k])
            b += lr * y[i]
        else:
            for k in range(d):
                w[k] += lr * (-2 * lam * w[k])
    return w, b


def predecir(w, b, x):
    return 1 if sum(w[k] * x[k] for k in range(len(x))) + b >= 0 else -1


def kernel_gaussiano(x, y, sigma=1.0):
    return math.exp(-sum((a - b) ** 2 for a, b in zip(x, y)) / (2 * sigma ** 2))


if __name__ == "__main__":
    X = [(1, 2), (2, 3), (3, 3), (6, 5), (7, 8), (8, 8)]
    y = [-1, -1, -1, 1, 1, 1]
    w, b = entrenar_svm(X, y)
    print(f"w={[round(x, 2) for x in w]}  b={round(b, 2)}")
    print("Pred (5,5):", predecir(w, b, (5, 5)))
    print("Kernel gauss (1,2)~(7,8):", round(kernel_gaussiano((1, 2), (7, 8)), 5))
