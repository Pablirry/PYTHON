'''
Implementa una función que pinte un rectángulo hueco de asteriscos.
'''

def rectangulo_hueco(ancho, alto):
    for i in range(alto):
        if i == 0 or i == alto - 1:
            print("*" * ancho)
        else:
            print("*" + " " * (ancho - 2) + "*")

ancho = int(input("Introduce el ancho del rectángulo: "))

while ancho < 3:
    print("El ancho debe ser mayor o igual a 3.")
    ancho = int(input("Introduce el ancho del rectángulo: "))

alto = int(input("Introduce el alto del rectángulo: "))

while alto < 3:
    print("El alto debe ser mayor o igual a 3.")
    alto = int(input("Introduce el alto del rectángulo: "))
    
rectangulo_hueco(ancho, alto)