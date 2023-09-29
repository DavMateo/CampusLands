def suma(num1, num2):
    resultado = num1 + num2
    return resultado

def resta(num1, num2):
    return num1 - num2

def multiplicacion(num1, num2):
    return num1 * num2

def division(num1, num2):
    try:
        resultado = num1 / num2
    except ZeroDivisionError:
        resultado = None

    return resultado

def menu():
    while True:
        try:
            print("*** MENU CALCULADORA ***")
            print("1. Sumar")
            print("2. Restar")
            print("3. Multiplicar")
            print("4. Dividir")
            print("5. Salir")
            opcion = int(input(">>> Opción (1-5): "))

            if opcion < 1 or opcion > 5:
                print("Opción no válida. Escoja de 1 a 5.")
                continue
            break

        except ValueError:
            print("Opción no válida. Escoja de 1 a 5.")

    return opcion


def leerNum(mensaje):
    pass


# PROGRAMA PRINCIPAL
while True:
    opcionUsuario = menu()

    if opcionUsuario == 1:
        print("\n\n1. Sumar")
        num1 = leerNum("Ingrese el primer número: ")
        num2 = leerNum("Ingrese el segundo número: ")
