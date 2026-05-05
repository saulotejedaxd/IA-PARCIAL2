"""
28 - k-NN, k-Medias y Clustering
k-NN: asigna la clase mayoritaria entre los k vecinos mas cercanos.
k-Medias: itera entre asignar puntos al centroide mas cercano y
recalcular centroides como media del cluster.
"""
import math
import random
from collections import Counter


def dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def knn(query, datos, k=3):
    cercanos = sorted(datos, key=lambda d: dist(query, d[0]))[:k]
    return Counter(c for _, c in cercanos).most_common(1)[0][0]


def k_medias(puntos, k, iters=20):
    centros = random.sample(puntos, k)
    for _ in range(iters):
        clusters = [[] for _ in range(k)]
        for p in puntos:
            i = min(range(k), key=lambda i: dist(p, centros[i]))
            clusters[i].append(p)
        nuevos = []
        for c in clusters:
            if c:
                nuevos.append(tuple(sum(x) / len(c) for x in zip(*c)))
            else:
                nuevos.append(random.choice(puntos))
        if nuevos == centros:
            break
        centros = nuevos
    return centros, clusters


if __name__ == "__main__":
    datos = [((1, 1), "A"), ((1, 2), "A"), ((2, 1), "A"),
             ((8, 8), "B"), ((9, 9), "B"), ((8, 9), "B")]
    print("kNN (5,5):", knn((5, 5), datos, k=3))
    pts = [d[0] for d in datos]
    centros, _ = k_medias(pts, 2)
    print("Centros k-medias:", [tuple(round(x, 2) for x in c) for c in centros])
