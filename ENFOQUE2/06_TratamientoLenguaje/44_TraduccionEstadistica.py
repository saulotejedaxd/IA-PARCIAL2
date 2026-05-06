"""
44 - Traduccion Automatica Estadistica
Modelo IBM-1 simplificado: estima P(palabra_destino | palabra_origen)
usando EM sobre un corpus paralelo y traduce palabra por palabra.
"""
from collections import defaultdict


def ibm1(corpus, iters=20):
    src_vocab = {w for s, _ in corpus for w in s}
    dst_vocab = {w for _, t in corpus for w in t}
    t = {(d, s): 1 / len(src_vocab) for d in dst_vocab for s in src_vocab}
    for _ in range(iters):
        c = defaultdict(float)
        total = defaultdict(float)
        for src, dst in corpus:
            for d in dst:
                z = sum(t[(d, s)] for s in src)
                for s in src:
                    delta = t[(d, s)] / z
                    c[(d, s)] += delta
                    total[s] += delta
        for (d, s) in t:
            t[(d, s)] = c[(d, s)] / total[s] if total[s] else 0
    return t


def traducir(palabra_src, t, dst_vocab):
    return max(dst_vocab, key=lambda d: t.get((d, palabra_src), 0))


if __name__ == "__main__":
    corpus = [
        (["la", "casa"], ["the", "house"]),
        (["la", "flor"], ["the", "flower"]),
        (["casa", "blanca"], ["white", "house"]),
    ]
    t = ibm1(corpus, iters=30)
    dst = {w for _, d in corpus for w in d}
    for w in ["la", "casa", "flor", "blanca"]:
        print(f"{w} -> {traducir(w, t, dst)}")
