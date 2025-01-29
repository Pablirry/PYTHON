'''
Tenemos una variable X que contiene un valor. Queremos mostrar en la consola:
    3*X si la X está entre 0 y 1.
    -1 si la X es negativa.
    10*X si la X es mayor que 1.
'''

x = float(input("Introduce un valor para X: "))

if 0 <= x <= 1:
    resultado = 3 * x
elif x < 0:
    resultado = -1
elif x > 1:
    resultado = 10 * x
    
print("El resultado es ", resultado)
