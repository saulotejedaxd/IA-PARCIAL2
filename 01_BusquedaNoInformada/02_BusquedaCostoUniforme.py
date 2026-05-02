"""
02 - Busqueda en Anchura de Costo Uniforme (UCS)
Variante de BFS que expande siempre el nodo con menor costo acumulado.
Optima cuando los costos de las aristas son no negativos.
Estructura clave: cola de prioridad (heap).
"""
import heapq


def ucs(grafo, inicio, meta):
    frontera = [(0, inicio, [inicio])]
    visitados = {}
    while frontera:
        costo, nodo, camino = heapq.heappop(frontera)
        if nodo == meta:
            return camino, costo
        if nodo in visitados and visitados[nodo] <= costo:
            continue
        visitados[nodo] = costo
        for vecino, peso in grafo.get(nodo, []):
            nuevo = costo + peso
            heapq.heappush(frontera, (nuevo, vecino, camino + [vecino]))
    return None, float("inf")


if __name__ == "__main__":
    grafo = {
        "A": [("B", 1), ("C", 4)],
        "B": [("C", 2), ("D", 5)],
        "C": [("D", 1)],
        "D": [],
    }
    camino, costo = ucs(grafo, "A", "D")
    print(f"Camino: {camino}  Costo total: {costo}")
