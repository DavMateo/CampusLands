# Programa para solucionar el problema de la liquidación servicio matrícula. Calcula valor a pagar
# y descuento si es que aplica.


# DEFINIENDO LAS VARIABLES PRINCIPALES.
checked = True
valorTecnicoSistemas = 800000
valorTecnicoDesarrolloVideojuegos = 1000000
valorTecnicoAnimacionDigital = 1200000
becaRendimientoAcademico = 50
becaCultural = 40
valorTotalMatriculas = 0



while checked:
    codigoEstudiante = int(input("\nIngrese el código del estudiante: "))
    nombreEstudiante = input("Ingrese el nombre del estudiante: ")
    programaAcademicoEstudiante = int(input("Ingrese el programa académico del estudiante: 1 para Técnico en Sistemas, 2 para Técnico en Desarrollo de videojuegos o 3 para Técnico en animación digital: "))
    indicadorBecaEstudiante = int(input("Becas: Ingrese 1 para beca por rendimiento académico, 2 para beca cultural o 3 si el estudiante no aplica para ninguna beca: "))

    if programaAcademicoEstudiante == 1:
        valorMatricula = valorTecnicoSistemas

        if indicadorBecaEstudiante == 1:
            valorDescontar = (valorTecnicoSistemas * becaRendimientoAcademico) / 100
            valorMatricula -= valorDescontar

        elif indicadorBecaEstudiante == 2:
            valorDescontar = (valorTecnicoSistemas * becaCultural) / 100
            valorMatricula -= valorDescontar

        elif indicadorBecaEstudiante == 3:
            valorMatricula -= 0
    
    elif programaAcademicoEstudiante == 2:
        valorMatricula = valorTecnicoDesarrolloVideojuegos

        if indicadorBecaEstudiante == 1:
            valorDescontar = (valorTecnicoDesarrolloVideojuegos * becaRendimientoAcademico) / 100
            valorMatricula -= valorDescontar

        elif indicadorBecaEstudiante == 2:
            valorDescontar = (valorTecnicoDesarrolloVideojuegos * becaRendimientoAcademico) / 100
            valorMatricula -= valorDescontar

        elif indicadorBecaEstudiante == 3:
            valorMatricula -= 0

    elif programaAcademicoEstudiante == 3:
        valorMatricula = valorTecnicoAnimacionDigital

        if indicadorBecaEstudiante == 1:
            valorDescontar = (valorTecnicoAnimacionDigital * becaRendimientoAcademico) / 100
            valorMatricula -= valorDescontar

        elif indicadorBecaEstudiante == 2:
            valorDescontar = (valorTecnicoAnimacionDigital * becaRendimientoAcademico) / 100
            valorMatricula -= valorDescontar

        elif indicadorBecaEstudiante == 3:
            valorMatricula -= 0
        
    else:
        print("\nError: Por favor elija una opción válida. Saliendo...")
        checked = False
    
    valorTotalMatriculas += valorMatricula

    print("\n", "=" * 35)
    print(f"\nCódigo estudiante: {codigoEstudiante}.")
    print(f"Nombre estudiante: {nombreEstudiante}.")
    print(f"Valor matrícula: {valorMatricula}.")
    print(f"Valor total matrículas: {valorTotalMatriculas}.")


    continuar = input("\n¿Desea continuar? S/N: ")

    if continuar == "S" or continuar == "s":
        checked  = True
    elif continuar == "N" or continuar == "n":
        checked = False
    else:
        print("\nError: Escribe una opción válida. Saliendo...")
        checked = False