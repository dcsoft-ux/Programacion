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

#➡️ Leer la cantidad de números a ingresar
cantidad = input("¿Cuántos números deseas ingresar? ")
#➡️ Llamar a la función llenar_lista y almacenar el resultado
numeros = llenar_lista(cantidad)
#➡️ Imprimir la lista de números ingresados
print("Los números ingresados son:", numeros)