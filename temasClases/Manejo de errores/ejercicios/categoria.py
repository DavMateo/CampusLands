while True:
    categoria = int(input("Ingrese una categoria (1, 2 o 3): "))

    try:
        if categoria < 1 or categoria > 3:
            print("Categoria inválida. Ingrese 1, 2, o 3.")
            continue    # Vuelve a empezar el while
        break

    except ValueError:
        print("Categoría inválida.")