# Función recursiva principal
def knapsack_recursive(index, peso_actual, valor_actual, combinacion, items, capacity, resultado):
    
    if index == len(items):
        print("Combinación:", combinacion, "Peso:", peso_actual, "Valor:", valor_actual)
        if peso_actual <= capacity and valor_actual > resultado[1]:
            resultado[0] = combinacion[:]  # mejor combinación
            resultado[1] = valor_actual    # mejor valor
        return


    #print(peso_actual,valor_actual,combinacion)
    # Excluir el objeto actual
    knapsack_recursive(index + 1, peso_actual, valor_actual, combinacion, items, capacity, resultado)
    print(index)
    # Incluir el objeto actual si cabe
    nombre, peso, valor = items[index]

    if peso_actual + peso <= capacity:
        combinacion.append(nombre)
        knapsack_recursive(index + 1,
                           peso_actual + peso,
                           valor_actual + valor,
                           combinacion,
                           items,
                           capacity,
                           resultado)
        combinacion.pop()  # backtrack

    return





items = [
    ("A", 1, 12),
    ("B", 5, 10),
    ("C", 2, 16),
    ("D", 9, 17),
    ("E", 10, 13)
]
W = 20
resultado = [[], 0]  # [mejor_comb, mejor_valor]

knapsack_recursive(0, 0, 0, [], items, W, resultado)

# Mostrar resultados
print("🔍 Mejor combinación:", resultado[0])
print("💰 Valor total:", resultado[1])



