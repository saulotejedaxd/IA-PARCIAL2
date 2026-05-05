"""
05 - Independencia Condicional
A es condicionalmente independiente de B dado C si
P(A,B|C) = P(A|C) * P(B|C). Aqui se prueba numericamente.
"""


def es_independiente_condicional(P_ABC, A, B, C, eps=1e-6):
    P_C = sum(p for (a, b, c), p in P_ABC.items() if c == C)
    if P_C == 0:
        return True
    P_AC = sum(p for (a, b, c), p in P_ABC.items() if a == A and c == C) / P_C
    P_BC = sum(p for (a, b, c), p in P_ABC.items() if b == B and c == C) / P_C
    P_ABCc = P_ABC.get((A, B, C), 0) / P_C
    return abs(P_ABCc - P_AC * P_BC) < eps


if __name__ == "__main__":
    P = {("a1", "b1", "c1"): 0.06, ("a1", "b2", "c1"): 0.04,
         ("a2", "b1", "c1"): 0.24, ("a2", "b2", "c1"): 0.16,
         ("a1", "b1", "c2"): 0.18, ("a1", "b2", "c2"): 0.12,
         ("a2", "b1", "c2"): 0.12, ("a2", "b2", "c2"): 0.08}
    print("A=a1, B=b1 son CI dado C=c1:",
          es_independiente_condicional(P, "a1", "b1", "c1"))
