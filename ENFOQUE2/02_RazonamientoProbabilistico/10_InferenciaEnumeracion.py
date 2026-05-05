"""
10 - Inferencia por Enumeracion
P(X | e) = alpha * Sum_y P(X, e, y) sumando sobre variables ocultas.
Costo exponencial pero exacto. Aqui sobre la red Burglary/Alarm.
"""
import itertools


CPT = {
    "B": [(), {True: 0.001, False: 0.999}],
    "E": [(), {True: 0.002, False: 0.998}],
    "A": [("B", "E"), {
        (True, True): {True: 0.95, False: 0.05},
        (True, False): {True: 0.94, False: 0.06},
        (False, True): {True: 0.29, False: 0.71},
        (False, False): {True: 0.001, False: 0.999}}],
    "J": [("A",), {(True,): {True: 0.9, False: 0.1},
                    (False,): {True: 0.05, False: 0.95}}],
    "M": [("A",), {(True,): {True: 0.7, False: 0.3},
                    (False,): {True: 0.01, False: 0.99}}],
}


def conjunta(asign):
    p = 1.0
    for v, (padres, tabla) in CPT.items():
        if not padres:
            p *= tabla[asign[v]]
        else:
            p *= tabla[tuple(asign[x] for x in padres)][asign[v]]
    return p


def enumerar(X, evidencia):
    ocultas = [v for v in CPT if v != X and v not in evidencia]
    Q = {True: 0.0, False: 0.0}
    for x in [True, False]:
        for vals in itertools.product([True, False], repeat=len(ocultas)):
            asign = dict(evidencia)
            asign[X] = x
            asign.update(dict(zip(ocultas, vals)))
            Q[x] += conjunta(asign)
    z = sum(Q.values())
    return {k: v / z for k, v in Q.items()}


if __name__ == "__main__":
    print("P(B | J=T, M=T):", enumerar("B", {"J": True, "M": True}))
