"""
03 - Probabilidad Condicionada y Normalizacion
P(A|B) = P(A,B) / P(B). Para que una distribucion sume 1 se normaliza
dividiendo por la suma. Aqui se usan ambas operaciones.
"""


def condicional(conjunta, b_val):
    sub = {a: p for (a, b), p in conjunta.items() if b == b_val}
    z = sum(sub.values())
    return {a: p / z for a, p in sub.items()}


if __name__ == "__main__":
    conjunta = {("si", "lluvia"): 0.20, ("no", "lluvia"): 0.05,
                ("si", "sol"): 0.10, ("no", "sol"): 0.65}
    print("P(paraguas | lluvia):", condicional(conjunta, "lluvia"))
    print("P(paraguas | sol):", condicional(conjunta, "sol"))
