"""
35 - Q-Learning (off-policy)
Aprende Q*(s,a) sin importar la politica de exploracion:
Q(s,a) <- Q(s,a) + alpha [r + gamma max_a' Q(s', a') - Q(s,a)]
"""
import random


def q_learning(estados, acciones, paso, episodios=500, alpha=0.1, gamma=0.9, eps=0.2):
    Q = {(s, a): 0.0 for s in estados for a in acciones(s)}
    for _ in range(episodios):
        s = random.choice([e for e in estados if acciones(e)])
        while acciones(s):
            if random.random() < eps:
                a = random.choice(acciones(s))
            else:
                a = max(acciones(s), key=lambda a: Q[(s, a)])
            sp, r, fin = paso(s, a)
            max_q = max((Q[(sp, ap)] for ap in acciones(sp)), default=0.0)
            Q[(s, a)] += alpha * (r + gamma * max_q - Q[(s, a)])
            if fin:
                break
            s = sp
    return Q


if __name__ == "__main__":
    estados = [0, 1, 2, 3]
    acciones = lambda s: [] if s == 3 else ["izq", "der"]
    def paso(s, a):
        sp = max(0, s - 1) if a == "izq" else min(3, s + 1)
        return sp, (10 if sp == 3 else -1), sp == 3
    Q = q_learning(estados, acciones, paso, episodios=500)
    politica = {s: max(acciones(s), key=lambda a: Q[(s, a)])
                for s in estados if acciones(s)}
    print("Politica greedy:", politica)
