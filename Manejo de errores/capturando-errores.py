while True:
    try:
        num1 = int(input("Ingrese un número: "))
        break
    except ValueError:
        print("Error: Número entero no válido.")

while True:
    try:
        num2 = int(input("Ingrese otro número: "))
        break
    except ValueError:
        print("Error. Número entero no válido.")


try:
    num2 = "a"
    suma = num1 + num2
    print("La suma es:", suma)
except Exception as e:  # Excepción general.
    print("Error al intentar sumar.\n", e) 
        # La letra "e" es un alias, pues "Exception" es una clase que contiene todas 
        # las excepciones posibles de Python. Al ocurrir una excepción cualquiera, se la pasa 
        # a "e" que funciona similar a una variable que almacena el tipo de error generado.

print("\nEl número que digitó es:", num1)