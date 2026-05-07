"""
45 - Graficos por Computador
Sintesis de imagenes: aqui se dibuja una imagen 2D simple en una matriz
y se rasterizan lineas con el algoritmo de Bresenham.
"""


def crear_canvas(w, h):
    return [[" "] * w for _ in range(h)]


def linea_bresenham(canvas, x0, y0, x1, y1, c="*"):
    dx, dy = abs(x1 - x0), abs(y1 - y0)
    sx, sy = (1 if x0 < x1 else -1), (1 if y0 < y1 else -1)
    err = dx - dy
    while True:
        if 0 <= y0 < len(canvas) and 0 <= x0 < len(canvas[0]):
            canvas[y0][x0] = c
        if x0 == x1 and y0 == y1:
            break
        e2 = 2 * err
        if e2 > -dy:
            err -= dy
            x0 += sx
        if e2 < dx:
            err += dx
            y0 += sy


def imprimir(canvas):
    for fila in canvas:
        print("".join(fila))


if __name__ == "__main__":
    c = crear_canvas(20, 8)
    linea_bresenham(c, 0, 0, 19, 7)
    linea_bresenham(c, 0, 7, 19, 0)
    imprimir(c)
