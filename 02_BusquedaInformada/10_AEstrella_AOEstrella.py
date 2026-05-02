"""
10 - Busqueda A* y AO*
A* combina costo real g(n) con la heuristica h(n): f(n) = g(n) + h(n).
Si h es admisible (no sobreestima) A* es optimo y completo.
AO* es la generalizacion para grafos AND-OR (planificacion con elecciones
y subobjetivos conjuntos). Aqui se muestra A* completo y un esqueleto AO*.
"""
import heapq


def a_estrella(grafo, inicio, meta, h):
    frontera = [(h[inicio], 0, inicio, [inicio])]
    mejor_g = {inicio: 0}
    while frontera:
        f, g, nodo, camino = heapq.heappop(frontera)
        if nodo == meta:
            return camino, g
        for vecino, peso in grafo.get(nodo, []):
            ng = g + peso
            if ng < mejor_g.get(vecino, float("inf")):
                mejor_g[vecino] = ng
                heapq.heappush(frontera, (ng + h[vecino], ng, vecino, camino + [vecino]))
    return None, float("inf")


def ao_estrella(nodo, grafo_and_or, h, resueltos=None):
    if resueltos is None:
        resueltos = {}
    if nodo in resueltos:
        return resueltos[nodo]
    if nodo not in grafo_and_or or not grafo_and_or[nodo]:
        resueltos[nodo] = (h.get(nodo, 0), [nodo])
        return resueltos[nodo]
    mejor = (float("inf"), None)
    for opcion in grafo_and_or[nodo]:
        costo, plan = 0, [nodo]
        for hijo, peso in opcion:
            c, p = ao_estrella(hijo, grafo_and_or, h, resueltos)
            costo += peso + c
            plan.append(p)
        if costo < mejor[0]:
            mejor = (costo, plan)
    resueltos[nodo] = mejor
    return mejor


if __name__ == "__main__":
    grafo = {
        "A": [("B", 1), ("C", 4)], "B": [("D", 5), ("E", 2)],
        "C": [("F", 1)], "D": [], "E": [("F", 1)], "F": [],
    }
    h = {"A": 5, "B": 3, "C": 2, "D": 4, "E": 1, "F": 0}
    print("A* A -> F:", a_estrella(grafo, "A", "F", h))

    grafo_ao = {
        "S": [[("A", 1), ("B", 1)], [("C", 3)]],
        "A": [], "B": [], "C": [],
    }
    print("AO* desde S:", ao_estrella("S", grafo_ao, {"A": 1, "B": 2, "C": 1}))
