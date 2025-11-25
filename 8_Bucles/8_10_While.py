#➡️ Juego de adivinar el número
#➡️ El programa genera un número aleatorio entre 0 y 100
#➡️ El usuario debe adivinar el número
#➡️ El programa indica si el número ingresado es mayor o menor que el número generado
#➡️ El ciclo while continúa hasta que el usuario adivina el número correcto
#➡️ Importamos la función randint del módulo random para generar números aleatorios
from random import *
#➡️ Generamos un número aleatorio entre 0 y 100
#➡️ randint(0, 100) devuelve un número entero entre 0 y 100, ambos inclusive
#➡️ Inicializamos la variable numeroMio con un valor que no es posible adivinar
numero = int(randint(0, 100))
#➡️ Inicializamos la variable numeroMio con un valor fuera del rango posible
numeroMio = -1

#➡️ Iniciamos un ciclo while que continuará hasta que el usuario adivine el número
while numero != numeroMio:
    #➡️ Solicitamos al usuario que ingrese un número
    numeroMio = input ("Introduce un número: ")
    #➡️ Convertimos la entrada del usuario a un entero para compararla con el número generado
    numeroMio = int(numeroMio)
    #➡️ Comparamos el número ingresado con el número generado
    if numero == numeroMio:
        #➡️ Si el número es correcto, informamos al usuario que ha ganado
        print("¡Ganaste!")
    #➡️ Si el número es incorrecto, indicamos si es mayor o menor
    elif numero < numeroMio:
        #➡️ Si el número ingresado es mayor, informamos al usuario
        print("El número es menor")
    #➡️ Si el número ingresado es menor, informamos al usuario
    else:
        #➡️ Si el número ingresado es mayor, informamos al usuario
        print("El número es mayor")
