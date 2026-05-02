"""
01 - Busqueda en Anchura (BFS - Breadth-First Search)
Explora el grafo nivel por nivel desde el nodo inicial, garantizando
encontrar la solucion mas corta en numero de aristas.
Estructura clave: Cola FIFO.
"""
from collections import deque


def bfs(grafo, inicio, meta):
    visitados = {inicio}
    cola = deque([(inicio, [inicio])])
    while cola:
        nodo, camino = cola.popleft()
        if nodo == meta:
            return camino
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                visitados.add(vecino)
                cola.append((vecino, camino + [vecino]))
    return None


if __name__ == "__main__":
    grafo = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }
    print("Camino BFS A -> F:", bfs(grafo, "A", "F"))
