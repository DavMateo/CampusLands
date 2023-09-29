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
                input("Presione cualquier tecla para continuar...")
                continue
            break

        except ValueError:
            print("Opción no válida. Escoja de 1 a 5.")
            input("Presione cualquier tecla para continuar...")

    return opcion


def leerNum(mensaje):
    while True:
        try:
            num = float(input(mensaje))
            return num
        
        except ValueError:
            print("Error: Número inválido.")
            input("Presione cualquier tecla para continuar...")


# PROGRAMA PRINCIPAL
while True:
    opcionUsuario = menu()

    if opcionUsuario == 1:
        print("\n\n1. Sumar")
        num1 = leerNum("Ingrese el primer número: ")
        num2 = leerNum("Ingrese el segundo número: ")
        print(f"El resultado de la suma es: {suma(num1, num2):.3f}")

    elif opcionUsuario == 2:
        print("\n\n1. Restar")
        num1 = leerNum("Ingrese el primer número: ")
        num2 = leerNum("Ingrese el segundo número: ")
        print(f"El resultado de la suma es: {resta(num1, num2):.3f}")

    elif opcionUsuario == 3:
        print("\n\n1. Multiplicar")
        num1 = leerNum("Ingrese el primer número: ")
        num2 = leerNum("Ingrese el segundo número: ")
        print(f"El resultado de la suma es: {multiplicacion(num1, num2):.3f}")
        
    elif opcionUsuario == 4:
        print("\n\n1. Dividir")
        num1 = leerNum("Ingrese el primer número: ")
        num2 = leerNum("Ingrese el segundo número: ")
        resultado = division(num1, num2)

        if resultado != None:
            print(f"El resultado de la división es: {division(num1, num2):.3f}")
        else:
            print("División entre cero es indeterminada.")
        
    elif opcionUsuario == 5:
        print("\n\nGracias por usar la calculadora")
        print("Adios")
        input() # Espera una entrada de usuario cualquiera.
        break
    input("Presione cualquier tecla para volver al MENU...")