"""
04 - Busqueda en Profundidad Limitada (DLS)
DFS con un limite de profundidad maxima para evitar caer en
ramas infinitas o demasiado largas.
"""


def dls(grafo, nodo, meta, limite, camino=None):
    if camino is None:
        camino = [nodo]
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


if __name__ == "__main__":
    grafo = {
        "A": ["B", "C"],
        "B": ["D", "E"],
        "C": ["F"],
        "D": [],
        "E": ["F"],
        "F": [],
    }
    print("Limite 1:", dls(grafo, "A", "F", 1))
    print("Limite 2:", dls(grafo, "A", "F", 2))
    print("Limite 3:", dls(grafo, "A", "F", 3))
