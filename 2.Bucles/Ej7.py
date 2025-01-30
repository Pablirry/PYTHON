'''
Dados dos enteros a>0 y b, modificar el programa anterior para 
calcular la expresión matemática y escribir el resultado en pantalla

b
∑   ((i^2 + 1)/i)
a
'''

a = int(input("Introduzca el valor de a: "))
b = int(input("Introduzca el valor de b: "))

suma = 0

for i in range(a, b+1):
    suma += ((i**2 + 1)/i)
    
print(f"El resultado del sumatorio es: ", suma)