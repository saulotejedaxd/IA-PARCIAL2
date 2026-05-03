"""
09 - Manto de Markov (Markov Blanket)
El Manto de Markov de un nodo X en una red Bayesiana son: sus padres,
sus hijos y los padres de sus hijos. X es independiente del resto de
la red dado su manto.
"""


def manto_markov(nodo, padres, hijos):
    manto = set(padres.get(nodo, []))
    for h in hijos.get(nodo, []):
        manto.add(h)
        manto.update(padres.get(h, []))
    manto.discard(nodo)
    return manto


if __name__ == "__main__":
    padres = {"A": [], "B": ["A"], "C": ["A"], "D": ["B", "C"], "E": ["D"]}
    hijos = {"A": ["B", "C"], "B": ["D"], "C": ["D"], "D": ["E"], "E": []}
    for n in padres:
        print(f"MB({n}) = {manto_markov(n, padres, hijos)}")
