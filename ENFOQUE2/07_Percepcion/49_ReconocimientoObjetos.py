"""
49 - Reconocimiento de Objetos
Clasificador basado en plantillas: compara una imagen contra prototipos
por correlacion normalizada y devuelve la clase mas similar.
"""


def correlacion(a, b):
    fa = [v for fila in a for v in fila]
    fb = [v for fila in b for v in fila]
    ma, mb = sum(fa) / len(fa), sum(fb) / len(fb)
    num = sum((x - ma) * (y - mb) for x, y in zip(fa, fb))
    da = sum((x - ma) ** 2 for x in fa) ** 0.5
    db = sum((y - mb) ** 2 for y in fb) ** 0.5
    return num / (da * db) if da and db else 0


def clasificar(img, prototipos):
    return max(prototipos, key=lambda c: correlacion(img, prototipos[c]))


if __name__ == "__main__":
    cuadrado = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    cruz = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    prototipos = {"cuadrado": cuadrado, "cruz": cruz}
    test = [[0, 1, 0], [1, 1, 1], [0, 1, 0]]
    print("Imagen reconocida como:", clasificar(test, prototipos))
