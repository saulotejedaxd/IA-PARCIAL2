"""
14 - Busqueda de Haz Local (Local Beam Search)
Mantiene k estados en cada iteracion. Genera todos sus sucesores y
conserva los k mejores globalmente. Equivale a k busquedas paralelas
con comunicacion.
"""
import random


def haz_local(f, inicios, vecinos, k=4, max_iter=200):
    estados = list(inicios[:k])
    mejor = max(estados, key=f)
    for _ in range(max_iter):
        sucesores = [v for s in estados for v in vecinos(s)]
        if not sucesores:
            break
        sucesores.sort(key=f, reverse=True)
        estados = sucesores[:k]
        if f(estados[0]) > f(mejor):
            mejor = estados[0]
    return mejor, f(mejor)


if __name__ == "__main__":
    f = lambda x: -(x - 7) ** 2 + 50
    vecinos = lambda x: [x - 1, x + 1]
    inicios = [random.randint(-30, 30) for _ in range(8)]
    sol, val = haz_local(f, inicios, vecinos, k=4)
    print(f"Mejor x={sol}  f(x)={val}")
