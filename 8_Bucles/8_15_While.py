#➡️ Juego de adivinar el número con un máximo de 8 intentos
#➡️ Importa la función randint del módulo random para generar un número aleatorio
#➡️ el random se usa para generar números aleatorios
#➡️ el randint se usa para generar un número entero aleatorio dentro de un rango específico
from random import *
#➡️ Solicita al usuario que ingrese su nombre
nombre = input("Escribe tu nombre: ")
#➡️ Genera un número secreto aleatorio entre 0 y 100
numero_secreto = randint(0,100)
#➡️ Inicializa las variables estimado e intentos
estimado = 0
#➡️ Inicializa el contador de intentos en 1
intentos = 1
#➡️ Informa al usuario sobre el juego y la cantidad de intentos disponibles
#➡️ Usa una f-string para incluir el nombre del usuario en el mensaje
#➡️ Indica que el usuario tiene 8 intentos para adivinar un número entre 1 y 100
print(f"{nombre} tienes 8 intentos para adivinar un número entre 1 y 100")
#➡️ Bucle while que se ejecuta mientras el número de intentos sea menor que 8
#➡️ Dentro del bucle, solicita al usuario que ingrese su estimación del número
while intentos < 8:
    #➡️ Solicita al usuario que ingrese su estimación del número
    estimado = int(input("Cuál es el número: "))
    #➡️ Incrementa el contador de intentos en 1
    intentos += 1
    #➡️ Verifica si la estimación está fuera del rango permitido (1-100)
    if estimado not in range(1,101):
        #➡️ Informa al usuario que el número debe estar entre 1 y 100
        print("El número debe estar entre 1 y 100")
    #➡️ Compara la estimación con el número secreto e informa al usuario
    if estimado < numero_secreto:
        #➡️ Le indica el usuario que el número es más alto
        print("El número es más alto")
    #➡️ Compara la estimación con el número secreto e informa al usuario
    elif estimado > numero_secreto:
        #➡️ Le indica al usuario que el número es más bajo
        print("El número es más bajo")
    #➡️ Si la estimación es correcta, informa al usuario y termina el juego
    else:
        #➡️ Informa al usuario que ha adivinado el número correctamente
        print(f"Adivinaste el número {nombre} en {intentos} intentos")
        #➡️ Sale del bucle ya que el número ha sido adivinado
        break
#➡️ Si el usuario no adivina el número en 8 intentos, informa cuál era el número secreto
if estimado != numero_secreto:
    #➡️ Informa al usuario que ha perdido y revela el número secreto
    print(f"Perdiste, el número era {numero_secreto}")
