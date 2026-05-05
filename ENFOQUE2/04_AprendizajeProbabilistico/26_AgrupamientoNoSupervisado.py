"""
26 - Agrupamiento No Supervisado (Clustering Jerarquico Aglomerativo)
Empieza con cada punto en su cluster y fusiona iterativamente los dos
mas cercanos (single linkage).
"""
import math


def dist(a, b):
    return math.sqrt(sum((x - y) ** 2 for x, y in zip(a, b)))


def aglomerativo(puntos, k):
    clusters = [[p] for p in puntos]
    while len(clusters) > k:
        mejor = (float("inf"), 0, 1)
        for i in range(len(clusters)):
            for j in range(i + 1, len(clusters)):
                d = min(dist(p, q) for p in clusters[i] for q in clusters[j])
                if d < mejor[0]:
                    mejor = (d, i, j)
        _, i, j = mejor
        clusters[i] = clusters[i] + clusters[j]
        del clusters[j]
    return clusters


if __name__ == "__main__":
    pts = [(0, 0), (0, 1), (1, 0), (10, 10), (10, 11), (11, 10)]
    print("Clusters:", aglomerativo(pts, 2))
