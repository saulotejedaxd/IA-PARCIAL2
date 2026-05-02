"""
06 - Busqueda Bidireccional
Lanza dos BFS simultaneas: una desde el inicio y otra desde la meta.
Termina cuando ambas fronteras se encuentran. Reduce drasticamente
el espacio explorado: 2 * b^(d/2) en lugar de b^d.
"""
from collections import deque


def expandir(grafo, frontera, padres, otra_frontera):
    nuevos = {}
    for nodo in frontera:
        for vecino in grafo.get(nodo, []):
            if vecino not in padres:
                padres[vecino] = nodo
                nuevos[vecino] = True
                if vecino in otra_frontera:
                    return vecino, nuevos
    return None, nuevos


def bidireccional(grafo, inicio, meta):
    if inicio == meta:
        return [inicio]
    padres_i = {inicio: None}
    padres_m = {meta: None}
    front_i = {inicio: True}
    front_m = {meta: True}
    while front_i and front_m:
        encuentro, front_i = expandir(grafo, front_i, padres_i, padres_m)
        if encuentro:
            return reconstruir(padres_i, padres_m, encuentro)
        encuentro, front_m = expandir(grafo, front_m, padres_m, padres_i)
        if encuentro:
            return reconstruir(padres_i, padres_m, encuentro)
    return None


def reconstruir(padres_i, padres_m, encuentro):
    camino = []
    n = encuentro
    while n is not None:
        camino.append(n)
        n = padres_i.get(n)
    camino.reverse()
    n = padres_m.get(encuentro)
    while n is not None:
        camino.append(n)
        n = padres_m.get(n)
    return camino


if __name__ == "__main__":
    grafo = {
        "A": ["B", "C"], "B": ["A", "D"], "C": ["A", "E"],
        "D": ["B", "F"], "E": ["C", "F"], "F": ["D", "E", "G"], "G": ["F"],
    }
    print("Camino bidireccional A -> G:", bidireccional(grafo, "A", "G"))
