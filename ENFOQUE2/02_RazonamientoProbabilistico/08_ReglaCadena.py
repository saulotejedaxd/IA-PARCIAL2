"""
08 - Regla de la Cadena
P(X1, ..., Xn) = Producto de P(Xi | X1, ..., X(i-1)).
En una red Bayesiana se simplifica a producto de P(Xi | padres(Xi)).
"""


def cadena(orden, conjuntas_marginales):
    p = 1.0
    historia = ""
    for v in orden:
        cond = conjuntas_marginales[v].get(historia, conjuntas_marginales[v][""])
        p *= cond
        historia += v
    return p


if __name__ == "__main__":
    P = {"A": {"": 0.6}, "B": {"A": 0.8, "": 0.5}, "C": {"AB": 0.3, "A": 0.4, "": 0.2}}
    print("P(A,B,C) por regla de cadena:", cadena(["A", "B", "C"], P))
