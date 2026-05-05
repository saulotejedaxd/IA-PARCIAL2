"""
14 - Monte Carlo para Cadenas de Markov (MCMC - Gibbs Sampling)
Construye una cadena cuya distribucion estacionaria es la posterior.
En cada paso resamplea una variable no-evidencia segun su CPT y la de
sus hijos (Markov Blanket).
"""
import random


def gibbs(X, evidencia, padres, hijos, cpt, n=10000):
    estado = {v: random.choice([True, False]) for v in cpt}
    estado.update(evidencia)
    no_ev = [v for v in cpt if v not in evidencia]
    cuenta = {True: 0, False: 0}
    for _ in range(n):
        for v in no_ev:
            estado[v] = muestrear_dado_mb(v, estado, padres, hijos, cpt)
        cuenta[estado[X]] += 1
    z = sum(cuenta.values())
    return {k: v / z for k, v in cuenta.items()}


def muestrear_dado_mb(v, estado, padres, hijos, cpt):
    probs = {}
    for val in [True, False]:
        e = dict(estado)
        e[v] = val
        clave = tuple(e[p] for p in padres[v])
        p = cpt[v][clave][val]
        for h in hijos.get(v, []):
            ch = tuple(e[x] for x in padres[h])
            p *= cpt[h][ch][e[h]]
        probs[val] = p
    z = sum(probs.values())
    r = random.random() * z
    return True if r < probs[True] else False


if __name__ == "__main__":
    padres = {"C": [], "S": ["C"], "R": ["C"], "W": ["S", "R"]}
    hijos = {"C": ["S", "R"], "S": ["W"], "R": ["W"], "W": []}
    cpt = {
        "C": {(): {True: 0.5, False: 0.5}},
        "S": {(True,): {True: 0.1, False: 0.9}, (False,): {True: 0.5, False: 0.5}},
        "R": {(True,): {True: 0.8, False: 0.2}, (False,): {True: 0.2, False: 0.8}},
        "W": {(True, True): {True: 0.99, False: 0.01},
              (True, False): {True: 0.9, False: 0.1},
              (False, True): {True: 0.9, False: 0.1},
              (False, False): {True: 0.01, False: 0.99}},
    }
    print("P(R | W=T) Gibbs:", gibbs("R", {"W": True}, padres, hijos, cpt, n=5000))
