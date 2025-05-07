



def dividends(n,respuesta_actual=0):
    
    if (respuesta_actual//10**(n-1)>=1):
        if(respuesta_actual % 3 == 0):
            return 1
        else:
            return 0

    contador = 0
    for i in range(1,n+1):
        
        contador += dividends(n,(respuesta_actual*10)+i)
    return contador


print(dividends(3))