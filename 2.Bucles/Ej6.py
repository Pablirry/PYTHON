'''
Escribe un programa que calcule la siguiente expresión y muestre el resultado:

100
∑   ((i^2 + 1)/i)
i=1

'''

suma = 0

for i in range(1, 101):
    suma += (i**2 + 1) / i
    
print("El resultado del sumatorio es: ", suma)