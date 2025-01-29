'''
Completar el siguiente programa de forma que imprima por pantalla 
la variable con menor valor.

A = int (input("Entrar valor para A: ")
B = int (input("Entrar valor para B: ")
C = int (input("Entrar valor para C: ")
'''

A = int (input("Entrar valor para A: "))
B = int (input("Entrar valor para B: "))
C = int (input("Entrar valor para C: "))

if A < B and A < C:
    menor = A
elif B < A and B < C:
    menor = B
else:
    menor = C
    
print("El menor valor es: ", menor)


