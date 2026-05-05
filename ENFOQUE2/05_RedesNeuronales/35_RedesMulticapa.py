"""
35 - Redes Multicapa (MLP)
Capas ocultas con activaciones no lineales permiten resolver problemas
no linealmente separables como XOR. Aqui se construye una MLP 2-2-1
con sigmoide y se hace solo forward pass (entrenamiento en archivo 36).
"""
import math
import random


def sig(x): return 1 / (1 + math.exp(-x))


class MLP:
    def __init__(self, capas):
        self.W = [[[random.uniform(-1, 1) for _ in range(capas[i] + 1)]
                   for _ in range(capas[i + 1])]
                  for i in range(len(capas) - 1)]

    def forward(self, x):
        a = x
        for capa in self.W:
            a = [sig(neur[-1] + sum(w * v for w, v in zip(neur[:-1], a))) for neur in capa]
        return a


if __name__ == "__main__":
    mlp = MLP([2, 2, 1])
    for x in [[0, 0], [0, 1], [1, 0], [1, 1]]:
        print(f"{x} -> {round(mlp.forward(x)[0], 3)}")
