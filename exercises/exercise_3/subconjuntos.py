def backtracking(A, indice= 0, subconjunto_actual=[], resultado=[]):
    if indice == len(A):
        resultado.append(subconjunto_actual.copy())
        return resultado

    # Incluir A[indice]
    subconjunto_actual.append(A[indice])
    backtracking(A, indice + 1, subconjunto_actual, resultado)

    # No incluir A[indice]
    subconjunto_actual.pop()
    backtracking(A, indice + 1, subconjunto_actual, resultado)

    return resultado




# Ejemplo de uso
A = [1, 2, 3,4]
resultado_ = backtracking(A)
print(resultado_)

print("Todos los subconjuntos posibles:")
for s in resultado_:
    print(s)
