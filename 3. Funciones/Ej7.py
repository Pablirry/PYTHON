'''
Implementa una función que muestre en pantalla la tabla de multiplicar
de un determinado número.
'''

def tabla_multiplicar(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")
    
n = int(input("Ingrese un número entero: "))

tabla_multiplicar(n)