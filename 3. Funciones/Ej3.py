'''
Escribir una función en lenguaje Python que reciba un número entero positivo
como parámetro y devuelva True si el número es primo y False en caso contrario.
El número cero no se considera primo.
'''

def es_primo(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

n = int(input("Introduce un numero: "))

print(es_primo(n))