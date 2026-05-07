"""
51 - Etiquetado de Lineas (Huffman-Clowes / Waltz)
En vision 3D se etiquetan aristas de un dibujo como convexas (+),
concavas (-) u ocluyentes (->) usando un catalogo de uniones validas.
Aqui un enfoque simplificado por restricciones para un cubo.
"""


CATALOGO_UNION_L = [("+", "+"), ("-", "-"), ("->", "+"), ("+", "->")]
CATALOGO_UNION_Y = [("+", "+", "+"), ("-", "-", "-")]


def es_consistente(union, etiquetas, tipo):
    cat = CATALOGO_UNION_L if tipo == "L" else CATALOGO_UNION_Y
    return tuple(etiquetas[a] for a in union) in cat or \
           tuple(reversed([etiquetas[a] for a in union])) in cat


if __name__ == "__main__":
    etiquetas = {"a1": "+", "a2": "+", "a3": "+", "a4": "->"}
    print("L (a1,a2):", es_consistente(("a1", "a2"), etiquetas, "L"))
    print("L (a1,a4):", es_consistente(("a1", "a4"), etiquetas, "L"))
    print("Y (a1,a2,a3):", es_consistente(("a1", "a2", "a3"), etiquetas, "Y"))
