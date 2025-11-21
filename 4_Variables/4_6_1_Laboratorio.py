# EJERCICIOS POR TIPO DE DATO — Contexto Empresarial
"""
1. Ejercicios para el tipo de dato int (entero)
Empresa: "LogiExpress" — Empresa de envíos nacionales
Situación:
El departamento de operaciones necesita calcular la cantidad total de paquetes procesados en una jornada.
Ejercicio:
Pide al usuario ingresar:
Cantidad de paquetes enviados en la mañana
Cantidad de paquetes enviados en la tarde
Cantidad de paquetes enviados en la noche
Objetivo:
Suma los valores y muestra el total de paquetes procesados.
"""

paquetes_manana = input("Ingrese la cantidad de paquetes enviados en la mañana: ")
paquetes_manana = int(paquetes_manana)
paquetes_tarde= input("Ingrese la cantidad de paquetes enviados en la tarde: ")
paquetes_tarde = int(paquetes_tarde)
paquetes_noche = input("Ingrese la cantidad de paquetes enviados en la noche: ")
paquetes_noche = int(paquetes_noche)

total = paquetes_manana + paquetes_tarde + paquetes_noche
print("Total de paquetes procesados en la jornada:", total)