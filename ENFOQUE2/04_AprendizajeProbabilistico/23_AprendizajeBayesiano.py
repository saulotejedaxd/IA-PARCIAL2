"""
23 - Aprendizaje Bayesiano
Actualiza la posterior P(h|datos) ~ P(datos|h) * P(h). Aqui se estima
la probabilidad p de cara de una moneda usando una prior Beta(a, b)
y datos observados (Beta es conjugada de Bernoulli).
"""


def beta_actualizar(a, b, observaciones):
    aciertos = sum(observaciones)
    fallos = len(observaciones) - aciertos
    return a + aciertos, b + fallos


def media_beta(a, b):
    return a / (a + b)


if __name__ == "__main__":
    a, b = 2, 2
    obs = [1, 0, 1, 1, 0, 1, 1, 1]
    a2, b2 = beta_actualizar(a, b, obs)
    print(f"Prior Beta({a},{b}) media={media_beta(a, b):.3f}")
    print(f"Posterior Beta({a2},{b2}) media={media_beta(a2, b2):.3f}")
