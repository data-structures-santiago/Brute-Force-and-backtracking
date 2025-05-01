# Este código genera todas las combinaciones posibles de un string dado,
# asegurándose de que las combinaciones tengan el mismo tamaño que el string original.
# Utiliza un enfoque recursivo para explorar todas las permutaciones posibles.

def combinaciones(s: str, current_sol: str = "", result: list[str] = []) -> list[str]:
    """
    Genera todas las combinaciones posibles de un string dado.

    Args:
        s (str): El string de entrada cuyos caracteres se usarán para generar combinaciones.
        current_sol (str): La solución parcial que se construye recursivamente.
        result (list[str]): Una lista que almacena todas las combinaciones generadas.

    Returns:
        list[str]: Una lista con todas las combinaciones posibles del string.
    """
    # Caso base: si la longitud de la solución actual es igual a la del string original,
    # se agrega la combinación a la lista de resultados.
    if len(current_sol) == len(s):
        result.append(current_sol)
        return result

    # Itera sobre los caracteres del string.
    for i in range(len(s)):
        # Si el carácter ya está en la solución actual, se omite para evitar duplicados.
        if s[i] in current_sol:
            continue
        # Llama recursivamente a la función agregando el carácter actual a la solución parcial.
        combinaciones(s, current_sol + s[i], result)
    
    return result

# Ejemplo de uso:
# Genera todas las combinaciones posibles del string "abc".
result = combinaciones("abc")

# Imprime el resultado.
print(result)