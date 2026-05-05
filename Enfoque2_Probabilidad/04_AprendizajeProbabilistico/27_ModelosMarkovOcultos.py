"""
27 - Modelos de Markov Ocultos: Aprendizaje (Baum-Welch)
EM aplicado a HMMs: estima A, B, pi a partir de observaciones sin
saber los estados. Aqui una version compacta.
"""


def normalizar(d):
    z = sum(d.values()) or 1e-12
    return {k: v / z for k, v in d.items()}


def baum_welch(observaciones, estados, vocab, iters=10):
    A = {s: {sp: 1 / len(estados) for sp in estados} for s in estados}
    B = {s: {o: 1 / len(vocab) for o in vocab} for s in estados}
    pi = {s: 1 / len(estados) for s in estados}
    T = len(observaciones)
    for _ in range(iters):
        alpha = [{s: pi[s] * B[s][observaciones[0]] for s in estados}]
        for t in range(1, T):
            a_t = {sp: sum(alpha[t-1][s] * A[s][sp] for s in estados) * B[sp][observaciones[t]]
                   for sp in estados}
            alpha.append(normalizar(a_t))
        beta = [{s: 1.0 for s in estados}]
        for t in range(T - 1, 0, -1):
            b_t = {s: sum(A[s][sp] * B[sp][observaciones[t]] * beta[0][sp] for sp in estados)
                   for s in estados}
            beta.insert(0, normalizar(b_t))
        gamma = [normalizar({s: alpha[t][s] * beta[t][s] for s in estados}) for t in range(T)]
        pi = gamma[0]
        for s in estados:
            for sp in estados:
                A[s][sp] = (sum(alpha[t][s] * A[s][sp] * B[sp][observaciones[t+1]] * beta[t+1][sp]
                                for t in range(T-1)) /
                            (sum(gamma[t][s] for t in range(T-1)) or 1e-12))
            A[s] = normalizar(A[s])
        for s in estados:
            for o in vocab:
                B[s][o] = sum(gamma[t][s] for t in range(T) if observaciones[t] == o) / \
                           (sum(gamma[t][s] for t in range(T)) or 1e-12)
            B[s] = normalizar(B[s])
    return A, B, pi


if __name__ == "__main__":
    obs = ["u", "u", "n", "u", "n", "n"]
    A, B, pi = baum_welch(obs, ["s1", "s2"], ["u", "n"], iters=20)
    print("A:", A)
    print("B:", B)
    print("pi:", pi)
