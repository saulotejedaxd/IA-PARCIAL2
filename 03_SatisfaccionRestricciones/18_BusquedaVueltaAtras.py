"""
18 - Busqueda de Vuelta Atras (Backtracking)
DFS sobre el espacio de asignaciones parciales con poda por consistencia.
"""


def backtracking(asignacion, csp):
    if len(asignacion) == len(csp["variables"]):
        return asignacion
    var = next(v for v in csp["variables"] if v not in asignacion)
    for valor in csp["dominios"][var]:
        if all(csp["restriccion"](var, valor, v, asignacion[v])
               for v in csp["vecinos"][var] if v in asignacion):
            asignacion[var] = valor
            res = backtracking(asignacion, csp)
            if res is not None:
                return res
            del asignacion[var]
    return None


if __name__ == "__main__":
    csp = {
        "variables": ["WA", "NT", "SA", "Q", "NSW", "V", "T"],
        "dominios": {v: ["R", "G", "B"] for v in
                     ["WA", "NT", "SA", "Q", "NSW", "V", "T"]},
        "vecinos": {
            "WA": ["NT", "SA"], "NT": ["WA", "SA", "Q"],
            "Q": ["NT", "SA", "NSW"], "NSW": ["Q", "SA", "V"],
            "V": ["NSW", "SA"], "SA": ["WA", "NT", "Q", "NSW", "V"], "T": [],
        },
        "restriccion": lambda x, vx, y, vy: vx != vy,
    }
    print("Solucion:", backtracking({}, csp))
