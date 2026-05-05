"""
19 - Modelos Ocultos de Markov (HMM)
Estados ocultos forman cadena de Markov; cada uno emite una observacion
con prob B[s][o]. Aqui se implementa Viterbi para hallar la mejor
secuencia de estados.
"""


def viterbi(observaciones, A, B, pi):
    estados = list(A.keys())
    V = [{s: pi[s] * B[s][observaciones[0]] for s in estados}]
    bp = [{s: None for s in estados}]
    for o in observaciones[1:]:
        Vt, bpt = {}, {}
        for sp in estados:
            mejor, arg = max(((V[-1][s] * A[s][sp], s) for s in estados))
            Vt[sp] = mejor * B[sp][o]
            bpt[sp] = arg
        V.append(Vt)
        bp.append(bpt)
    fin = max(V[-1], key=V[-1].get)
    camino = [fin]
    for t in range(len(V) - 1, 0, -1):
        camino.insert(0, bp[t][camino[0]])
    return camino, V[-1][fin]


if __name__ == "__main__":
    A = {"L": {"L": 0.7, "S": 0.3}, "S": {"L": 0.3, "S": 0.7}}
    B = {"L": {"u": 0.9, "n": 0.1}, "S": {"u": 0.2, "n": 0.8}}
    pi = {"L": 0.5, "S": 0.5}
    seq, prob = viterbi(["u", "u", "n", "u"], A, B, pi)
    print(f"Mejor secuencia: {seq}  Prob: {prob:.5f}")
