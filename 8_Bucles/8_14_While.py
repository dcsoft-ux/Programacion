#➡️ Escribe un programa que pida al usuario su nombre y lo imprima letra por letra. Si encuentra la letra 'a', debe detener la impresión.
#➡️ Solicita al usuario que ingrese su nombre
#➡️ Itera sobre cada letra del nombre ingresado
#➡️ Imprime cada letra por separado
nombre = input("Nombre: ")
#➡️ Itera sobre cada letra del nombre
#➡️ Si la letra es 'a', detiene la impresión usando break
#➡️ Imprime cada letra del nombre
for letra in nombre:
    #➡️ Imprime la letra actual
    print(letra)
    #➡️ Si la letra es 'a', detiene el bucle
    #➡️ Usa break para salir del bucle cuando se encuentra 'a'
    if letra == 'a':
        #➡️ Detiene el bucle
        break
