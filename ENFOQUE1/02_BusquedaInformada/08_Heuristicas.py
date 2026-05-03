"""
08 - Heuristicas
Una heuristica h(n) estima el costo desde n hasta la meta. Se usa para
guiar la busqueda. Aqui se muestran tres heuristicas clasicas para el
puzzle 8 y para grids: piezas mal colocadas, distancia Manhattan,
distancia Euclidiana.
"""
import math


def h_piezas_mal(estado, meta):
    return sum(1 for a, b in zip(estado, meta) if a != b and a != 0)


def h_manhattan(p, q):
    return abs(p[0] - q[0]) + abs(p[1] - q[1])


def h_euclidiana(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


if __name__ == "__main__":
    estado = [1, 2, 3, 4, 0, 6, 7, 5, 8]
    meta = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    print("Piezas mal colocadas:", h_piezas_mal(estado, meta))
    print("Manhattan (0,0)->(3,4):", h_manhattan((0, 0), (3, 4)))
    print("Euclidiana (0,0)->(3,4):", h_euclidiana((0, 0), (3, 4)))
