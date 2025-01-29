'''
Pedir al usuario 3 números enteros a, b y c. 
Si los valores introducidos no cumplen las siguientes condiciones, 
se volverán a pedir al usuario hasta que los introduzca correctamente.
· (0.5 puntos) Todos los valores deben ser mayores que 0.
· (0.5 puntos) El valor de b debe ser inferior a c.
Nota: se acepta como válido volver a pedir los 3 números de nuevo si uno solo de los valores 
ha sido incorrecto. No es necesario pedir únicamente los valores que han sido incorrectos
'''

while True:
    a = float(input("Introduzca el primer número (mayor que 0.): "))
    b = float(input("Introduzca el segundo número (mayor que 0.): "))
    c = float(input("Introduzca el tercer número (mayor que 0.): "))
    
    if a > 0 and b > 0 and c > 0 and b < c:
        break
    else:
        print("Los valores introducidos no cumplen las condiciones. Por favor, inténtelo de nuevo.")

print("Valores correctos: a = ", a, " b = ", b, " c = ", c)