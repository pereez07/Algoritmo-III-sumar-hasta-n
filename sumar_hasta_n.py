def sumar_hasta_n (n):    
    suma = 0
    contador = 1
    while contador <= n:
        suma = suma + contador
        contador = contador + 1

    return suma

print(sumar_hasta_n(5))
