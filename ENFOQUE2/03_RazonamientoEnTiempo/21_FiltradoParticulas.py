"""
21 - Red Bayesiana Dinamica: Filtrado de Particulas
Aproxima la creencia con N particulas (muestras). En cada paso:
1) propaga cada particula segun el modelo de transicion,
2) pondera por la verosimilitud de la observacion,
3) re-muestrea con reemplazo segun los pesos.
"""
import random


def transicion(s):
    return s if random.random() < 0.7 else (1 - s)


def sensor(s, o):
    if s == 1:
        return 0.9 if o == "u" else 0.1
    return 0.2 if o == "u" else 0.8


def filtro_particulas(observaciones, N=1000):
    particulas = [random.randint(0, 1) for _ in range(N)]
    for o in observaciones:
        particulas = [transicion(p) for p in particulas]
        pesos = [sensor(p, o) for p in particulas]
        z = sum(pesos)
        pesos = [w / z for w in pesos]
        particulas = random.choices(particulas, weights=pesos, k=N)
    return sum(particulas) / N


if __name__ == "__main__":
    p_lluvia = filtro_particulas(["u", "u", "n", "u"])
    print(f"P(lluvia | u,u,n,u) ~ {p_lluvia:.3f}")
