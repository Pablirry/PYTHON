'''
Escribir un programa en Python que lea un número entero comprendido entre -5 y 5 (ambos excluidos)
de tal forma que lo siga pidiendo al usuario mientras no sea correcto
'''

numero = int(input("Introduce un número entero entre -5 y 5: "))

while numero < -5 or numero > 5:
    print("El número no está en el rango permitido")
    numero = int(input("Introduce un número entero entre -5 y 5: "))

print("El número ", numero , " es correcto")