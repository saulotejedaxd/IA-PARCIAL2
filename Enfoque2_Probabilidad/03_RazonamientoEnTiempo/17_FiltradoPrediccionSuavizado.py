"""
17 - Filtrado, Prediccion, Suavizado y Explicacion
- Filtrado: P(X_t | e_{1:t})
- Prediccion: P(X_{t+k} | e_{1:t})
- Suavizado: P(X_k | e_{1:t}) con k < t
- Explicacion (Viterbi): mejor secuencia de estados.
"""


def normalizar(d):
    z = sum(d.values())
    return {k: v / z for k, v in d.items()}


def filtrar(b, obs, T, S):
    pred = {sp: sum(b[s] * T[s][sp] for s in b) for sp in T}
    nuevo = {sp: pred[sp] * S[sp][obs] for sp in pred}
    return normalizar(nuevo)


def predecir(b, k, T):
    for _ in range(k):
        b = {sp: sum(b[s] * T[s][sp] for s in b) for sp in T}
    return b


def suavizar(b_init, observaciones, T, S):
    fwd = [b_init]
    for o in observaciones:
        fwd.append(filtrar(fwd[-1], o, T, S))
    bwd = {s: 1.0 for s in T}
    suaves = [None] * (len(fwd))
    suaves[-1] = fwd[-1]
    for t in range(len(observaciones) - 1, -1, -1):
        o = observaciones[t]
        bwd = {s: sum(T[s][sp] * S[sp][o] * bwd[sp] for sp in T) for s in T}
        comb = {s: fwd[t][s] * bwd[s] for s in T}
        suaves[t] = normalizar(comb)
    return suaves


if __name__ == "__main__":
    T = {"L": {"L": 0.7, "S": 0.3}, "S": {"L": 0.3, "S": 0.7}}
    Sm = {"L": {"u": 0.9, "n": 0.1}, "S": {"u": 0.2, "n": 0.8}}
    b = {"L": 0.5, "S": 0.5}
    b1 = filtrar(b, "u", T, Sm)
    print("Filtrado tras u:", b1)
    print("Prediccion 2 pasos:", predecir(b1, 2, T))
    print("Suavizado [u, u, n]:", suavizar(b, ["u", "u", "n"], T, Sm))
