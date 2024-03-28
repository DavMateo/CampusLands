num = input("Ingrese el número: ")

if num.startswith("+") and num.count("-") == 2:
    separarNumero = num.split("-")
    print("El telefono es:", separarNumero[1])
else:
    print("Error: El número no cumple con el formato.")