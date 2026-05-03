"""
07 - Red Bayesiana
DAG donde cada nodo X tiene una CPT P(X|padres(X)). Aqui se modela la
red clasica del libro AIMA: Burglary -> Alarm <- Earthquake -> JohnCalls,
MaryCalls, y se calcula la distribucion conjunta.
"""


class RedBayesiana:
    def __init__(self):
        self.nodos = {}

    def agregar(self, var, padres, cpt):
        self.nodos[var] = {"padres": padres, "cpt": cpt}

    def conjunta(self, asignacion):
        p = 1.0
        for v, n in self.nodos.items():
            llave = tuple(asignacion[x] for x in n["padres"])
            p *= n["cpt"][llave][asignacion[v]]
        return p


if __name__ == "__main__":
    rb = RedBayesiana()
    rb.agregar("B", [], {(): {True: 0.001, False: 0.999}})
    rb.agregar("E", [], {(): {True: 0.002, False: 0.998}})
    rb.agregar("A", ["B", "E"], {
        (True, True): {True: 0.95, False: 0.05},
        (True, False): {True: 0.94, False: 0.06},
        (False, True): {True: 0.29, False: 0.71},
        (False, False): {True: 0.001, False: 0.999},
    })
    rb.agregar("J", ["A"], {(True,): {True: 0.9, False: 0.1},
                              (False,): {True: 0.05, False: 0.95}})
    rb.agregar("M", ["A"], {(True,): {True: 0.7, False: 0.3},
                              (False,): {True: 0.01, False: 0.99}})
    a = {"B": True, "E": False, "A": True, "J": True, "M": True}
    print("P(B,!E,A,J,M) =", rb.conjunta(a))
