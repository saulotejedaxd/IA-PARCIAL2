"""
11 - Eliminacion de Variables
Mejora la enumeracion al reusar calculos via factores. Los factores se
multiplican y las variables ocultas se suman (marginalizan) cuando
ya no aparecen en mas factores.
"""


def multiplicar(f1, f2):
    nuevo = {}
    vars2 = f2["vars"]
    vars_comunes = [v for v in f1["vars"] if v in vars2]
    nuevas = list(dict.fromkeys(f1["vars"] + vars2))
    for k1, p1 in f1["tabla"].items():
        d1 = dict(zip(f1["vars"], k1))
        for k2, p2 in f2["tabla"].items():
            d2 = dict(zip(vars2, k2))
            if all(d1[v] == d2[v] for v in vars_comunes):
                d = {**d1, **d2}
                nuevo[tuple(d[v] for v in nuevas)] = p1 * p2
    return {"vars": nuevas, "tabla": nuevo}


def sumar_var(f, var):
    idx = f["vars"].index(var)
    nuevas = [v for v in f["vars"] if v != var]
    nuevo = {}
    for k, p in f["tabla"].items():
        nk = tuple(v for i, v in enumerate(k) if i != idx)
        nuevo[nk] = nuevo.get(nk, 0) + p
    return {"vars": nuevas, "tabla": nuevo}


def normalizar(f):
    z = sum(f["tabla"].values())
    return {k: v / z for k, v in f["tabla"].items()}


if __name__ == "__main__":
    fA = {"vars": ["A"], "tabla": {(True,): 0.6, (False,): 0.4}}
    fBA = {"vars": ["B", "A"], "tabla": {(True, True): 0.8, (False, True): 0.2,
                                            (True, False): 0.3, (False, False): 0.7}}
    f = multiplicar(fA, fBA)
    f = sumar_var(f, "A")
    print("P(B):", normalizar(f))
