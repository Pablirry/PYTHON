''' 
Escribir un programa que lea tres enteros e indique 
si están o no en orden ascendente. 
'''

A = int(input("Introduce un valor para A: "))
B = int(input("Introduce un valor para B: "))
C = int(input("Introduce un valor para C: "))

if A <= B <= C: 
    print("Los valores están en orden ascendente.")
else:
    print("Los valores no están en orden ascendente.")

