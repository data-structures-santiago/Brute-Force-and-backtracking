def queens(n:int,respuesta=[]): # como devuevlo solo el resultado sin que sea un parametro mas
    
    if len(respuesta)==n:        
        print(respuesta)
        return  
    
    for i in range(n):
        if validar(i,respuesta):
            respuesta.append(i)
            queens(n,respuesta)
            respuesta.pop()
        
    return respuesta


def validar(posible_reina,respuesta):
    if posible_reina in respuesta:
        return False
    
    val_izq = posible_reina
    val_der = posible_reina

    for i in range(len(respuesta)-1,-1,-1):
        val_izq -= 1
        val_der += 1
        if respuesta[i] == val_izq or respuesta[i] == val_der:
            return False
    
    return True
    
    

print(queens(4))


