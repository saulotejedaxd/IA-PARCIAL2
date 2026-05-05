"""
18 - Algoritmo Hacia Delante - Hacia Atras (Forward-Backward)
Calcula P(X_t | e_{1:T}) para todo t en O(N^2 * T) usando dos pasadas:
forward (alpha) y backward (beta).
"""


def forward_backward(b0, observaciones, T, S):
    estados = list(T.keys())
    alpha = [b0]
    for o in observaciones:
        a = alpha[-1]
        pred = {sp: sum(a[s] * T[s][sp] for s in estados) for sp in estados}
        nuevo = {sp: pred[sp] * S[sp][o] for sp in estados}
        z = sum(nuevo.values())
        alpha.append({k: v / z for k, v in nuevo.items()})
    beta = [{s: 1.0 for s in estados}]
    for o in reversed(observaciones):
        b = beta[0]
        nb = {s: sum(T[s][sp] * S[sp][o] * b[sp] for sp in estados) for s in estados}
        z = sum(nb.values())
        beta.insert(0, {k: v / z for k, v in nb.items()})
    posteriores = []
    for t in range(len(alpha)):
        comb = {s: alpha[t][s] * beta[t][s] for s in estados}
        z = sum(comb.values())
        posteriores.append({k: v / z for k, v in comb.items()})
    return posteriores


if __name__ == "__main__":
    T = {"L": {"L": 0.7, "S": 0.3}, "S": {"L": 0.3, "S": 0.7}}
    Sm = {"L": {"u": 0.9, "n": 0.1}, "S": {"u": 0.2, "n": 0.8}}
    b0 = {"L": 0.5, "S": 0.5}
    for t, p in enumerate(forward_backward(b0, ["u", "u", "n"], T, Sm)):
        print(f"t={t}: {p}")
