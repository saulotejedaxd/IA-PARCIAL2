"""
16 - Busqueda Online (LRTA*)
El agente solo conoce el entorno conforme actua. Aqui se implementa
Learning Real-Time A*: actualiza la heuristica H con la experiencia
y elige siempre el vecino con menor c(s,a,s')+H(s').
"""


def lrta_star(estado, meta, sucesores_de, costo, H, max_pasos=200):
    s = estado
    pasos = 0
    while s != meta and pasos < max_pasos:
        sucs = sucesores_de(s)
        if not sucs:
            return None
        a = min(sucs, key=lambda sp: costo(s, sp) + H.get(sp, 0))
        H[s] = max(H.get(s, 0), costo(s, a) + H.get(a, 0))
        s = a
        pasos += 1
    return s, pasos, H


if __name__ == "__main__":
    grafo = {1: [2, 3], 2: [1, 4], 3: [1, 4], 4: [2, 3, 5], 5: [4]}
    sucesores = lambda s: grafo.get(s, [])
    costo = lambda a, b: 1
    H = {1: 4, 2: 3, 3: 3, 4: 1, 5: 0}
    print("LRTA* desde 1 a 5:", lrta_star(1, 5, sucesores, costo, H))
