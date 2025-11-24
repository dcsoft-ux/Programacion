"""
2. Ejercicios para el tipo de dato float (decimal)
Empresa: "AquaPure" — Purificadora de agua
Situación:
El laboratorio debe registrar la cantidad de litros purificados en distintos tanques.
Ejercicio:
Pide al usuario:
Litros purificados en el tanque A
Litros purificados en el tanque B
Objetivo:
Calcular la producción total con decimales.
"""
tanque_a = input("Ingrese los litros purificados en el tanque A: ")
tanque_a = float(tanque_a)
# tanque_a = float(input("Ingrese los litros purificados en el tanque A: "))
tanque_b = input("Ingrese los litros purificados en el tanque B: ")
tanque_b = float(tanque_b)
total_produccion = tanque_a + tanque_b
print("Producción total de litros purificados:", total_produccion)