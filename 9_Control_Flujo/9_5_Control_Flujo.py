calculadora = True
while calculadora:
    n = int(input("1. Sumar\n2. Restar\n3. Multiplicar\n4. Dividir\n5. Salir\nSeleccione una opción: "))
    match n:
        case 1:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            print(a+b)
        case 2:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            print(a-b)
        case 3:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            print(a*b)
        case 4:
            a = int(input("Ingrese el primer número: "))
            b = int(input("Ingrese el segundo número: "))
            print(a/b)
        case 5:
            calculadora = False
        case _:
            print("No se encuentra")