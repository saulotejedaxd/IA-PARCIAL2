"""
46 - Preprocesado: Filtros
Filtros espaciales por convolucion 2D. Aqui: media (suavizado),
gaussiano (suavizado ponderado).
"""


def conv2d(img, kernel):
    h, w = len(img), len(img[0])
    kh, kw = len(kernel), len(kernel[0])
    pad_h, pad_w = kh // 2, kw // 2
    salida = [[0.0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            s = 0.0
            for u in range(kh):
                for v in range(kw):
                    ii = min(max(i + u - pad_h, 0), h - 1)
                    jj = min(max(j + v - pad_w, 0), w - 1)
                    s += img[ii][jj] * kernel[u][v]
            salida[i][j] = s
    return salida


if __name__ == "__main__":
    img = [[10, 10, 10, 10, 10],
           [10, 50, 50, 50, 10],
           [10, 50, 90, 50, 10],
           [10, 50, 50, 50, 10],
           [10, 10, 10, 10, 10]]
    media = [[1 / 9] * 3 for _ in range(3)]
    print("Media 3x3:")
    for fila in conv2d(img, media):
        print(" ", [round(v, 1) for v in fila])
    g = [[1, 2, 1], [2, 4, 2], [1, 2, 1]]
    g = [[v / 16 for v in fila] for fila in g]
    print("Gaussiano:")
    for fila in conv2d(img, g):
        print(" ", [round(v, 1) for v in fila])
