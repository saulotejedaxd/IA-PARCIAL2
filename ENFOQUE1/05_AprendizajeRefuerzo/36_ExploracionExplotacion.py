"""
36 - Exploracion vs Explotacion
Dilema clasico: explotar la mejor opcion conocida o explorar otras.
Aqui se comparan epsilon-greedy y UCB1 en un bandido multi-brazo.
"""
import math
import random


def epsilon_greedy(brazos, eps=0.1, T=1000):
    Q = [0.0] * len(brazos)
    n = [0] * len(brazos)
    total = 0
    for _ in range(T):
        a = random.randrange(len(brazos)) if random.random() < eps else max(range(len(brazos)), key=lambda i: Q[i])
        r = brazos[a]()
        n[a] += 1
        Q[a] += (r - Q[a]) / n[a]
        total += r
    return total, Q


def ucb1(brazos, T=1000):
    Q = [0.0] * len(brazos)
    n = [0] * len(brazos)
    total = 0
    for t in range(1, T + 1):
        if 0 in n:
            a = n.index(0)
        else:
            a = max(range(len(brazos)),
                    key=lambda i: Q[i] + math.sqrt(2 * math.log(t) / n[i]))
        r = brazos[a]()
        n[a] += 1
        Q[a] += (r - Q[a]) / n[a]
        total += r
    return total, Q


if __name__ == "__main__":
    medias = [0.2, 0.5, 0.7, 0.3]
    brazos = [(lambda m=m: 1 if random.random() < m else 0) for m in medias]
    print("eps-greedy:", epsilon_greedy(brazos))
    print("UCB1:", ucb1(brazos))
