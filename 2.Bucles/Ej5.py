'''
Escribir un programa que recorra los números comprendidos entre el b y el c (ambos incluidos).
De los números recorridos, solo deben mostrarse por pantalla los que sean divisibles entre a. 
Se deben sumar todos los números divisibles entre a, y mostrar el resultado al finalizar 
el programa.
'''

a = int(input("Introduzca el valor de a: "))
b = int(input("Introduzca el valor de b: "))
c = int(input("Introduzca el valor de c: "))

suma = 0

for n in range(b, c+1):
    if n % a == 0:
        print(n)
        suma += n
        
print("La suma de los números divisibles entre ", a, " es ", suma)