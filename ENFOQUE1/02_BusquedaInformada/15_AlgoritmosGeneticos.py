"""
15 - Algoritmos Geneticos
Optimizacion inspirada en evolucion biologica: poblacion -> seleccion ->
cruce -> mutacion. Aqui se maximiza la suma de bits (One-Max).
"""
import random


def fitness(ind):
    return sum(ind)


def seleccion(pob, k=3):
    return max(random.sample(pob, k), key=fitness)


def cruce(p1, p2):
    c = random.randint(1, len(p1) - 1)
    return p1[:c] + p2[c:]


def mutar(ind, p=0.05):
    return [bit ^ (random.random() < p) for bit in ind]


def algoritmo_genetico(n_bits=20, pop=40, gens=100):
    poblacion = [[random.randint(0, 1) for _ in range(n_bits)] for _ in range(pop)]
    for _ in range(gens):
        nueva = []
        for _ in range(pop):
            p1, p2 = seleccion(poblacion), seleccion(poblacion)
            hijo = mutar(cruce(p1, p2))
            nueva.append(hijo)
        poblacion = nueva
    mejor = max(poblacion, key=fitness)
    return mejor, fitness(mejor)


if __name__ == "__main__":
    sol, val = algoritmo_genetico()
    print(f"Mejor individuo: {sol}  Fitness: {val}")
