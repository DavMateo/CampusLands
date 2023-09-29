# Anidando condicionales dentro de otros condicionales.

nombreEstudiante = input("Nombre del estudiante: ")
nota = int(input("Ingrese una nota [0 - 100] : "))

if nota >= 0 and nota <= 59: 
    notaCualitativa = "D"
elif nota >= 60 and nota <= 79:
    notaCualitativa = "C"
elif nota >= 80 and nota <= 89:
    notaCualitativa = "B"
elif nota >= 90 and nota <= 100:
    notaCualitativa = "A"
else:
    notaCualitativa = ""
    print("Error: Has introducido un número distinto de entre 0 a 100")


print("\n", "-" * 30)
print("Estudiante:", nombreEstudiante);
print("Nota cuantitativa:", nota);
print("Nota cualitativa:", notaCualitativa);