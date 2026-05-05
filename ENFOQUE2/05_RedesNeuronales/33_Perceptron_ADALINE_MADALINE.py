"""
33 - Perceptron, ADALINE y MADALINE
Perceptron: actualiza pesos solo cuando se equivoca (clasificacion).
ADALINE: usa la salida lineal antes de la activacion para minimizar MSE.
MADALINE: red de varias unidades ADALINE en paralelo.
"""


def perceptron(X, y, lr=0.1, epochs=20):
    w = [0.0] * len(X[0])
    b = 0.0
    for _ in range(epochs):
        for x, t in zip(X, y):
            o = 1 if sum(wi * xi for wi, xi in zip(w, x)) + b >= 0 else 0
            err = t - o
            w = [wi + lr * err * xi for wi, xi in zip(w, x)]
            b += lr * err
    return w, b


def adaline(X, y, lr=0.05, epochs=200):
    w = [0.0] * len(X[0])
    b = 0.0
    for _ in range(epochs):
        for x, t in zip(X, y):
            o = sum(wi * xi for wi, xi in zip(w, x)) + b
            err = t - o
            w = [wi + lr * err * xi for wi, xi in zip(w, x)]
            b += lr * err
    return w, b


def madaline(X, n_unidades=2, lr=0.05, epochs=200):
    return [adaline(X, [(i + 1) % n_unidades for i in range(len(X))], lr, epochs)
            for _ in range(n_unidades)]


if __name__ == "__main__":
    X = [(0, 0), (0, 1), (1, 0), (1, 1)]
    y = [0, 0, 0, 1]
    w, b = perceptron(X, y)
    print("Perceptron AND w:", [round(x, 2) for x in w], "b:", round(b, 2))
    w, b = adaline(X, [0, 0, 0, 1])
    print("ADALINE AND w:", [round(x, 2) for x in w], "b:", round(b, 2))
    print("MADALINE (2 unidades):", madaline(X))
