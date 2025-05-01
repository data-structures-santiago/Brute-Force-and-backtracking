# Este código genera todas las combinaciones posibles de un string dado,
# pero solo incluye aquellas combinaciones en las que el segundo carácter sea "a".
# Utiliza un enfoque recursivo para explorar las combinaciones y aplicar la restricción con una poda basica.

def combinaciones(s: str, current_sol: str = "", result: list[str] = []) -> list[str]:
    """
    Genera combinaciones de un string dado con una condición específica (ejercicio con poda de arboles basica).

    Args:
        s (str): El string de entrada cuyos caracteres se usarán para generar combinaciones.
        current_sol (str): La solución parcial que se construye recursivamente.
        result (list[str]): Una lista que almacena las combinaciones válidas generadas.

    Returns:
        list[str]: Una lista con las combinaciones que cumplen la condición.
    """
    # Caso base: si la longitud de la solución actual es igual a la del string original,
    # verifica si el segundo carácter es "a". Si es así, agrega la combinación a la lista de resultados.
    if len(current_sol) == len(s):
        if current_sol[1] == "a":
            result.append(current_sol)
        return result

    # Itera sobre los caracteres del string.
    for i in range(len(s)):
        # Si el carácter ya está en la solución actual, se omite para evitar duplicados.
        if s[i] in current_sol:
            continue
        # Restricción adicional: si la longitud de la solución parcial es 2 y el segundo carácter no es "a",
        # se detiene la exploración de esa rama (podar).
        if len(current_sol) == 2 and current_sol[1] != "a":
            return
        # Llama recursivamente a la función agregando el carácter actual a la solución parcial.
        combinaciones(s, current_sol + s[i], result)

    return result

# Ejemplo de uso:
# Genera combinaciones del string "abc" donde el segundo carácter es "a".
result = combinaciones("abc")

# Imprime el resultado.
print(result)