"""
11 - Busqueda de Ascension de Colinas (Hill Climbing)
Busqueda local: en cada paso elige el vecino con mejor valor.
Riesgos clasicos: maximos locales, mesetas, crestas. Aqui se maximiza
una funcion sobre enteros con vecindad +-1.
"""
import random


def hill_climbing(f, x0, vecinos, max_iter=1000):
    actual = x0
    for _ in range(max_iter):
        candidatos = vecinos(actual)
        siguiente = max(candidatos, key=f, default=actual)
        if f(siguiente) <= f(actual):
            return actual, f(actual)
        actual = siguiente
    return actual, f(actual)


if __name__ == "__main__":
    f = lambda x: -(x - 7) ** 2 + 50
    vecinos = lambda x: [x - 1, x + 1]
    inicio = random.randint(-20, 20)
    sol, val = hill_climbing(f, inicio, vecinos)
    print(f"Inicio={inicio}  Optimo encontrado x={sol}  f(x)={val}")
