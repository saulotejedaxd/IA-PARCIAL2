"""
13 - Ponderacion de Verosimilitud (Likelihood Weighting)
Genera muestras fijando la evidencia y pondera cada muestra por la
verosimilitud de la evidencia bajo sus padres muestreados.
"""
import random


def ponderacion(X, evidencia, orden, padres, cpt, n=10000):
    cuenta = {True: 0.0, False: 0.0}
    for _ in range(n):
        asign = {}
        peso = 1.0
        for v in orden:
            clave = tuple(asign[p] for p in padres[v])
            dist = cpt[v][clave]
            if v in evidencia:
                asign[v] = evidencia[v]
                peso *= dist[evidencia[v]]
            else:
                r = random.random()
                acc = 0
                for val, p in dist.items():
                    acc += p
                    if r < acc:
                        asign[v] = val
                        break
        cuenta[asign[X]] += peso
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
    print("P(Rain | WetGrass=T) ~", ponderacion("Rain", {"WetGrass": True},
                                                  orden, padres, cpt))
