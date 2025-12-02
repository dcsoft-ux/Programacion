#➡️ Una funcion es un bloque de código reutilizable que realiza una tarea específica.
#➡️ Ejemplo de una función en Python
#➡️ Define una función llamada saludar que toma un parámetro nombre
def saludar(nombre):
    #➡️ Imprime un mensaje de saludo utilizando el parámetro nombre
    print(f"Hola {nombre} !")

#➡️ Creamos la variable nombre y le asignamos un valor
nombre = "Ana"

#➡️ Llamamos a la función saludar pasando la variable nombre como argumento
saludar(nombre)

#➡️ Creamos la variable nombre y le asignamos un valor
nombre = input("Ingresa tu nombre: ")
#➡️ Llamamos a la función saludar pasando la variable nombre como argumento
saludar(nombre)