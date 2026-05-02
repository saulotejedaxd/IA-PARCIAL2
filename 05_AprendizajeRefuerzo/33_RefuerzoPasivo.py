"""
33 - Aprendizaje por Refuerzo Pasivo
Politica fija: el agente solo evalua V_pi(s) a partir de episodios.
Aqui se usa Monte Carlo first-visit.
"""
import random


def mc_pasivo(politica, episodios_gen, n=500, gamma=0.9):
    V = {}
    cuenta = {}
    for _ in range(n):
        ep = episodios_gen(politica)
        G = 0
        visto = set()
        for t in reversed(range(len(ep))):
            s, _, r = ep[t]
            G = gamma * G + r
            if s not in visto:
                visto.add(s)
                V[s] = V.get(s, 0.0) + (G - V.get(s, 0.0)) / (cuenta.get(s, 0) + 1)
                cuenta[s] = cuenta.get(s, 0) + 1
    return V


if __name__ == "__main__":
    estados = ["A", "B", "C", "T"]
    politica = {"A": "der", "B": "der", "C": "der"}

    def episodio(pi):
        s = "A"
        ep = []
        while s != "T":
            a = pi[s]
            sp = {"A": "B", "B": "C", "C": "T"}[s]
            r = -1 if sp != "T" else 10
            ep.append((s, a, r))
            s = sp
        return ep

    V = mc_pasivo(politica, episodio)
    print("V(pi):", {k: round(v, 3) for k, v in V.items()})
