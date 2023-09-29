# Validar el nombre del usuario.

while True:
    try:
        nombre = input("Ingrese el nombre del usuario: ")
        nombre = nombre.strip() # Elimina espacios al inicio o al final.

        if len(nombre) == 0 or nombre.isalnum() == False:
            print("Nombre inválido. Vuelva a digitarlo.")
            continue
        break

    except Exception as e:
        print("Error al ingresar el nombre.\n", e)


# Validar el estrato
while True:
    try:
        estrato = int(input("Ingrese el estrato (1-5): "))
        
        if estrato < 1 or estrato > 5:
            print("El estrato no está en el rango (1-5). Intente de nuevo")
            continue
        break

    except ValueError:  # El "exception" se define al final de todo el bloque o dato que querramos validar.
        print("Error. Estrato inválido.")


if estrato == 1:
    tarifaBasica = 10000
elif estrato == 2:
    tarifaBasica = 15000
elif estrato == 3:
    tarifaBasica = 30000
elif estrato == 4:
    tarifaBasica = 50000
else:
    tarifaBasica = 60000


print("\n", "=" * 35)
print(f"Nombre: {nombre}")
print(f"Estrato: {estrato}")
print(f"Tarifa básica: {tarifaBasica}")