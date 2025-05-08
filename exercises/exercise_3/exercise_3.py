def backtracking(A,k=5, indice= 0, subconjunto_actual=[], resultado=[]):
    
    if sum(subconjunto_actual) == k:
        resultado.append(subconjunto_actual.copy())
        return resultado
    
    if sum(subconjunto_actual) > k or indice == len(A) :
        return
    subconjunto_actual.append(A[indice])

    
    
    backtracking(A,k, indice + 1, subconjunto_actual, resultado)

    # No incluir A[indice]
    subconjunto_actual.pop()
    backtracking(A,k, indice + 1, subconjunto_actual, resultado)


    return resultado




# Ejemplo de uso
A = [1, 2, 3,4]
k = 5
resultado_ = backtracking(A,k)
print(resultado_)

print("Todos los subconjuntos posibles:")
for s in resultado_:
    print(s)
