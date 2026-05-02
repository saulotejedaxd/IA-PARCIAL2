"""
29 - Proceso de Decision de Markov (MDP)
Tupla (S, A, P, R, gamma). Cumple la propiedad de Markov: el siguiente
estado solo depende del actual y la accion. Esta clase encapsula un
MDP simple y resuelve via Value Iteration.
"""


class MDP:
    def __init__(self, S, A, P, R, gamma=0.9):
        self.S, self.A, self.P, self.R, self.gamma = S, A, P, R, gamma

    def value_iteration(self, eps=1e-4):
        V = {s: 0.0 for s in self.S}
        while True:
            delta = 0
            for s in self.S:
                if not self.A(s):
                    continue
                v = max(
                    sum(p * (self.R(s, a, sp) + self.gamma * V[sp])
                        for sp, p in self.P(s, a).items())
                    for a in self.A(s)
                )
                delta = max(delta, abs(v - V[s]))
                V[s] = v
            if delta < eps:
                return V

    def politica_optima(self, V):
        pi = {}
        for s in self.S:
            if not self.A(s):
                continue
            pi[s] = max(self.A(s), key=lambda a:
                        sum(p * (self.R(s, a, sp) + self.gamma * V[sp])
                            for sp, p in self.P(s, a).items()))
        return pi


if __name__ == "__main__":
    S = ["calido", "frio", "T"]
    A = lambda s: [] if s == "T" else ["lento", "rapido"]
    def P(s, a):
        if s == "calido" and a == "lento":
            return {"calido": 0.5, "frio": 0.5}
        if s == "calido" and a == "rapido":
            return {"T": 0.5, "calido": 0.5}
        if s == "frio" and a == "lento":
            return {"frio": 1.0}
        if s == "frio" and a == "rapido":
            return {"T": 1.0}
    def R(s, a, sp):
        return 5 if sp == "T" else (1 if a == "lento" else 2)
    mdp = MDP(S, A, P, R)
    V = mdp.value_iteration()
    print("V*:", {k: round(v, 2) for k, v in V.items()})
    print("Pi*:", mdp.politica_optima(V))
