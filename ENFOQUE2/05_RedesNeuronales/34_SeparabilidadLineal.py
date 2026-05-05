"""
34 - Separabilidad Lineal
Un conjunto es linealmente separable si existe un hiperplano que separa
las clases. AND y OR si lo son; XOR no. Aqui se entrena un perceptron
y se reporta si converge sin errores.
"""


def perceptron_converge(X, y, lr=0.1, max_epochs=100):
    w = [0.0] * len(X[0])
    b = 0.0
    for _ in range(max_epochs):
        errores = 0
        for x, t in zip(X, y):
            o = 1 if sum(wi * xi for wi, xi in zip(w, x)) + b >= 0 else 0
            err = t - o
            if err:
                errores += 1
                w = [wi + lr * err * xi for wi, xi in zip(w, x)]
                b += lr * err
        if errores == 0:
            return True, w, b
    return False, w, b


if __name__ == "__main__":
    X = [(0, 0), (0, 1), (1, 0), (1, 1)]
    print("AND separable:", perceptron_converge(X, [0, 0, 0, 1])[0])
    print("OR  separable:", perceptron_converge(X, [0, 1, 1, 1])[0])
    print("XOR separable:", perceptron_converge(X, [0, 1, 1, 0])[0])
