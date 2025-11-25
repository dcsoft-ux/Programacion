#➡️ Muestra la tabla de multiplicar de ese número del 0 al 9
#➡️ Utiliza un ciclo for para generar la tabla de multiplicar
#➡️ Cada iteración del ciclo multiplica el número ingresado por el índice del ciclo
#➡️ Imprime el resultado de cada multiplicación
#➡️ Solicita al usuario que ingrese un número
numero = int(input("Ingrese un número: "))
#➡️ Ciclo for para iterar desde 0 hasta 9
for i in range(0, 10):
    #➡️ Calcula la multiplicación del número ingresado por el índice del ciclo
    multiplicacion = numero * i
    #➡️ Imprime el resultado de la multiplicación
    print (multiplicacion)