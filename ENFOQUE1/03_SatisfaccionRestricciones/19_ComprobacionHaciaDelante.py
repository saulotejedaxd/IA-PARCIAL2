"""
19 - Comprobacion Hacia Delante (Forward Checking)
Despues de asignar una variable, elimina valores incompatibles de los
dominios de los vecinos no asignados; si un dominio queda vacio, retrocede.
"""
import copy


def forward_check(var, valor, dominios, vecinos, restr, asignacion):
    nuevos = copy.deepcopy(dominios)
    nuevos[var] = [valor]
    for v in vecinos[var]:
        if v in asignacion:
            continue
        nuevos[v] = [d for d in nuevos[v] if restr(var, valor, v, d)]
        if not nuevos[v]:
            return None
    return nuevos


def backtrack_fc(asignacion, dominios, csp):
    if len(asignacion) == len(csp["variables"]):
        return asignacion
    var = next(v for v in csp["variables"] if v not in asignacion)
    for valor in dominios[var]:
        nd = forward_check(var, valor, dominios, csp["vecinos"], csp["restriccion"], asignacion)
        if nd is not None:
            asignacion[var] = valor
            res = backtrack_fc(asignacion, nd, csp)
            if res is not None:
                return res
            del asignacion[var]
    return None


if __name__ == "__main__":
    csp = {
        "variables": ["A", "B", "C"],
        "vecinos": {"A": ["B", "C"], "B": ["A", "C"], "C": ["A", "B"]},
        "restriccion": lambda x, vx, y, vy: vx != vy,
    }
    dominios = {"A": ["R", "G", "B"], "B": ["R", "G", "B"], "C": ["R", "G", "B"]}
    print("Solucion FC:", backtrack_fc({}, dominios, csp))
