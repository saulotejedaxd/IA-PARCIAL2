"""
25 - Algoritmo EM (Expectation-Maximization)
Maximiza la verosimilitud cuando hay variables latentes.
Aqui se ajusta una mezcla de dos gaussianas 1D.
"""
import math


def gauss(x, mu, sigma2):
    return math.exp(-((x - mu) ** 2) / (2 * sigma2)) / math.sqrt(2 * math.pi * sigma2)


def em_2gauss(datos, iters=50):
    mu = [min(datos), max(datos)]
    sigma2 = [1.0, 1.0]
    pi = [0.5, 0.5]
    for _ in range(iters):
        gamma = []
        for x in datos:
            r = [pi[k] * gauss(x, mu[k], sigma2[k]) for k in range(2)]
            z = sum(r) or 1e-12
            gamma.append([v / z for v in r])
        for k in range(2):
            Nk = sum(g[k] for g in gamma) or 1e-12
            mu[k] = sum(g[k] * x for g, x in zip(gamma, datos)) / Nk
            sigma2[k] = sum(g[k] * (x - mu[k]) ** 2 for g, x in zip(gamma, datos)) / Nk + 1e-6
            pi[k] = Nk / len(datos)
    return mu, sigma2, pi


if __name__ == "__main__":
    datos = [1.0, 1.1, 0.9, 1.2, 5.0, 5.1, 4.9, 5.2, 1.05, 4.95]
    mu, s2, pi = em_2gauss(datos)
    print(f"mu={[round(m,2) for m in mu]}  sigma2={[round(s,2) for s in s2]}  pi={[round(p,2) for p in pi]}")
