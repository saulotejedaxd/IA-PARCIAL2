"""
05 - Busqueda en Profundidad Iterativa (IDDFS)
Combina ventajas de BFS (completitud, optimalidad en grafos sin pesos)
con la baja memoria de DFS, repitiendo busquedas con limite creciente.
"""


def dls(grafo, nodo, meta, limite, camino):
    if nodo == meta:
        return camino
    if limite <= 0:
        return None
    for vecino in grafo.get(nodo, []):
        if vecino in camino:
            continue
        res = dls(grafo, vecino, meta, limite - 1, camino + [vecino])
        if res:
            return res
    return None


def iddfs(grafo, inicio, meta, max_profundidad=20):
    for limite in range(max_profundidad + 1):
        res = dls(grafo, inicio, meta, limite, [inicio])
        if res:
            return res, limite
    return None, -1


if __name__ == "__main__":
    grafo = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }
    camino, prof = iddfs(grafo, "A", "F")
    print(f"Camino: {camino}  Profundidad: {prof}")
