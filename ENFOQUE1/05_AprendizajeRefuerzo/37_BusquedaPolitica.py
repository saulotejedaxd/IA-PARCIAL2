"""
37 - Busqueda de la Politica (Policy Search)
Optimiza directamente los parametros de una politica parametrica
maximizando el retorno esperado. Aqui se usa hill-climbing sobre
una politica softmax para un problema con 2 estados y 2 acciones.
"""
import math
import random


def softmax(theta):
    e = [math.exp(t) for t in theta]
    z = sum(e)
    return [x / z for x in e]


def evaluar(theta, episodios=200):
    total = 0
    for _ in range(episodios):
        s = 0
        G = 0
        for _ in range(10):
            probs = softmax(theta[s])
            a = 0 if random.random() < probs[0] else 1
            r = 1 if (s == 0 and a == 1) or (s == 1 and a == 0) else 0
            G += r
            s = 1 - s if a == 1 else s
        total += G
    return total / episodios


def policy_search(theta, sigma=0.3, iters=200):
    mejor = evaluar(theta)
    for _ in range(iters):
        prop = [[t + random.gauss(0, sigma) for t in fila] for fila in theta]
        v = evaluar(prop)
        if v > mejor:
            theta, mejor = prop, v
    return theta, mejor


if __name__ == "__main__":
    theta = [[0.0, 0.0], [0.0, 0.0]]
    th, val = policy_search(theta)
    print("Politica softmax estado 0:", [round(x, 2) for x in softmax(th[0])])
    print("Politica softmax estado 1:", [round(x, 2) for x in softmax(th[1])])
    print("Retorno medio:", round(val, 2))
