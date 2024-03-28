# Programa para calcular la tarifa a pagar por el servicio de energía.
# (Solo se tendrá en cuenta la tarifa básica).


# Dado el nombre y estrato (1, 2, 3, 4, 5) de un usuario del servicio de energía eléctrica,
# calcular lo que pagaría de tarifa básica del servicio de energía eléctrica, que depende del estrato, así:
#   1: $10.000
#   2: $15.000
#   3: $30.000
#   4: $50.000
#   5: $65.000



# DECLARANDO LAS VARIABLES PRINCIPALES.
checked = True
estrato1 = 10000
estrato2 = 15000
estrato3 = 30000
estrato4 = 50000
estrato5 = 65000


# DEFINIENDO LA PARTE DEL PROGRAMA
while checked:
    nombre = input("\n¿Cuál es su nombre?: ")
    estrato = int(input("¿Cúal es su estrato?: "))


    if checked == True:
        print("\n", "=" * 35)
        print(f"Nombre: {nombre}")
        
        if estrato == 1:
            print(f"Valor de tarifa básica: {estrato1}")
        elif estrato == 2:
            print(f"Valor de tarifa básica: {estrato2}")
        elif estrato == 3:
            print(f"Valor de tarifa básica: {estrato3}")
        elif estrato == 4:
            print(f"Valor de tarifa básica: {estrato4}")
        elif estrato == 5:
            print(f"Valor de tarifa básica: {estrato5}")
        else:
            print("Error: Introduce un estrato válido en número entero (1, 2, 3, 4 o 5).")
    else:
        break   # Por si dado caso la variable checked llegase a fallar.


    continuar = input("\n¿Desea continuar? S/N: ")


    if continuar == "s" or continuar == "S":
        checked = True
    elif continuar == "n" or continuar == "N":
        checked = False
        print("Saliendo...")
    else:
        print("Error: Asegúrate de introducir S para sí o N para no. Saliendo...")
        checked = False