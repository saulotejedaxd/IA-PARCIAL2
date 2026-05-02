"""
32 - Teoria de Juegos: Equilibrios y Mecanismos
Equilibrio de Nash: ningun jugador puede mejorar cambiando su estrategia
unilateralmente. Aqui se buscan equilibrios en estrategias puras para
un juego bimatricial 2x2 (clasico Dilema del Prisionero).
"""


def equilibrios_nash(matriz_A, matriz_B, acciones1, acciones2):
    eq = []
    for i, a in enumerate(acciones1):
        for j, b in enumerate(acciones2):
            mejor1 = all(matriz_A[i][j] >= matriz_A[k][j] for k in range(len(acciones1)))
            mejor2 = all(matriz_B[i][j] >= matriz_B[i][k] for k in range(len(acciones2)))
            if mejor1 and mejor2:
                eq.append((a, b, matriz_A[i][j], matriz_B[i][j]))
    return eq


if __name__ == "__main__":
    A = [[-1, -3], [0, -2]]
    B = [[-1, 0], [-3, -2]]
    acciones = ["callar", "delatar"]
    eq = equilibrios_nash(A, B, acciones, acciones)
    print("Equilibrios de Nash en Dilema del Prisionero:")
    for e in eq:
        print(f"  J1={e[0]}, J2={e[1]}  pagos=({e[2]}, {e[3]})")
