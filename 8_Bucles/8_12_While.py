#➡️ Bucle while con else
#➡️ Inicializa la variable respuesta con 's'
#➡️ Mientras la respuesta sea 's', el bucle continuará ejecutándose
#➡️ Solicita al usuario que ingrese si quiere seguir o no
respuesta = 's'
#➡️ Bucle while que se ejecuta mientras la respuesta sea 's'
#➡️ Dentro del bucle, se pide al usuario que ingrese una nueva respuesta
#➡️ Si la respuesta es diferente de 's', el bucle termina y se ejecuta el bloque else
#➡️ Al salir del bucle, se imprime un mensaje de agradecimiento
while respuesta == 's':
    #➡️ Solicita al usuario que ingrese si quiere seguir
    #➡️ Actualiza la variable respuesta con la entrada del usuario
    respuesta = input("Quieres seguir? (s/n)")
#➡️ Bloque else que se ejecuta cuando la condición del while ya no es verdadera
else:
    #➡️ Imprime un mensaje de agradecimiento
    print("Gracias")
