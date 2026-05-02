"""
12 - Busqueda Tabu
Busqueda local que mantiene una lista (tabu) de movimientos recientes
prohibidos para escapar de optimos locales y evitar ciclos.
"""
from collections import deque
import random


def busqueda_tabu(f, x0, vecinos, tam_tabu=5, max_iter=200):
    actual = x0
    mejor = x0
    tabu = deque(maxlen=tam_tabu)
    for _ in range(max_iter):
        candidatos = [v for v in vecinos(actual) if v not in tabu]
        if not candidatos:
            break
        siguiente = max(candidatos, key=f)
        tabu.append(actual)
        actual = siguiente
        if f(actual) > f(mejor):
            mejor = actual
    return mejor, f(mejor)


if __name__ == "__main__":
    f = lambda x: -(x - 7) ** 2 + 50 + 5 * (x % 3 == 0)
    vecinos = lambda x: [x - 1, x + 1, x + 2, x - 2]
    inicio = random.randint(-10, 30)
    sol, val = busqueda_tabu(f, inicio, vecinos)
    print(f"Inicio={inicio}  Mejor x={sol}  f(x)={val}")
