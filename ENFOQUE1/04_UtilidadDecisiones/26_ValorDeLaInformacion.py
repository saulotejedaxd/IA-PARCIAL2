"""
26 - Valor de la Informacion (VOI)
Cuanto vale en utilidad esperada conocer una variable antes de decidir.
VPI(E) = Sum_e P(e) * MEU(decision | e=evidencia) - MEU(decision actual)
"""


def meu(acciones, prob, utilidad):
    return max(sum(p * utilidad(r, a) for r, p in prob(a).items()) for a in acciones)


def voi(acciones, prob_a_priori, prob_dado_evidencia, valores_evidencia,
        prob_evidencia, utilidad):
    base = meu(acciones, prob_a_priori, utilidad)
    esperado = 0.0
    for e in valores_evidencia:
        eu_e = meu(acciones, lambda a, ev=e: prob_dado_evidencia(a, ev), utilidad)
        esperado += prob_evidencia[e] * eu_e
    return esperado - base


if __name__ == "__main__":
    acciones = ["A", "B"]
    a_priori = lambda a: {"x": 0.5, "y": 0.5}
    util = lambda r, a: {("x", "A"): 10, ("y", "A"): 0,
                         ("x", "B"): 4, ("y", "B"): 6}[(r, a)]
    dado = lambda a, e: {"x": (1.0 if e == "x" else 0.0),
                          "y": (1.0 if e == "y" else 0.0)}
    print("VPI(estado real) =", voi(acciones, a_priori, dado, ["x", "y"],
                                     {"x": 0.5, "y": 0.5}, util))
