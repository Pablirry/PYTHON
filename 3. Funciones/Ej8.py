'''
Implementa un programa que imprima por pantalla todas las ternas pitagóricas 
(valores de catetos e hipotenusas) posibles con valores enteros menores que 500 
(hipotenusa incluida).
'''

def ternas_pitagoricas(max_valor):
    for a in range(1, max_valor):
        for b in range(a, max_valor):
            c = (a**2 + b**2) ** 0.5
            if c.is_integer() and c < max_valor:
                print(f"({a}, {b}, {int(c)})")

# Llamada a la función con el valor máximo de 500
ternas_pitagoricas(500)
