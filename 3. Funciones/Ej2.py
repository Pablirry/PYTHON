'''
Escribir una función en Python que reciba como parámetros de entrada un número N 
y un dígito D y calcule y devuelva el número de veces que aparece el dígito D 
en el número N.
'''

def contar_digitos (N, D) :
    return str(N).count(str(D))

N = int(input("Ingrese un número entero: "))

D = int(input("Ingrese un dígito: "))

print(f"El dígito {D} aparece {contar_digitos(N, D)} veces en el número {N}.")