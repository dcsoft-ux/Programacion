"""
Este programa pide:
1. El precio de un producto (como cadena) y lo convierte a entero. Ok
2. El impuesto (como cadena) y lo convierte a entero. Ok
3. El descuento (como cadena) y lo convierte a flotante. Ok
4. Luego imprime los tipos de datos antes y después de la conversión. Ok
5. Imprimimos el total a pagar después de aplicar el impuesto y el descuento.
"""
precio = input("Ingrese el precio del producto: ")
print(type(precio))
precio = int(precio)
print(type(precio))
impuesto = input("Ingrese el impuesto (en porcentaje): ")
print(type(impuesto))
impuesto = int(impuesto)
print(type(impuesto))
descuento = input("Ingrese el descuento (en porcentaje): ")
print(type(descuento))
descuento = float(descuento)
print(type(descuento))
print("Total a pagar: =",precio+(precio*impuesto/100)-(precio*descuento/100))