for n in range (1, 50):
    match(n % 2, n % 7):
        case (0, 0):
            print("Dos y Siete")
        case (0, 1):
            print("Dos")
        case (1, 0):
            print("Siete")