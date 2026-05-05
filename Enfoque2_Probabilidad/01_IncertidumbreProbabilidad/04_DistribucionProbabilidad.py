"""
04 - Distribucion de Probabilidad
Asigna probabilidad a cada valor de una variable aleatoria.
Aqui se muestra la distribucion binomial discreta y la uniforme.
"""
import math


def binomial(n, p):
    return [math.comb(n, k) * (p ** k) * ((1 - p) ** (n - k)) for k in range(n + 1)]


def uniforme(valores):
    return {v: 1 / len(valores) for v in valores}


if __name__ == "__main__":
    print("Binomial(10, 0.3):", [round(x, 3) for x in binomial(10, 0.3)])
    print("Uniforme dado:", uniforme(range(1, 7)))
