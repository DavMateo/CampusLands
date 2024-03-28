# Programa para determinar si un estudiante aprobó o reprobó el curso.

def resultadoEstudiante(n1, n2, n3, n4, n5):
    promedio = (n1 + n2 + n3 + n4 + n5) / 5
    if promedio > 3.5:
        return True
    else:
        return False


num1 = float(input("Ingrese la nota 1: "))
num2 = float(input("Ingrese la nota 2: "))
num3 = float(input("Ingrese la nota 3: "))
num4 = float(input("Ingrese la nota 4: "))
num5 = float(input("Ingrese la nota 5: "))

resultadoNotaEstudiante = resultadoEstudiante(num1, num2, num3, num4, num5)

if resultadoNotaEstudiante:     # Es lo mismo que decir "resultadoNotaEstudiante == True"
    print("El estudiante ha aprobado el curso.")
else:
    print("El estudiante reprobó el curso.")