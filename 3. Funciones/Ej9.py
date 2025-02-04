'''
Una máquina de refrescos admite monedas de 2 euros, 1 euros, 50 céntimos, 
20 céntimos, 10 céntimos, 2 céntimos y 1 céntimo. 
Crea un programa que muestre un producto y un precio y 
que permita introducir un importe exacto o superior. 
El programa debe calcular el cambio en el menor número de monedas posibles.
'''

def cambio(precio, pago):
    cambio = pago - precio
    monedas = [200, 100, 50, 20, 10, 2, 1]
    resultado = []
    
    for moneda in monedas:
        cantidad = cambio // moneda
        if cantidad > 0:
            resultado.append((moneda, cantidad))
            cambio -= moneda * cantidad
    return resultado

producto = str(input("Introduce nombre de producto: "))
precio = int(input("Introduce el precio en céntimos: "))

print(f"Producto: {producto}")
print(f"Precio: {precio / 100:.2f} euros")

pago = int(input("Introduce el importe en céntimos: "))

if pago < precio:
    print("El importe introducido es insuficiente.")
else:
    cambio = cambio(precio, pago)
    print("Cambio:")
    for moneda, cantidad in cambio:
        print(f"{cantidad} moneda(s) de {moneda / 100:.2f} euros")