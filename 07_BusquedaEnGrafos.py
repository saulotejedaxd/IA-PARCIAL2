"""
07 - Busqueda en Grafos (Graph Search generico)
Esquema generalizado de busqueda con conjunto de explorados,
parametrizable por la estrategia (cola, pila, prioridad).
Evita re-expansion de estados ya vistos.
"""
from collections import deque
import heapq


def graph_search(grafo, inicio, meta, estrategia="bfs"):
    if estrategia == "bfs":
        frontera = deque([(inicio, [inicio])])
        pop = frontera.popleft
        push = lambda x: frontera.append(x)
    elif estrategia == "dfs":
        frontera = [(inicio, [inicio])]
        pop = frontera.pop
        push = lambda x: frontera.append(x)
    else:
        raise ValueError("estrategia debe ser bfs o dfs")
    explorados = set()
    while frontera:
        nodo, camino = pop()
        if nodo == meta:
            return camino
        if nodo in explorados:
            continue
        explorados.add(nodo)
        for vecino in grafo.get(nodo, []):
            if vecino not in explorados:
                push((vecino, camino + [vecino]))
    return None


if __name__ == "__main__":
    grafo = {
        "A": ["B", "C"], "B": ["D"], "C": ["D", "E"],
        "D": ["F"], "E": ["F"], "F": [],
    }
    print("BFS:", graph_search(grafo, "A", "F", "bfs"))
    print("DFS:", graph_search(grafo, "A", "F", "dfs"))
