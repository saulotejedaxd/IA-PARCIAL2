"""
52 - Movimiento (Flujo Optico por diferencia)
Estima el desplazamiento entre dos frames buscando el bloque que mejor
coincide en el frame siguiente (block matching).
"""


def sad(a, b):
    return sum(abs(a[i][j] - b[i][j]) for i in range(len(a)) for j in range(len(a[0])))


def flujo_optico(f1, f2, x, y, tam=3, busqueda=2):
    h, w = len(f1), len(f1[0])
    bloque = [fila[x:x + tam] for fila in f1[y:y + tam]]
    mejor = (float("inf"), 0, 0)
    for dy in range(-busqueda, busqueda + 1):
        for dx in range(-busqueda, busqueda + 1):
            ny, nx = y + dy, x + dx
            if 0 <= ny <= h - tam and 0 <= nx <= w - tam:
                cand = [fila[nx:nx + tam] for fila in f2[ny:ny + tam]]
                d = sad(bloque, cand)
                if d < mejor[0]:
                    mejor = (d, dx, dy)
    return mejor[1], mejor[2]


if __name__ == "__main__":
    f1 = [[0]*8 for _ in range(8)]
    f1[3][3] = f1[3][4] = f1[4][3] = f1[4][4] = 9
    f2 = [[0]*8 for _ in range(8)]
    f2[3][5] = f2[3][6] = f2[4][5] = f2[4][6] = 9
    dx, dy = flujo_optico(f1, f2, 3, 3, tam=2, busqueda=3)
    print(f"Desplazamiento estimado: dx={dx}, dy={dy}")
