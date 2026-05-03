"""
20 - Propagacion de Restricciones (AC-3)
Mantiene consistencia de arcos: para cada arco (Xi, Xj), elimina valores
de Xi sin soporte en Xj. Detecta inconsistencias antes de buscar.
"""
from collections import deque


def revisar(dominios, xi, xj, restr):
    revisado = False
    for x in list(dominios[xi]):
        if not any(restr(xi, x, xj, y) for y in dominios[xj]):
            dominios[xi].remove(x)
            revisado = True
    return revisado


def ac3(dominios, vecinos, restr):
    cola = deque((xi, xj) for xi in vecinos for xj in vecinos[xi])
    while cola:
        xi, xj = cola.popleft()
        if revisar(dominios, xi, xj, restr):
            if not dominios[xi]:
                return False
            for xk in vecinos[xi]:
                if xk != xj:
                    cola.append((xk, xi))
    return True


if __name__ == "__main__":
    dominios = {"A": [1, 2, 3], "B": [1, 2, 3], "C": [1, 2, 3]}
    vecinos = {"A": ["B"], "B": ["A", "C"], "C": ["B"]}
    restr = lambda x, vx, y, vy: vx != vy
    ac3(dominios, vecinos, restr)
    print("Dominios tras AC-3:", dominios)
