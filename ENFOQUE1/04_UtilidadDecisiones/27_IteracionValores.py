"""
27 - Iteracion de Valores (Value Iteration)
Resuelve un MDP iterando la ecuacion de Bellman:
V*(s) = max_a Sum_s' P(s'|s,a) [R(s,a,s') + gamma * V*(s')]
hasta convergencia.
"""


def value_iteration(estados, acciones, P, R, gamma=0.9, eps=1e-4):
    V = {s: 0.0 for s in estados}
    while True:
        delta = 0
        nuevo = dict(V)
        for s in estados:
            if not acciones(s):
                continue
            nuevo[s] = max(
                sum(p * (R(s, a, sp) + gamma * V[sp]) for sp, p in P(s, a).items())
                for a in acciones(s)
            )
            delta = max(delta, abs(nuevo[s] - V[s]))
        V = nuevo
        if delta < eps:
            break
    return V


if __name__ == "__main__":
    estados = ["s1", "s2", "terminal"]
    acciones = lambda s: [] if s == "terminal" else ["a", "b"]
    def P(s, a):
        if a == "a":
            return {"s2": 0.8, "s1": 0.2}
        return {"terminal": 0.5, "s1": 0.5}
    def R(s, a, sp):
        return 10 if sp == "terminal" else -1
    V = value_iteration(estados, acciones, P, R)
    print("V* =", {k: round(v, 3) for k, v in V.items()})
