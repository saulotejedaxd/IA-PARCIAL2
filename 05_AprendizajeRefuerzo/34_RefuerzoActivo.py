"""
34 - Aprendizaje por Refuerzo Activo (SARSA on-policy)
El agente decide acciones y aprende V/Q. SARSA actualiza con la accion
realmente tomada bajo su politica epsilon-greedy.
"""
import random


def sarsa(estados, acciones, paso, episodios=500, alpha=0.1, gamma=0.9, eps=0.1):
    Q = {(s, a): 0.0 for s in estados for a in acciones(s)}
    for _ in range(episodios):
        s = random.choice([e for e in estados if acciones(e)])
        a = elegir(Q, s, acciones, eps)
        while acciones(s):
            sp, r, fin = paso(s, a)
            ap = elegir(Q, sp, acciones, eps) if acciones(sp) else None
            target = r + (0 if ap is None else gamma * Q[(sp, ap)])
            Q[(s, a)] += alpha * (target - Q[(s, a)])
            if fin:
                break
            s, a = sp, ap
    return Q


def elegir(Q, s, acciones, eps):
    if random.random() < eps or not acciones(s):
        return random.choice(acciones(s)) if acciones(s) else None
    return max(acciones(s), key=lambda a: Q[(s, a)])


if __name__ == "__main__":
    estados = [0, 1, 2, 3]
    acciones = lambda s: [] if s == 3 else ["der"]
    def paso(s, a):
        sp = s + 1
        return sp, (10 if sp == 3 else -1), sp == 3
    Q = sarsa(estados, acciones, paso, episodios=200)
    print("Q SARSA:", {k: round(v, 2) for k, v in Q.items()})
