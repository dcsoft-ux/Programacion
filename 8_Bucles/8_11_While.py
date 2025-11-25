#➡️ Inicializa la variable monedas con el valor 5
monedas = 5
#➡️ Mientras haya monedas disponibles (monedas > 0)
#➡️ Ejecuta el bloque de código dentro del while
#➡️ Disminuye el número de monedas en 1 en cada iteración
#➡️ Cuando no queden monedas, ejecuta el bloque de código dentro del else
#➡️ Imprime el número de monedas restantes en cada iteración
while monedas > 0:
    #➡️ Imprime el número de monedas restantes
    print(f"Tengo {monedas}")
    #➡️ Disminuye el número de monedas en 1
    #➡️ Actualiza el valor de monedas restando 1
    monedas -= 1
#➡️ Bloque else que se ejecuta cuando la condición del while ya no es verdadera
else:
    #➡️ Imprime que no quedan monedas
    #➡️ Mensaje final cuando no quedan monedas
    print("No tengo monedas")
