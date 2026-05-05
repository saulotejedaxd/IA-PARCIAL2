"""
24 - Naive-Bayes
Clasificador asumiendo independencia condicional de atributos dado la
clase: P(C|x) ~ P(C) * Producto P(xi|C).
"""
from collections import Counter, defaultdict


def entrenar(datos):
    clases = Counter(d[-1] for d in datos)
    total = sum(clases.values())
    prior = {c: n / total for c, n in clases.items()}
    cond = defaultdict(lambda: defaultdict(Counter))
    for d in datos:
        c = d[-1]
        for i, x in enumerate(d[:-1]):
            cond[c][i][x] += 1
    return prior, cond, clases


def predecir(x, prior, cond, clases):
    mejor, mejor_p = None, -1
    for c in prior:
        p = prior[c]
        for i, v in enumerate(x):
            p *= (cond[c][i][v] + 1) / (clases[c] + len(cond[c][i]) + 1)
        if p > mejor_p:
            mejor, mejor_p = c, p
    return mejor


if __name__ == "__main__":
    datos = [
        ("sol", "calor", "no"), ("sol", "calor", "no"),
        ("nub", "calor", "si"), ("lluvia", "templ", "si"),
        ("lluvia", "frio", "si"), ("lluvia", "frio", "no"),
        ("nub", "frio", "si"), ("sol", "templ", "no"),
    ]
    pr, co, cl = entrenar(datos)
    print("Prediccion (sol, frio):", predecir(("sol", "frio"), pr, co, cl))
    print("Prediccion (nub, templ):", predecir(("nub", "templ"), pr, co, cl))
