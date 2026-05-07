"""
47 - Deteccion de Aristas y Segmentacion
Filtro Sobel para gradiente y umbralizacion para segmentar.
"""


def conv2d(img, k):
    h, w = len(img), len(img[0])
    kh, kw = len(k), len(k[0])
    ph, pw = kh // 2, kw // 2
    out = [[0.0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            s = 0.0
            for u in range(kh):
                for v in range(kw):
                    ii = min(max(i + u - ph, 0), h - 1)
                    jj = min(max(j + v - pw, 0), w - 1)
                    s += img[ii][jj] * k[u][v]
            out[i][j] = s
    return out


def magnitud(gx, gy):
    return [[(gx[i][j] ** 2 + gy[i][j] ** 2) ** 0.5
             for j in range(len(gx[0]))] for i in range(len(gx))]


def umbralizar(img, T):
    return [[1 if v > T else 0 for v in fila] for fila in img]


if __name__ == "__main__":
    img = [[0, 0, 0, 0, 0, 0],
           [0, 0, 0, 9, 9, 9],
           [0, 0, 0, 9, 9, 9],
           [0, 0, 0, 9, 9, 9],
           [0, 0, 0, 9, 9, 9],
           [0, 0, 0, 0, 0, 0]]
    sx = [[-1, 0, 1], [-2, 0, 2], [-1, 0, 1]]
    sy = [[-1, -2, -1], [0, 0, 0], [1, 2, 1]]
    M = magnitud(conv2d(img, sx), conv2d(img, sy))
    print("Mapa de aristas (umbral 5):")
    for fila in umbralizar(M, 5):
        print(" ", fila)
