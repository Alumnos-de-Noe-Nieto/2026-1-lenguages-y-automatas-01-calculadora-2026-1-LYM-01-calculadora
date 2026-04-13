"""
Nivel 1: Análisis Léxico - Alfabeto (Σ = {I, V, X, L, C, D, M})
"""

def validar_simbolos(cadena: str) -> bool:
    cadena_limpia = cadena.strip()
    if not cadena_limpia:
        return False
    alfabeto = "IVXLCDM"
    for simbolo in cadena_limpia:
        if simbolo not in alfabeto:
            return False
    return True
