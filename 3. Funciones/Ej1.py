'''
Escribir una función de nombre checkNum que dados tres números enteros a, b y c
como parámetros devuelva: 1, cuando los tres números son iguales, 2, 
cuando dos de ellos son iguales y 3 cuando ninguno de ellos son iguales.
'''

def checkNum(a, b, c):
    if a == b == c:
        return 1
    elif a == b or a == c or b == c:
        return 2
    else:
        return 3
    
a = int(input("Ingrese el primer número: "))

b = int(input("Ingrese el segundo número: "))

c = int(input("Ingrese el tercer número: "))

print(checkNum(a, b, c))