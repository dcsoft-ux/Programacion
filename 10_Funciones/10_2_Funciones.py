#➡️ Ejercicio de funciones

#➡️ Funcion que recibe dos atributos, nombre y apellido, y devuelve el nombre completo
def nombre_completo(nombre, apellido):
    #➡️ Concatena el nombre y apellido con un espacio en medio
    return f"{nombre} {apellido}"

#➡️ Solicitamos al usuario que ingrese su nombre
nombre = input("Ingresa tu nombre: ")
#➡️ Solicitamos al usuario que ingrese su apellido
apellido = input("Ingresa tu apellido: ")
#➡️ Llamamos a la función nombre_completo y almacenamos el resultado en la variable completo
completo = nombre_completo(nombre, apellido)
#➡️ Imprimimos el nombre completo
print(f"Tu nombre completo es: {completo}")