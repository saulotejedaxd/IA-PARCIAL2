"""
22 - Busqueda Local: Minimos-Conflictos
Asignacion completa inicial; en cada paso elige variable en conflicto
y le asigna el valor que minimiza el numero de violaciones.
Muy efectivo para N-reinas y CSPs grandes.
"""
import random


def conflictos(var, val, asignacion, vecinos, restr):
    return sum(1 for v in vecinos[var] if v in asignacion
               and not restr(var, val, v, asignacion[v]))


def min_conflictos(csp, max_iter=1000):
    asignacion = {v: random.choice(csp["dominios"][v]) for v in csp["variables"]}
    for _ in range(max_iter):
        en_conflicto = [v for v in csp["variables"]
                        if conflictos(v, asignacion[v], asignacion,
                                       csp["vecinos"], csp["restriccion"]) > 0]
        if not en_conflicto:
            return asignacion
        var = random.choice(en_conflicto)
        asignacion[var] = min(csp["dominios"][var],
                              key=lambda val: conflictos(var, val, asignacion,
                                                          csp["vecinos"],
                                                          csp["restriccion"]))
    return None


if __name__ == "__main__":
    n = 8
    csp = {
        "variables": list(range(n)),
        "dominios": {i: list(range(n)) for i in range(n)},
        "vecinos": {i: [j for j in range(n) if j != i] for i in range(n)},
        "restriccion": lambda x, vx, y, vy: vx != vy and abs(x - y) != abs(vx - vy),
    }
    print("8-reinas (fila->col):", min_conflictos(csp))
