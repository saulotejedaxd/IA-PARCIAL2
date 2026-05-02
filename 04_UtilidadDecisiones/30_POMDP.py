"""
30 - MDP Parcialmente Observable (POMDP)
El agente no observa el estado real; mantiene una creencia (distribucion
de probabilidad sobre estados) que actualiza tras cada accion y observacion.
Aqui se muestra la actualizacion de creencia (belief update).
"""


def actualizar_creencia(b, a, o, T, O, S):
    nuevo = {}
    for sp in S:
        suma = sum(T(s, a, sp) * b[s] for s in S)
        nuevo[sp] = O(sp, a, o) * suma
    z = sum(nuevo.values())
    if z == 0:
        return b
    return {s: p / z for s, p in nuevo.items()}


if __name__ == "__main__":
    S = ["sano", "enfermo"]
    b0 = {"sano": 0.7, "enfermo": 0.3}
    def T(s, a, sp):
        return {"sano": {"sano": 0.9, "enfermo": 0.1},
                "enfermo": {"sano": 0.4, "enfermo": 0.6}}[s][sp]
    def O(s, a, o):
        return {"sano": {"+": 0.2, "-": 0.8},
                "enfermo": {"+": 0.9, "-": 0.1}}[s][o]
    print("Creencia inicial:", b0)
    b1 = actualizar_creencia(b0, "examen", "+", T, O, S)
    print("Tras observar +:", {k: round(v, 3) for k, v in b1.items()})
