# Programa para saber la liquidación del servicio de matrícula.


indicadorBeca1 = 50
indicadorBeca2 = 40
isVerdadero = True
valorNetoTotal = 0


while isVerdadero:

    while True:
        try:
            codigo = int(input("Ingrese el código del estudiante: "))
            break
        except Exception as e:
            print("Ha ocurrido un error al ingresar su código. \nError:", e)


    while True:
        try:
            nombre = input("Ingrese el nombre del estudiante: ")
            nombreArray = nombre.split(" ") # Verifica que el nombre tenga al menos dos palabras (1 nombre y 1 apellido)

            # Validación de la información:
            if len(nombreArray) < 2 or len(nombre) == 0 or nombre.isalnum():
                print("Error: Introduce tu nombre correctamente.")
                continue
            break

        except Exception as e:
            print("Ha ocurrido un error al digitar su nombre. \nError:", e)


    while True:
        try:
            programaAcademico = int(input("Ingrese el programa académico (1, 2 o 3): "))
            
            # Validación de la información
            if programaAcademico < 1 or programaAcademico > 3:
                print("Error: Escribe una opción dentro del rango establecido para el programa académico (1, 2 o 3)")
                continue
            break

        except ValueError:
            print("Ha ocurrido un error al digitar su programa académico. Asegúrese de ingresar un número entero válido.")
            print("Error:", e)


    while True:
        try:
            indicadorBeca = int(input("Ingrese el indicador de Beca (1, 2 o 3): "))

            # Validación de la información
            if indicadorBeca < 1 or indicadorBeca > 3:
                print("Error: Escribe una opción dentro del rango establecido para el indicador de beca (1, 2 o 3)")
                continue
            break

        except ValueError:
            print("Ha ocurrido un error al digitar su indicador de beca. Asegúrese de ingresar un número entero válido.")
            print("Error:", e)



    if programaAcademico == 1:
        valorMatricula = 800000

    if indicadorBeca == 1:
        descuentoMatricula = (valorMatricula * indicadorBeca1) / 100
        valorNetoMatricula = valorMatricula - descuentoMatricula

    elif indicadorBeca == 2:
        descuentoMatricula = (valorMatricula * indicadorBeca2) / 100
        valorNetoMatricula = valorMatricula - descuentoMatricula
    
    elif indicadorBeca == 3:
        valorNetoMatricula = valorMatricula

    
    print("\n", "=" * 35)
    print(f"Nombre: {nombre}")
    print(f"Valor matrícula: {valorNetoMatricula}")


    while True:
        try:
            continuar = input("¿Desea continuar? S/N: ").lower()

            if not continuar == "s" or not continuar == "n":
                print("Error: Has ingresado un valor distinto al indicado (S/N).")
                continue
            break

        except Exception as e:
            print(f"Error: Has introducido un valor erróneo. \nError: {e}")

    if continuar == "s":
        isVerdadero = True
    else:
        isVerdadero = False

print("\n", "=" * 35)
print(f"Valor total matrículas: {valorNetoTotal}")