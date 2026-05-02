"""
25 - Redes de Decision (Diagramas de Influencia)
Extension de redes Bayesianas con nodos de decision (cuadrados) y
de utilidad (rombos). Selecciona la accion que maximiza utilidad esperada.
"""


def red_decision(acciones, prob_resultado, utilidad):
    mejor, mejor_eu = None, float("-inf")
    for a in acciones:
        eu = sum(p * utilidad(r, a) for r, p in prob_resultado(a).items())
        print(f"  EU({a}) = {eu:.3f}")
        if eu > mejor_eu:
            mejor, mejor_eu = a, eu
    return mejor, mejor_eu


if __name__ == "__main__":
    acciones = ["llevar_paraguas", "no_llevar"]
    def prob(a):
        return {"lluvia": 0.3, "sol": 0.7}
    def U(estado, accion):
        tabla = {("lluvia", "llevar_paraguas"): 8, ("sol", "llevar_paraguas"): 6,
                 ("lluvia", "no_llevar"): -10, ("sol", "no_llevar"): 10}
        return tabla[(estado, accion)]
    print("Decision optima:", red_decision(acciones, prob, U))
