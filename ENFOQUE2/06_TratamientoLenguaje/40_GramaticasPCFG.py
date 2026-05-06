"""
40 - Gramaticas Probabilisticas Independientes del Contexto (PCFG)
Cada regla A -> B C tiene una probabilidad. La probabilidad de un
arbol es el producto de las reglas usadas. Aqui se calcula el arbol
mas probable de una oracion con un CYK probabilistico simple.
"""


def cyk_pcfg(oracion, reglas_term, reglas_bin):
    n = len(oracion)
    tabla = [[{} for _ in range(n)] for _ in range(n)]
    for i, w in enumerate(oracion):
        for A, p in reglas_term.get(w, {}).items():
            tabla[i][i][A] = p
    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            for k in range(i, j):
                for A, prods in reglas_bin.items():
                    for (B, C), p in prods.items():
                        if B in tabla[i][k] and C in tabla[k + 1][j]:
                            q = p * tabla[i][k][B] * tabla[k + 1][j][C]
                            if q > tabla[i][j].get(A, 0):
                                tabla[i][j][A] = q
    return tabla[0][n - 1]


if __name__ == "__main__":
    term = {"el": {"DT": 1.0}, "gato": {"N": 1.0}, "duerme": {"V": 1.0}}
    bin_r = {"NP": {("DT", "N"): 1.0},
             "S": {("NP", "V"): 1.0}}
    print("Top:", cyk_pcfg(["el", "gato", "duerme"], term, bin_r))
