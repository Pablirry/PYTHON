'''
Implementa una función que retorne el factorial de un número natural
'''

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

n = int(input("Ingrese un número entero positivo: "))

while n < 0:
    print("Error: El número debe ser positivo.")
    n = int(input("Ingrese un número entero positivo: "))

factorial_n = factorial(n)

print("El factorial de", n, "es:", factorial_n)
    