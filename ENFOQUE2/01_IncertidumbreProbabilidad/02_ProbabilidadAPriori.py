"""
02 - Probabilidad a Priori (P(X))
Probabilidad de un evento sin condicionar en evidencia. Aqui se calcula
a partir de una tabla de frecuencias.
"""


def a_priori(tabla):
    total = sum(tabla.values())
    return {k: v / total for k, v in tabla.items()}


if __name__ == "__main__":
    clima = {"sol": 70, "nublado": 20, "lluvia": 10}
    print("P(clima):", a_priori(clima))
