"""
21 - Salto Atras Dirigido por Conflictos (Conflict-Directed Backjumping)
Cuando una variable no tiene valor consistente, salta directamente a
la variable mas reciente en su conjunto de conflicto, en vez de
retroceder cronologicamente.
"""


def cbj(asignacion, conflictos, csp, orden):
    if len(asignacion) == len(orden):
        return asignacion, None
    idx = len(asignacion)
    var = orden[idx]
    conf_var = set()
    for valor in csp["dominios"][var]:
        ok = True
        for v in csp["vecinos"][var]:
            if v in asignacion and not csp["restriccion"](var, valor, v, asignacion[v]):
                conf_var.add(v)
                ok = False
                break
        if ok:
            asignacion[var] = valor
            res, salto = cbj(asignacion, conflictos, csp, orden)
            if res is not None:
                return res, None
            del asignacion[var]
            if salto and salto != var:
                return None, salto
            conf_var |= (conflictos.get(var, set()) - {var})
    if not conf_var:
        return None, None
    salto_a = max((orden.index(v) for v in conf_var if v in orden), default=-1)
    objetivo = orden[salto_a] if salto_a >= 0 else None
    if objetivo:
        conflictos[objetivo] = conflictos.get(objetivo, set()) | (conf_var - {objetivo})
    return None, objetivo


if __name__ == "__main__":
    csp = {
        "dominios": {v: ["R", "G", "B"] for v in ["A", "B", "C", "D"]},
        "vecinos": {"A": ["B", "C"], "B": ["A", "C", "D"],
                    "C": ["A", "B", "D"], "D": ["B", "C"]},
        "restriccion": lambda x, vx, y, vy: vx != vy,
    }
    print("CBJ:", cbj({}, {}, csp, ["A", "B", "C", "D"])[0])
