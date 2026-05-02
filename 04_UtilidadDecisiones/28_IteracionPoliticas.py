"""
28 - Iteracion de Politicas (Policy Iteration)
Alterna evaluacion de politica (resolver V_pi) con mejora de politica
(eleccion greedy con respecto a V_pi). Converge en pocos pasos.
"""


def evaluar_politica(politica, estados, P, R, gamma, eps=1e-4):
    V = {s: 0.0 for s in estados}
    while True:
        delta = 0
        for s in estados:
            a = politica.get(s)
            if a is None:
                continue
            v = sum(p * (R(s, a, sp) + gamma * V[sp]) for sp, p in P(s, a).items())
            delta = max(delta, abs(v - V[s]))
            V[s] = v
        if delta < eps:
            return V


def policy_iteration(estados, acciones, P, R, gamma=0.9):
    politica = {s: (acciones(s)[0] if acciones(s) else None) for s in estados}
    while True:
        V = evaluar_politica(politica, estados, P, R, gamma)
        estable = True
        for s in estados:
            if not acciones(s):
                continue
            mejor = max(acciones(s), key=lambda a:
                        sum(p * (R(s, a, sp) + gamma * V[sp]) for sp, p in P(s, a).items()))
            if mejor != politica[s]:
                politica[s] = mejor
                estable = False
        if estable:
            return politica, V


if __name__ == "__main__":
    estados = ["s1", "s2", "T"]
    acciones = lambda s: [] if s == "T" else ["a", "b"]
    def P(s, a):
        if a == "a":
            return {"s2": 1.0}
        return {"T": 0.7, "s1": 0.3}
    def R(s, a, sp):
        return 10 if sp == "T" else -1
    pi, V = policy_iteration(estados, acciones, P, R)
    print("Politica:", pi)
    print("V:", {k: round(v, 3) for k, v in V.items()})
