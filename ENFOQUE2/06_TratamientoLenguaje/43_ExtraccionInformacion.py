"""
43 - Extraccion de Informacion (NER por reglas)
Detecta entidades nombradas y relaciones simples a partir de patrones.
"""
import re


PATRONES = {
    "PERSONA": r"\b[A-Z][a-z]+ [A-Z][a-z]+\b",
    "FECHA":   r"\b\d{1,2}/\d{1,2}/\d{2,4}\b",
    "EMAIL":   r"\b[\w.]+@[\w.]+\.\w+\b",
    "NUMERO":  r"\b\d+\b",
}


def extraer(texto):
    encontrado = {}
    for tipo, pat in PATRONES.items():
        encontrado[tipo] = re.findall(pat, texto)
    return encontrado


if __name__ == "__main__":
    texto = ("Juan Perez nacio el 12/03/1990. Su correo es juan.perez@mail.com "
             "y tiene 35 anos. Maria Lopez lo conocio en 2020.")
    for tipo, vals in extraer(texto).items():
        print(f"{tipo}: {vals}")
