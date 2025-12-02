#➡️ Funcion para llenar una lista con números
def llenar_lista(cantidad):
    #➡️ Convierte la cantidad a entero
    cantidad = int(cantidad)
    #➡️ Inicializa una lista vacía
    lista_numeros = []
    #➡️ Itera desde 0 hasta cantidad-1
    for i in range(cantidad):
        #➡️ Solicita al usuario que ingrese un número
        numero = int(input(f"Ingresa el número {i + 1}: "))
        #➡️ Agrega el número a la lista
        lista_numeros.append(numero)
    #➡️ Devuelve la lista de números
    return lista_numeros

#➡️ Funcion para saber que numeros son pares e impares en una lista
def pares_e_impares(lista):
    #➡️ Inicializa dos listas vacías para pares e impares
    lista_pares = []
    lista_impares = []
    #➡️ Itera sobre cada número en la lista proporcionada
    for numero in lista:
        #➡️ Verifica si el número es par
        if numero % 2 == 0:
            #➡️ Agrega el número a la lista de pares
            lista_pares.append(numero)
        else:
            #➡️ Agrega el número a la lista de impares
            lista_impares.append(numero)
    #➡️ Devuelve ambas listas: pares e impares
    return lista_pares, lista_impares

#➡️ Leer la cantidad de números a ingresar
cantidad = input("¿Cuántos números deseas ingresar? ")
#➡️ Llamar a la función llenar_lista y almacenar el resultado
numeros = llenar_lista(cantidad)
#➡️ Imprimir la lista de números ingresados
print("Los números ingresados son:", numeros)
#➡️ Llamar a la función pares_e_impares y almacenar los resultados
pares, impares = pares_e_impares(numeros)
#➡️ Imprimir las listas de números pares e impares
print("Números pares:", pares)
print("Números impares:", impares)

