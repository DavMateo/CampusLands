#Ejercicio: Hacer un programa que lea N estudiantes (Nombre y nota).
# Y nos muestre el promedio de la clase, el estudiante con mayor nota y el estudiante
# con menor nota.


def leerInt(msj):
    while True:
        try:
            n = int(input(msj))
            if n < 1:
                print("Valor inválido. Debe ser mayor a cero")
                continue
            return n
        
        except ValueError:
            print("Error al ingresar el número.")

def leerNombre(msj):
    while True:
        try:
            nom = input(msj)
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def leerNotas(msj):
    while True:
        try:
            n = float(input(msj))
            
            if n < 0 or n > 5:
                print("Nota inválida. Debe ser mayor o igual a cero.")
                continue
            return n
        
        except ValueError:
            print("Error al ingresar la nota.")

n = leerInt("Cuántos estudiantes son?: ")
listaNombres = []
listaNotas = []

for i in range(1, n + 1):
    print(f"\nDatos del estudiante n°{i}")
    listaNombres.append(leerNombre("Nombre?: "))
    listaNotas.append(leerNotas("Nota? "))


# Calcular y mostrar el promedio
promedio = sum(listaNotas) / n
print("\n", "=" * 30)
print(f"El promedio del curso es: {promedio:.1f}")


# Encontrar y mostrar el estudiante con mayor nota
notaMayor = max(listaNotas)
posicionEstudianteMayor = listaNotas.index(notaMayor)
nombreEstudianteMayorNota = listaNombres[posicionEstudianteMayor]
print(f"El estudiante {nombreEstudianteMayorNota} tiene la mayor nota: {notaMayor}")


# Encontrar y mostrar el estudiante con menor nota
notaMenor = min(listaNotas)
posicionEstudianteMenor = listaNotas.index(notaMenor)
nombreEstudianteMenorNota = listaNombres[posicionEstudianteMenor]
print(f"El estudiante {nombreEstudianteMenorNota} tiene la menor nota: {notaMenor}")