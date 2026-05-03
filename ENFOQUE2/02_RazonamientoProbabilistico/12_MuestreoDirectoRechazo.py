"""
12 - Muestreo Directo y por Rechazo
Directo: muestrea cada variable en orden topologico segun su CPT.
Por rechazo: descarta muestras que no concuerdan con la evidencia.
"""
import random


def muestreo_directo(orden, padres, cpt):
    asign = {}
    for v in orden:
        clave = tuple(asign[p] for p in padres[v])
        dist = cpt[v][clave]
        r = random.random()
        acc = 0
        for val, p in dist.items():
            acc += p
            if r < acc:
                asign[v] = val
                break
    return asign


def muestreo_rechazo(X, evidencia, orden, padres, cpt, n=10000):
    cuenta = {True: 0, False: 0}
    for _ in range(n):
        m = muestreo_directo(orden, padres, cpt)
        if all(m[v] == val for v, val in evidencia.items()):
            cuenta[m[X]] += 1
    z = sum(cuenta.values())
    return {k: (v / z if z else 0) for k, v in cuenta.items()}


if __name__ == "__main__":
    orden = ["Cloudy", "Sprinkler", "Rain", "WetGrass"]
    padres = {"Cloudy": [], "Sprinkler": ["Cloudy"], "Rain": ["Cloudy"],
              "WetGrass": ["Sprinkler", "Rain"]}
    cpt = {
        "Cloudy": {(): {True: 0.5, False: 0.5}},
        "Sprinkler": {(True,): {True: 0.1, False: 0.9},
                       (False,): {True: 0.5, False: 0.5}},
        "Rain": {(True,): {True: 0.8, False: 0.2},
                  (False,): {True: 0.2, False: 0.8}},
        "WetGrass": {(True, True): {True: 0.99, False: 0.01},
                       (True, False): {True: 0.9, False: 0.1},
                       (False, True): {True: 0.9, False: 0.1},
                       (False, False): {True: 0.01, False: 0.99}},
    }
    print("P(Rain | WetGrass=T) ~", muestreo_rechazo("Rain", {"WetGrass": True},
                                                       orden, padres, cpt))
