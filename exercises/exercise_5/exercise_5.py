def dividends(n,respuesta_actual="",answers=[]):
    

    if len(respuesta_actual) == n:
        if (int(respuesta_actual) % 3 == 0):

            answers.append(respuesta_actual)
        
        return

    for i in range(1,n+1):
        
        dividends(n,respuesta_actual+str(i),answers)
        
    return answers


print(dividends(3))
