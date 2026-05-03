"""
31 - Red Bayesiana Dinamica (DBN)
Modelo probabilistico para sistemas que evolucionan en el tiempo. Cada
slot temporal contiene variables de estado y observacion conectadas a
las del slot anterior. Aqui se hace filtrado en una DBN minima (HMM).
"""


def filtrar(belief, observacion, transicion, sensor):
    estados = list(belief.keys())
    pred = {sp: sum(belief[s] * transicion[s][sp] for s in estados) for sp in estados}
    nuevo = {s: sensor[s][observacion] * pred[s] for s in estados}
    z = sum(nuevo.values())
    return {s: v / z for s, v in nuevo.items()}


if __name__ == "__main__":
    estados = ["lluvia", "no_lluvia"]
    transicion = {"lluvia": {"lluvia": 0.7, "no_lluvia": 0.3},
                  "no_lluvia": {"lluvia": 0.3, "no_lluvia": 0.7}}
    sensor = {"lluvia": {"paraguas": 0.9, "nada": 0.1},
              "no_lluvia": {"paraguas": 0.2, "nada": 0.8}}
    b = {"lluvia": 0.5, "no_lluvia": 0.5}
    for o in ["paraguas", "paraguas", "nada"]:
        b = filtrar(b, o, transicion, sensor)
        print(f"obs={o}  belief={ {k: round(v,3) for k,v in b.items()} }")
