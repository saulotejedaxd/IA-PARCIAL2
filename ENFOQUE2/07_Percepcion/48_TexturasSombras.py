"""
48 - Texturas y Sombras
Caracterizacion de texturas via energia local (varianza en ventana) e
iluminacion (gradiente). Calculo simple sobre una imagen sintetica.
"""


def varianza_local(img, win=3):
    h, w = len(img), len(img[0])
    p = win // 2
    out = [[0.0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            vals = []
            for u in range(-p, p + 1):
                for v in range(-p, p + 1):
                    ii = min(max(i + u, 0), h - 1)
                    jj = min(max(j + v, 0), w - 1)
                    vals.append(img[ii][jj])
            m = sum(vals) / len(vals)
            out[i][j] = sum((x - m) ** 2 for x in vals) / len(vals)
    return out


if __name__ == "__main__":
    textura = [[(i + j) % 2 * 9 for j in range(6)] for i in range(6)]
    plana = [[5] * 6 for _ in range(6)]
    print("Varianza textura (esperado alto):", round(varianza_local(textura)[2][2], 2))
    print("Varianza plana (esperado bajo):", round(varianza_local(plana)[2][2], 2))
