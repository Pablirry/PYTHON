'''
Implementa una función que calcule el valor absoluto de un número.
'''

def absolute_value(number):
    if number < 0:
        return -number
    else:
        return number

number = absolute_value(int(input("Ingrese un número: ")))

print("El valor absoluto de", number, "es", absolute_value(number))