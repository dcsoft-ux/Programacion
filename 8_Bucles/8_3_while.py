from random import *
numero = int(randint(0, 100))
numeroMio = -1

while numero != numeroMio:
    numeroMio = input ("Introduce un número: ")
    numeroMio = int(numeroMio)
    if numero == numeroMio:
        print("¡Ganaste!")
    elif numero < numeroMio:
        print("El número es menor")
    else:
        print("El número es mayor")
