#➡️ Funcion para saber si un número es par o impar
def es_par_o_impar(numero):
    #➡️ Convierte el valor ingresado a entero
    numero = int(numero)
    #➡️ Verifica si el número es divisible por 2
    if numero % 2 == 0:
        return "El número es par"
    else:
        return "El número es impar"
#➡️ Solicita al usuario que ingrese un número
numero = input("Ingresa un número entero: ")
#➡️ Llama a la función es_par_o_impar y almacena el resultado
resultado = es_par_o_impar(numero)
#➡️ Imprime el resultado
print(resultado)