"""
09 - Busqueda Voraz Primero el Mejor (Greedy Best-First Search)
Expande el nodo con menor h(n). Es rapida pero no optima ni completa
en grafos infinitos: puede atorarse o tomar caminos largos.
"""
import heapq


def voraz(grafo, inicio, meta, h):
    frontera = [(h[inicio], inicio, [inicio])]
    visitados = set()
    while frontera:
        _, nodo, camino = heapq.heappop(frontera)
        if nodo == meta:
            return camino
        if nodo in visitados:
            continue
        visitados.add(nodo)
        for vecino in grafo.get(nodo, []):
            if vecino not in visitados:
                heapq.heappush(frontera, (h[vecino], vecino, camino + [vecino]))
    return None


if __name__ == "__main__":
    grafo = {
        "A": ["B", "C"], "B": ["D"], "C": ["D", "E"],
        "D": ["F"], "E": ["F"], "F": [],
    }
    h = {"A": 6, "B": 4, "C": 4, "D": 2, "E": 3, "F": 0}
    print("Camino voraz A -> F:", voraz(grafo, "A", "F", h))
