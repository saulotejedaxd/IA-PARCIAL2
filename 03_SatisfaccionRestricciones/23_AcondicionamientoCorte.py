"""
23 - Acondicionamiento del Corte (Cutset Conditioning)
Para CSPs con un grafo de restricciones casi acrico: identifica un
cutset (conjunto cuya eliminacion deja el grafo sin ciclos), instancia
sus variables y resuelve el resto como arbol.
"""


def es_arbol(vecinos, eliminar):
    visitados = set()
    nodos = [v for v in vecinos if v not in eliminar]
    if not nodos:
        return True
    pila = [(nodos[0], None)]
    while pila:
        n, padre = pila.pop()
        if n in visitados:
            return False
        visitados.add(n)
        for x in vecinos[n]:
            if x in eliminar or x == padre:
                continue
            pila.append((x, n))
    return len(visitados) == len(nodos)


def resolver_arbol(variables, dominios, vecinos, restr, asignacion):
    if not variables:
        return asignacion
    v = variables[0]
    for d in dominios[v]:
        if all(restr(v, d, n, asignacion[n]) for n in vecinos[v] if n in asignacion):
            asignacion[v] = d
            r = resolver_arbol(variables[1:], dominios, vecinos, restr, asignacion)
            if r is not None:
                return r
            del asignacion[v]
    return None


def cutset_conditioning(csp, cutset):
    if not es_arbol(csp["vecinos"], set(cutset)):
        return None
    def asignar_cutset(i, asign):
        if i == len(cutset):
            resto = [v for v in csp["variables"] if v not in cutset]
            return resolver_arbol(resto, csp["dominios"], csp["vecinos"],
                                  csp["restriccion"], dict(asign))
        var = cutset[i]
        for d in csp["dominios"][var]:
            if all(csp["restriccion"](var, d, v, asign[v])
                   for v in csp["vecinos"][var] if v in asign):
                asign[var] = d
                r = asignar_cutset(i + 1, asign)
                if r is not None:
                    return r
                del asign[var]
        return None
    return asignar_cutset(0, {})


if __name__ == "__main__":
    csp = {
        "variables": ["A", "B", "C", "D"],
        "dominios": {v: ["R", "G"] for v in ["A", "B", "C", "D"]},
        "vecinos": {"A": ["B", "C"], "B": ["A", "C", "D"],
                    "C": ["A", "B"], "D": ["B"]},
        "restriccion": lambda x, vx, y, vy: vx != vy,
    }
    print("Cutset {C}:", cutset_conditioning(csp, ["C"]))
