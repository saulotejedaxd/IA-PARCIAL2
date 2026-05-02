"""
03 - Busqueda en Profundidad (DFS - Depth-First Search)
Explora cada rama hasta el final antes de retroceder. Usa pila (LIFO),
ya sea explicita o por recursion. No garantiza camino mas corto.
"""


def dfs(grafo, inicio, meta, visitados=None, camino=None):
    if visitados is None:
        visitados, camino = set(), [inicio]
    visitados.add(inicio)
    if inicio == meta:
        return camino
    for vecino in grafo.get(inicio, []):
        if vecino not in visitados:
            resultado = dfs(grafo, vecino, meta, visitados, camino + [vecino])
            if resultado:
                return resultado
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
    print("Camino DFS A -> F:", dfs(grafo, "A", "F"))
