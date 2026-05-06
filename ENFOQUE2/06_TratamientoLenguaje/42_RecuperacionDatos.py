"""
42 - Recuperacion de Datos (IR): TF-IDF y modelo vectorial
Indexa documentos por TF-IDF y recupera los mas similares (coseno) a
una consulta.
"""
import math
from collections import Counter


def tokenizar(texto):
    return texto.lower().split()


def tf_idf(docs):
    df = Counter()
    tfs = []
    for d in docs:
        tf = Counter(tokenizar(d))
        tfs.append(tf)
        for w in tf:
            df[w] += 1
    N = len(docs)
    idf = {w: math.log(N / df[w]) for w in df}
    return [{w: tf[w] * idf[w] for w in tf} for tf in tfs], idf


def coseno(a, b):
    com = set(a) & set(b)
    n = sum(a[w] * b[w] for w in com)
    da = math.sqrt(sum(v * v for v in a.values()))
    db = math.sqrt(sum(v * v for v in b.values()))
    return n / (da * db) if da and db else 0


def buscar(consulta, docs, vectores, idf):
    qtf = Counter(tokenizar(consulta))
    qv = {w: qtf[w] * idf.get(w, 0) for w in qtf}
    return sorted(((coseno(qv, v), i) for i, v in enumerate(vectores)), reverse=True)


if __name__ == "__main__":
    docs = ["el gato come pescado", "el perro come carne",
            "los gatos beben leche", "el pescado nada en el rio"]
    vectores, idf = tf_idf(docs)
    print("Resultados para 'gato pescado':")
    for s, i in buscar("gato pescado", docs, vectores, idf):
        print(f"  {s:.3f} -> {docs[i]}")
