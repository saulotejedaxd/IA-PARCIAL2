"""
17 - Problemas de Satisfaccion de Restricciones (CSP)
Un CSP se define por: variables X, dominios D, restricciones C.
Aqui se modela el coloreo de mapa de Australia y se valida una asignacion.
"""


class CSP:
    def __init__(self, variables, dominios, vecinos, restriccion):
        self.variables = variables
        self.dominios = dominios
        self.vecinos = vecinos
        self.restriccion = restriccion

    def consistente(self, var, valor, asignacion):
        for v in self.vecinos[var]:
            if v in asignacion and not self.restriccion(var, valor, v, asignacion[v]):
                return False
        return True


if __name__ == "__main__":
    variables = ["WA", "NT", "Q", "NSW", "V", "SA", "T"]
    dominios = {v: ["R", "G", "B"] for v in variables}
    vecinos = {
        "WA": ["NT", "SA"], "NT": ["WA", "SA", "Q"],
        "Q": ["NT", "SA", "NSW"], "NSW": ["Q", "SA", "V"],
        "V": ["NSW", "SA"], "SA": ["WA", "NT", "Q", "NSW", "V"], "T": [],
    }
    restr = lambda x, vx, y, vy: vx != vy
    csp = CSP(variables, dominios, vecinos, restr)
    asignacion = {"WA": "R", "NT": "G", "SA": "B"}
    print("WA=R consistente con asignacion:", csp.consistente("WA", "R", asignacion))
    print("Q=G consistente:", csp.consistente("Q", "G", asignacion))
