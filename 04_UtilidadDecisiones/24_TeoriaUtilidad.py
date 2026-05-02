"""
24 - Teoria de la Utilidad: Funcion de Utilidad
Modela las preferencias del agente. La utilidad esperada de una accion
es la suma ponderada de las utilidades de sus posibles resultados:
EU(a) = Sum_s P(s|a) * U(s).
Aqui se decide entre dos loterias.
"""


def utilidad_esperada(loteria, U):
    return sum(p * U[r] for p, r in loteria)


if __name__ == "__main__":
    U = {"gano": 100, "empate": 0, "pierdo": -50}
    A = [(0.7, "gano"), (0.2, "empate"), (0.1, "pierdo")]
    B = [(0.4, "gano"), (0.5, "empate"), (0.1, "pierdo")]
    print("EU(A) =", utilidad_esperada(A, U))
    print("EU(B) =", utilidad_esperada(B, U))
    print("Eleccion:", "A" if utilidad_esperada(A, U) > utilidad_esperada(B, U) else "B")
