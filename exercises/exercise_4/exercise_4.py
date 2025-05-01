def backtracking(n,s,pos,suma=0):
    """
    Genera todas las combinaciones de n elementos que suman s.
    
    Args:
        n (int): Número total de elementos.
        s (int): Suma objetivo.
        pos (int): Posición actual en la combinación.
        suma (int): Suma actual de la combinación.
        
    Returns:
        int: Número de combinaciones que suman s.
    """
    if pos == n:
        return 1 if suma == s else 0
    
    suma_total = 0

    for i in range(10):
        if suma + i > s:   
            continue
        suma_total += backtracking(n, s, pos + 1, suma+i)
    

    return suma_total


n=2
s=5
# Ejemplo de uso    
print(backtracking(n, s, 0))