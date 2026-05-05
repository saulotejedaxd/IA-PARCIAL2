"""
31 - Computacion Neuronal
Modelo basico de neurona artificial: combina sumas ponderadas con
una funcion de activacion. Aqui se implementa una neurona McCulloch-Pitts
y se usa para implementar AND, OR y NOT logicos.
"""


def neurona(entradas, pesos, umbral):
    s = sum(e * w for e, w in zip(entradas, pesos))
    return 1 if s >= umbral else 0


if __name__ == "__main__":
    print("AND:")
    for x in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        print(f"  {x} -> {neurona(x, [1, 1], 2)}")
    print("OR:")
    for x in [(0, 0), (0, 1), (1, 0), (1, 1)]:
        print(f"  {x} -> {neurona(x, [1, 1], 1)}")
    print("NOT:")
    for x in [0, 1]:
        print(f"  {x} -> {neurona([x], [-1], 0)}")
