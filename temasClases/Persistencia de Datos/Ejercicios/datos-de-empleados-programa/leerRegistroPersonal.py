# Programa que permite leer y mostrar en pantalla los datos del personal 
# de una empresa que están almacenados en el disco del equipo de cómputo.


# DECLARANDO LAS VARIABLES PRINCIPALES
count = 0
encabezado = []
listaInfoEmpleados = []
personal = {}


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def crearMatrices(fil, col):
    matrizDatos = []
    
    for i in range(fil):
        fila = [0] * col
        matrizDatos.append(fila)
    
    return matrizDatos
            

# CREANDO LA ESTRUCTURA DEL PROGRAMA
infoEmpleados = open("Persistencia de Datos\Ejercicios\datos-de-empleados-programa\datos-empleados.dat", "r")
encabezado.append(infoEmpleados.readline())
convertirToLista = list(infoEmpleados)


for i in range(len(convertirToLista)):
    listaInfoEmpleados.append(convertirToLista[i].split(","))
infoEmpleados.close()

    
#Mostrar Info Empleado
print("\n")
id, nombre, edad, sexo, telefono = encabezado[0].split(",")

print("{:<13} {:<30} {:<4} {:<3} {:<12}".format(id, nombre, edad, sexo, telefono), end="-" * 61)
print("")

for f in range(len(listaInfoEmpleados)):
    idUser, nombreUser, edadUser, sexoUser, telefonoUser = listaInfoEmpleados[f]
    print("{:<13} {:<30} {:<4} {:<3} {:<12}".format(idUser, nombreUser, edadUser, sexoUser, telefonoUser), end="")

print("")