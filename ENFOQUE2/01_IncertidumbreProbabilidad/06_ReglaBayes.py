"""
06 - Regla de Bayes
P(H|E) = P(E|H) * P(H) / P(E). Pilar del razonamiento probabilistico:
actualizar creencias a partir de nueva evidencia.
"""


def bayes(prior, verosimilitud, evidencia):
    posterior = {}
    for h, ph in prior.items():
        posterior[h] = ph * verosimilitud[h][evidencia]
    z = sum(posterior.values())
    return {h: p / z for h, p in posterior.items()}


if __name__ == "__main__":
    prior = {"enfermo": 0.01, "sano": 0.99}
    verosimilitud = {"enfermo": {"+": 0.99, "-": 0.01},
                     "sano": {"+": 0.05, "-": 0.95}}
    print("Prior P(H):", prior)
    print("Posterior tras test +:", bayes(prior, verosimilitud, "+"))
