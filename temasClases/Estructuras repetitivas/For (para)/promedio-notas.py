# Capturar las notas de un curso y calcular el promedio de estas.
# Mostrar en pantalla el resultado del promedio.

cantidadNotas = int(input("¿Cuántas notas desea promediar?: "))
sumaNotas = 0

for i in range(1, cantidadNotas + 1):
    notas = float(input(f"Ingrese la nota #{i}: "))

    sumaNotas += notas

notaPromedio = sumaNotas / cantidadNotas

print(f"El promedio de las notas es: {notaPromedio:.1f}")