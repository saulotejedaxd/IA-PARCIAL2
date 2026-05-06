"""
41 - Gramaticas Probabilisticas Lexicalizadas
Cada constituyente lleva un cabezal lexico (head). Permiten capturar
preferencias semantico-estadisticas (e.g. P(NP -> Det N | head=gato)).
"""


def prob_regla_lexicalizada(regla, head, tabla):
    return tabla.get((regla, head), tabla.get((regla, "*"), 0.0))


if __name__ == "__main__":
    tabla = {
        (("NP", "DT", "N"), "gato"): 0.7,
        (("NP", "DT", "N"), "perro"): 0.6,
        (("NP", "DT", "N"), "*"): 0.5,
        (("VP", "V", "NP"), "comer"): 0.8,
    }
    print("P(NP->DT N | gato):", prob_regla_lexicalizada(("NP", "DT", "N"), "gato", tabla))
    print("P(NP->DT N | leon):", prob_regla_lexicalizada(("NP", "DT", "N"), "leon", tabla))
    print("P(VP->V NP | comer):", prob_regla_lexicalizada(("VP", "V", "NP"), "comer", tabla))
