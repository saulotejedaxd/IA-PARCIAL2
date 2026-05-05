"""
37 - Mapas Autoorganizados de Kohonen (SOM)
Aprendizaje no supervisado: cada neurona del mapa 2D tiene un vector
de pesos. La neurona BMU (mejor coincidencia) y sus vecinas se acercan
al patron de entrada. Aqui se entrena con puntos en R^2.
"""
import math
import random


def dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def som(datos, ancho=4, alto=4, epochs=200, lr=0.5, sigma=2.0):
    mapa = [[[random.random(), random.random()] for _ in range(ancho)] for _ in range(alto)]
    for ep in range(epochs):
        lr_t = lr * (1 - ep / epochs)
        s_t = sigma * (1 - ep / epochs)
        for x in datos:
            bi, bj, bd = 0, 0, float("inf")
            for i in range(alto):
                for j in range(ancho):
                    d = dist(mapa[i][j], x)
                    if d < bd:
                        bi, bj, bd = i, j, d
            for i in range(alto):
                for j in range(ancho):
                    h = math.exp(-((i - bi) ** 2 + (j - bj) ** 2) / (2 * s_t ** 2 + 1e-9))
                    for k in range(2):
                        mapa[i][j][k] += lr_t * h * (x[k] - mapa[i][j][k])
    return mapa


if __name__ == "__main__":
    datos = [[random.gauss(0, 1), random.gauss(0, 1)] for _ in range(50)] + \
            [[random.gauss(5, 1), random.gauss(5, 1)] for _ in range(50)]
    mapa = som(datos)
    print("Mapa 4x4 entrenado (esquinas):")
    print("  (0,0):", [round(x, 2) for x in mapa[0][0]])
    print("  (3,3):", [round(x, 2) for x in mapa[3][3]])
