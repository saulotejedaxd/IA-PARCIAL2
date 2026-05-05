"""
22 - Reconocimiento del Habla
Modelo conceptual: HMM donde estados son fonemas y observaciones son
vectores acusticos. Aqui se simula clasificando palabras a partir de
secuencias de fonemas con Viterbi.
"""


def viterbi_palabras(observ_fonemas, modelos):
    mejor_palabra, mejor_p = None, -1
    for palabra, (A, B, pi) in modelos.items():
        estados = list(A.keys())
        V = {s: pi[s] * B[s].get(observ_fonemas[0], 1e-9) for s in estados}
        for o in observ_fonemas[1:]:
            Vt = {}
            for sp in estados:
                Vt[sp] = max(V[s] * A[s][sp] for s in estados) * B[sp].get(o, 1e-9)
            V = Vt
        p = max(V.values())
        if p > mejor_p:
            mejor_p, mejor_palabra = p, palabra
    return mejor_palabra, mejor_p


if __name__ == "__main__":
    A = {"s1": {"s1": 0.5, "s2": 0.5}, "s2": {"s1": 0.0, "s2": 1.0}}
    pi = {"s1": 1.0, "s2": 0.0}
    modelos = {
        "hola":  (A, {"s1": {"o": 0.8, "a": 0.2}, "s2": {"l": 0.7, "a": 0.3}}, pi),
        "casa":  (A, {"s1": {"k": 0.9, "a": 0.1}, "s2": {"a": 0.7, "s": 0.3}}, pi),
    }
    obs = ["o", "l", "a"]
    print("Reconocido:", viterbi_palabras(obs, modelos))
