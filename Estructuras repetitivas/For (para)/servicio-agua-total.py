usuarios = int(input("¿Cuántos usuarios?: "))
totalConsumo = 0

for i in range(1, usuarios + 1):
    print(f"\nDatos del usuario #{i}:")

    codigo = input("¿Cuál es el código?: ")
    nombre = input("¿Cuál es el nombre?: ")
    estado = input("¿Cuál es el estado? [V: Vigente o S: Suspendido]: ")
    estrato = int(input("¿Cuál es el estrato? [1 al 6]: "))
    consumo = float(input("¿Cuál es el consumo del agua al mes? [cm3]: "))

    if estado == "V" or estado == "v":
        # Calcular la tarifa básica
        if estrato == 1:
            tarifaBasica = 10000
        elif estrato == 2:
            tarifaBasica = 20000
        elif estrato == 3:
            tarifaBasica = 30000
        elif estrato == 4:
            tarifaBasica = 45000
        elif estrato == 5:
            tarifaBasica = 60000
        elif estrato == 6:
            tarifaBasica = 70000
        else:
            tarifaBasica = 0

        # Calcular el valor de consumo
        valorConsumo = consumo * 200

        # Calcular el valor a pagar
        valorPagar = tarifaBasica + valorConsumo

        # Calcular el valor total a pagar de todos los usuarios
        totalConsumo += valorPagar
        
        # Imprimir el informe del usuario
        print("\n", "=" * 40)

        print("\tNombre: ", nombre)
        print(f"\tValor tarifa básica: ${tarifaBasica:,}")
        print(f"\tValor consumo: ${valorConsumo:,.0f}")
        print(f"\tValor de la factura de agua: ${valorPagar:,.0f}")


# Imprimir valor total a pagar de todos los usuarios
print("\n", "=" * 40)
print(f"\tValor total: ${totalConsumo:,.0f}")