"""
39 - Modelo Probabilistico del Lenguaje: Corpus
Modelo n-grama: estima P(w_i | w_{i-n+1:i-1}) por conteo de frecuencias
en un corpus. Aqui se entrena un bigrama y se calcula la probabilidad
de una oracion.
"""
from collections import Counter, defaultdict


def entrenar_bigrama(corpus):
    uni = Counter()
    bi = defaultdict(Counter)
    for oracion in corpus:
        toks = ["<s>"] + oracion.split() + ["</s>"]
        for i in range(len(toks) - 1):
            uni[toks[i]] += 1
            bi[toks[i]][toks[i + 1]] += 1
    return uni, bi


def prob_oracion(oracion, uni, bi):
    toks = ["<s>"] + oracion.split() + ["</s>"]
    p = 1.0
    for i in range(len(toks) - 1):
        v = bi[toks[i]].get(toks[i + 1], 0)
        d = uni[toks[i]] or 1
        p *= (v + 1) / (d + len(uni))
    return p


if __name__ == "__main__":
    corpus = ["el gato come pescado", "el perro come carne", "el gato duerme"]
    uni, bi = entrenar_bigrama(corpus)
    print("P('el gato come') =", prob_oracion("el gato come", uni, bi))
    print("P('el pescado duerme') =", prob_oracion("el pescado duerme", uni, bi))
