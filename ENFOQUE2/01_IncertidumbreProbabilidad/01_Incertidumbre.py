"""
01 - Incertidumbre
Cuantifica grado de creencia en eventos. Aqui se simula tirar dados
y se compara la frecuencia empirica con la probabilidad teorica.
"""
import random


def simular(experimento, n=10000):
    conteo = {}
    for _ in range(n):
        r = experimento()
        conteo[r] = conteo.get(r, 0) + 1
    return {k: v / n for k, v in sorted(conteo.items())}


if __name__ == "__main__":
    dado = lambda: random.randint(1, 6)
    print("Frecuencias dado justo:", simular(dado))
    print("Probabilidad teorica:", {i: round(1/6, 4) for i in range(1, 7)})
