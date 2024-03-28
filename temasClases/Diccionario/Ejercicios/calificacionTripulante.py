# Este programa permitirá calcular la nota definitiva de un estudiante en base a 
# otras calificaciones con un peso determinado.


# DEFINIENDO LAS VARIABLES PRINCIPALES
isVerdadero = True
aprobar = False
count = 0
notasEstudiante = []
infoEstudianteLista = [] # Esta lista se destructurará para convertirse en un objeto. Se apoyará con el uso de otra lista.
infoEstudianteTransitoria = []
listaNotas = []
listanombreFinal = []
nombreArray = []
informacionEstudiante = {}


# DEFINIENDO LAS FUNCIONES
def vaciarLista():
    global listaNotas
    global infoEstudianteLista
    global infoEstudianteTransitoria
    global nombreArray
    global listanombreFinal
    # Uso la palabra reservada Global para indicarle a Python que deseo modificar una variable que ha 
    # sido declarada por fuera de la función actual.
    
    listaNotas = list()
    infoEstudianteTransitoria = list()
    infoEstudianteLista = list()
    nombreArray = list()
    listanombreFinal = list()

def calculoNota(nota, peso, id):
    while True:
        try:
            calificacion = float(input(nota))
            
            if calificacion < 0.0 or calificacion > 5.0:
                print("Error: La nota ingresada es incorrecta. Asegúrese de introducir un valor entre 0.0 a 5.0.\n")
                continue
            
            listaNotas.append(calificacion)
            break
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la(s) nota(s). Inténtelo de nuevo.\n")
        
        
    while True:
        try:
            pesoPorcentaje = int(peso)
            
            if pesoPorcentaje < 0 or pesoPorcentaje > 100:
                print("Error: El peso ingresado es incorrecto. Asegúrese de introducir un valor entre 0 a 100.\n")
                continue
            
            listaNotas.append(pesoPorcentaje)
            break
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el peso de la nota. Inténtelo de nuevo.\n")


    if len(listaNotas) == 6:
        notaDefinitiva(listaNotas, id)


def notaDefinitiva(notas, id):
    notaPromedio = ((notas[0] * notas[1]) + (notas[2] * notas[3]) + (notas[4] * notas[5])) / 100
    infoEstudianteLista.append(notaPromedio)
    
    if notaPromedio >= 3.0:
        aprobar = True
    elif notaPromedio <= 2.9:
        aprobar = False
    
    infoEstudianteLista.append(aprobar)
    datosEstudiante(infoEstudianteLista, id)


def datosEstudiante(informacion, id):    
    for i in range(1, len(informacion)):
        infoEstudianteTransitoria.append(infoEstudianteLista[i])
    
    informacionEstudiante[id] = infoEstudianteTransitoria
    print(informacionEstudiante)
    vaciarLista()


# ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    # Verificación código
    while True:
        try:
            codigo = int(input("\nIngrese el código (Escriba 999 para salir): "))
            
            if codigo < 0:
                print("Error: El código no puede ser menor que 0.\n")
                continue
            
            infoEstudianteLista.append(codigo)
            break
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el código. Inténtelo de nuevo.\n")
    
    if codigo == 999:
        isVerdadero = False
    
    
    # Verificación nombre
    while isVerdadero:
        try: 
            nombre = input("Ingrese el nombre: ").strip()
            nombreArray = nombre.split(" ")
            
            # Algoritmo para filtrar y verificar el ingreso de nombres al programa
            for i in range(len(nombreArray)):
                if nombreArray != "":
                    listanombreFinal.append(nombreArray[i])
                        
            nombreFinalVerificacion = "".join(listanombreFinal).lower()
            nombreFinal = " ".join(listanombreFinal).title()
            nombreFinalArray = nombreFinal.split(" ")
            
            if len(nombreFinalVerificacion) == 0 or not nombreFinalVerificacion.isalnum() or len(nombreFinalArray) < 2:
                print("Error: Introduce un nombre válido.\n")
                listanombreFinal = list()
                continue
            
            infoEstudianteLista.append(nombreFinal)
            break
        
        except Exception as e:
            print(f"Ha ocurrido un problema. Error: {e}\n")
    
    
    # Verificación nota
    while isVerdadero:
        for i in range(3):
            if i == 0 or i == 1:
                pesoNota = 30
            elif i == 2:
                pesoNota = 40
            
            calculoNota(f"Ingrese la nota {i+1}: ", pesoNota, codigo)
        break
    
    while isVerdadero:
        claves = informacionEstudiante.keys()
        
        print("\n", "=" * 35)
        print("\tINFORMACIÓN ESTUDIANTE")
        print(f"Estudiante: {informacionEstudiante[codigo][0]}")
        print(f"Código: {[*claves][count]}")  
            # El símbolo de asterísco significa que se desempaqueta en una lista la información contenida en la variable "claves"
        print(f"La nota promedio del estudiante es de: {informacionEstudiante[codigo][1]}/5.0")
        
        if informacionEstudiante[codigo][2]:
            print(f"¡El estudiante SI aprobó el curso!")
        else:
            print(f"El estudiante reprobó el curso.")
        
        
        input("\nPresione cualquier tecla para continuar...")
        count += 1
        break
    
    while not isVerdadero:
        input("Presione cualquier tecla para salir...")
        break

print("\n", "¡Gracias por usar nuestro software!")