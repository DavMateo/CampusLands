# Este programa permite recibir y gestionar información meteorológica recibida por múltiples
# estaciones meteorológicas a nivel nacional.


# IMPORTANDO LAS LIBRERIAS INDISPENSABLES
import json


# DECLARANDO LAS VARIABLES NECESARIAS
isVerdadero = True
inicializandoSistema = True


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS
def filtrarTexto(texto):
    textoArray = texto.split(" ")
    textoFiltradoArray = []
    
    for i in range(len(textoArray)):
        if textoArray[i] != "":
            textoFiltradoArray.append(textoArray[i])
    
    return textoFiltradoArray


def existeCodigo(id, dictObservatorios):
    validarExisteId = dictObservatorios.get(id)
    
    if validarExisteId == None:
        return False
    else:
        return True


def organizarInfoObservatorio(dictObservatorios, tipoOrden):
    checkedOrdenCod = False
    lstKeysdictObservatorios = list(dictObservatorios.keys())
    lstValuesdictObservatorios = []
    

    for i in range(len(lstKeysdictObservatorios)):
        lstValuesdictObservatorios.append(list(dictObservatorios[lstKeysdictObservatorios[i]].values()))
        lstValuesdictObservatorios[i].insert(0, lstKeysdictObservatorios[i])
        
    
    #Inicio del algoritmo de ordenamiento burbuja
    for i in range(0, len(lstValuesdictObservatorios) - 1):
        for j in range(i+1, len(lstValuesdictObservatorios)):
            if tipoOrden == "codigo":
                if lstValuesdictObservatorios[i][1] > lstValuesdictObservatorios[j][1]:
                    t = lstValuesdictObservatorios[i]
                    lstValuesdictObservatorios[i] = lstValuesdictObservatorios[j]
                    lstValuesdictObservatorios[j] = t
                    checkedOrdenCod = True
            
            elif tipoOrden == "nombre":
                if lstValuesdictObservatorios[i][2] > lstValuesdictObservatorios[j][2]:
                    t = lstValuesdictObservatorios[i]
                    lstValuesdictObservatorios[i] = lstValuesdictObservatorios[j]
                    lstValuesdictObservatorios[j] = t
            
            elif tipoOrden == "fecha":
                if lstValuesdictObservatorios[i][5] > lstValuesdictObservatorios[j][4]:
                    t = lstValuesdictObservatorios[i]
                    lstValuesdictObservatorios[i] = lstValuesdictObservatorios[j]
                    lstValuesdictObservatorios[j] = t
            
            elif tipoOrden == "temperaturaMinima":
                if lstValuesdictObservatorios[i][3] > lstValuesdictObservatorios[j][3]:
                    t = lstValuesdictObservatorios[i]
                    lstValuesdictObservatorios[i] = lstValuesdictObservatorios[j]
                    lstValuesdictObservatorios[j] = t
            
            elif tipoOrden == "temperaturaMaxima":
                if lstValuesdictObservatorios[i][4] > lstValuesdictObservatorios[j][4]:
                    t = lstValuesdictObservatorios[i]
                    lstValuesdictObservatorios[i] = lstValuesdictObservatorios[j]
                    lstValuesdictObservatorios[j] = t
    
    if checkedOrdenCod:
        for i in range(len(lstValuesdictObservatorios)):
            lstValuesdictObservatorios[i].pop(0)
    
    
    #Asociar las claves de los libros a sus valores correspondientes
    try:
        for i in range(len(lstKeysdictObservatorios)):
            for j in range(len(dictObservatorios)):
                if lstValuesdictObservatorios[i] == list(dictObservatorios[lstKeysdictObservatorios[j]].values()):
                    lstValuesdictObservatorios[i].insert(0, lstKeysdictObservatorios[j])
    
    except KeyError:
        print("Error: El código no corresponde a ningún observatorio registrado. Inténtelo de nuevo.\n")
        pass
    
    return lstValuesdictObservatorios


def ordenarInfoArchivo(dictObservatorios):
    lstConvDict = []
    lstValuedictObservatorioOrdenado = organizarInfoObservatorio(dictObservatorios, "codigo")
    
    for i in range(len(lstValuedictObservatorioOrdenado)):
        lstValuedictObservatorioOrdenado[i].pop(0)
        codTupla, nomTupla, temp, fechaTupla = lstValuedictObservatorioOrdenado[i]
        lstConvDict.append((codTupla, {'codigo': codTupla, 'nombre': nomTupla, 'temperatura': temp, 'fecha': fechaTupla}))
    
    dictObservatorios = {}
    dictObservatorios = dict(lstConvDict)
    return dictObservatorios



def recibirInformacion(rutaCsv, rutaFile):
    infoClima = open(rutaCsv, "r")
    encabezado = infoClima.readline()
    convertirToLista = list(infoClima)
    lstEncabezado = []
    lstInfoClima = []
    lstTemps = []


    for i in range(len(convertirToLista)):
        lstInfoClima.append(convertirToLista[i].split(";"))

    lstEncabezado.append(encabezado.split(";"))
    infoClima.close()

    for i in range(len(lstInfoClima)):
        lstTemps.append(lstInfoClima[i][2])

    return convertirToDict(rutaFile, lstEncabezado, lstInfoClima, lstTemps)


def convertirToDict(rutaFile, lstEncabezado, lstInfoClima, lstTemps):
    dictObservatorioInfo = {}
    codigoTit, nombreTit, tempTit, fechaTit = lstEncabezado[0]

    for i in range(len(lstInfoClima)):
        codigo, nombre, temp, fecha = lstInfoClima[i]

        dictObservatorioInfo[lstInfoClima[i][0]] = {
            codigoTit.lower(): codigo, 
            nombreTit.lower(): nombre.title(),
            tempTit.lower(): lstTemps,
            fechaTit.lower(): fecha
        }
    
    return dictObservatorioInfo


def mostrarListaObservatorios(dictObservatorios, tipoOrden, paginacion = 0):
    lstValoresObservatoriosOrdenados =  organizarInfoObservatorio(dictObservatorios, f"{tipoOrden}")
    # lstKeysDictLibros = list(dictLibros.keys())
    

    print(f"\n==== ORDENAR POR {tipoOrden.upper()} ====\n")

    if paginacion == 0:
        print("{:<8} {:<10} {:<25} {:<10} {:<10} {:<12} {:<10}".format("N°", "CÓDIGO", "NOMBRE DEL OBSERVATORIO", "TEMP MIN", "TEMP MAX", "FECHA", "PROMEDIO"))
        
        for i in range(len(dictObservatorios)):
            try:
                # codigoLibro = lstKeysDictLibros[i]
                lstValoresObservatoriosOrdenados[i].pop(0)
                codigo, nombre, temp, fecha = lstValoresObservatoriosOrdenados[i]
                print("{:<8} {:<12} {:<30} {:<10} {:<10} {:<12}".format(i+1, codigo, nombre, tempMin(temp), tempMax(temp), fecha))
            
            except IndexError:
                break
    
    else:
        limitePaginacion = paginacion
        inicioBucle = 0
        checked = False

        if len(dictObservatorios) <= paginacion:  #En caso de error cambiar a 10
            print("{:<8} {:<10} {:<25} {:<10} {:<10} {:<12} {:<10}".format("N°", "CÓDIGO", "NOMBRE DEL OBSERVATORIO", "TEMP MIN", "TEMP MAX", "FECHA", "PROMEDIO"))
            
            for i in range(paginacion):
                try:
                    # codigoLibro = lstKeysDictLibros[i]
                    codigo, nombre, temp, fecha = lstValoresObservatoriosOrdenados[i]
                    print("{:<8} {:<10} {:<25} {:<10} {:<10} {:<12} {:<10}".format(i+1, codigo, nombre, tempMin(temp), tempMax(temp), fecha, promediar(temp)))
                
                except IndexError:
                    break
        
        else:
            print("{:<8} {:<10} {:<25} {:<10} {:<10} {:<12} {:<10}".format("N°", "CÓDIGO", "NOMBRE DEL OBSERVATORIO", "TEMP MIN", "TEMP MAX", "FECHA", "PROMEDIO"))
            
            while True:
                for i in range(inicioBucle, limitePaginacion):
                    try:
                        # codigoLibro = lstKeysDictLibros[i]

                        lstValoresObservatoriosOrdenados[i].pop(0)
                        codigo, nombre, temp, fecha = lstValoresObservatoriosOrdenados[i]
                        print("{:<8} {:<10} {:<25} {:<10} {:<10} {:<12} {:<10}".format(i+1, codigo, nombre, tempMin(temp), tempMax(temp), fecha, promediar(temp)))
                        
                        if i+1 == limitePaginacion:
                            break
                    
                    except IndexError:
                        checked = True
                        break
                
                if checked:
                    break
                else:
                    continuarListaLibros = validarOpcionUsuario("\n>> ¿Deseas listar más datos? (1 SI / 0 NO): ", 0, 1)
                    print("")
                    
                    if continuarListaLibros == 0:
                        break
                    elif continuarListaLibros == 1:
                        #Estas variables establecen el rango de inicio y fin en el bucle for
                        inicioBucle = limitePaginacion
                        limitePaginacion += paginacion
                        continue


def consultarObs(cod, dictObservatorios):
    print("\n*** CONSULTAR OBSERVATORIO ***\n")
    
    while True:
        verificarExisteobservatorio = existeObservatorio(cod, dictObservatorios)
        
        if verificarExisteobservatorio == False:
            print("Error: El código ingresado no corresponde a ningún observatorio registrado. Inténtelo de nuevo.\n")
            volverIntentar = validarOpcionUsuario(">> ¿Desea volver a buscar el observatorio? (1 SI / 0 NO): ", 0, 1)
            
            if volverIntentar == 1:
                input("Asegúrate de que el código está escrito correctamente...")
                continue
            elif volverIntentar == 0:
                input("Regresando al menú principal. Presione cualquier tecla para continuar...")
                break
        
        else:
            codTab, nomTab, tempTab, fechaTab = list(verificarExisteobservatorio[1].keys())
            cod, nom, temp, fecha = list(verificarExisteobservatorio[1].values())

            print(f"\n==== {codTab.title()}: {cod} ====")
            print(f"{nomTab.upper()}: {nom.title()}")
            print(f"{f'{tempTab} MINIMA'.upper()}: {tempMin(temp)}ºC")
            print(f"{f'{tempTab} MAXIMO'.upper()}: {tempMax(temp)}ºC")
            print(f"{fechaTab.upper()}: {fecha}")
        
        
        seguirConsultando = validarOpcionUsuario("\n>> ¿Deseas consultar otro observatorio? (1 SI / 0 NO): ", 0, 1)
        
        if seguirConsultando == 1:
            continue
        elif seguirConsultando == 0:
            input("Presione cualquier tecla para regresar al menú...")
            break


def existeObservatorio(cod, dictObservatorios, checked=False):
    if checked:
        validarExisteLibro = dictObservatorios.get(cod)
    else:
        codigo = validarCodigo(cod, 1, True)
        validarExisteLibro = dictObservatorios.get(codigo)
    
    
    if validarExisteLibro == None:
        return False
    else: 
        return codigo, validarExisteLibro


def promedio(dictObservatorios, cod):
    print("\n==== PROMEDIO ====\n")
    print("{:<8} {:<10} {:<25} {:<10} {:<10} {:<12} {:<10}".format("N°", "CÓDIGO", "NOMBRE DEL OBSERVATORIO", "TEMP MIN", "TEMP MAX", "FECHA", "PROMEDIO"))


    print("{:<8} {:<10} {:<25} {:<10} {:<10} {:<12} {:<10}".format(1, dictObservatorios[cod]["codigo"], dictObservatorios[cod]["nombre"], tempMin(dictObservatorios[cod]["temperatura"]), tempMax(dictObservatorios[cod]["temperatura"]), dictObservatorios[cod]["fecha"], promediar(dictObservatorios[cod]["temperatura"])))


def promediar(tempDatos):
    sumarPromedio = 0

    for i in range(len(tempDatos)):
        sumarPromedio += float(tempDatos[i])
    
    return sumarPromedio // len(tempDatos)


def tempMin(temp):
    return min(temp)


def tempMax(temp):
    return max(temp)



# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < min or opcionUsuario > max:
                print(f"Error: Debes elegir una opción dentro del rango válido ({min}-{max}).\n")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la opción elegida. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarCodigo(msj, min, checked=False):
    while True:
        try:
            id = input(msj)
            existeCod = existeCodigo(id, dictObservatorios)
            
            if checked:
                pass
                # El pass es con el fin de evitar la validación de si existe un ID específico, pues se quiere que valide que el ID ingresado sea válido pero que no valide si ya existe o no.
            else:
                if existeCod:
                    print(f"Error: El id '{id}' ya existe.\n")
                    continue
                
                else:
                    if id < min:
                        print(f"Error: El ID no puede ser menor que {min}.\n")
                        continue
            return id
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el código del observador. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarNombre(msj, min):
    while True:
        try:
            observatorio = input(msj).strip()
            observatorioFiltradoArray = filtrarTexto(observatorio)
            
            observatorioValidar = "".join(observatorioFiltradoArray).lower()
            observatorioFinal = " ".join(observatorioFiltradoArray).title()
            
            if len(observatorioFiltradoArray) < min:
                print(f"Error: Debes ingresar al menos {min} palabras.\n")
                continue
            
            elif observatorioValidar.isdigit() or not observatorioValidar.isalnum() or len(observatorioValidar) == 0:
                print("Error: El nombre no debe estar compuesto de sólo números ni tener caracteres especiales, solo caracteres alfa-numéricos.\n")
                continue
            
            return observatorioFinal
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar el nombre del observatorio.\n")
            print(f"Error: {e}\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarAbrirInfoArchivo(rutaFile, dictObservatorios):
    #Validación n°1 - Intentar abrir el archivo en modo lectura / escritura
    try:
        intentarAbrirArchivo = open(rutaFile, "r")
    
    except Exception as e:
        try:
            intentarAbrirArchivo = open(rutaFile, "w")
        
        except Exception as d:
            print("Ha ocurrido un problema al intentar abrir el archivo necesario.")
            print(f"Error: {d}.\n")
            return False
    intentarAbrirArchivo.close()
    
    
    #Validación n°2 - Recibir la información del archivo ".json" al ejecutarse el programa
    try:
        abrirArchivo = open(rutaFile, "r")
        
        linea = abrirArchivo.readline()
        if linea.strip() != "":
            abrirArchivo.seek(0)
            dictObservatorios.update(json.load(abrirArchivo))
        
        else:
            dictObservatorios = {}
    
    except Exception as e:
        print("Ha ocurrido un problema al intentar recuperar la información del sistema.")
        print(f"Error: {e}.\n")
        return False
    
    return dictObservatorios


def validarEscribirInfoArchivo(rutaFile, dictObservatorios):
    #Validación n°1 - Abrir el archivo en modo escritura
    try:
        guardarInfo = open(rutaFile, "w")
    
    except Exception as e:
        print("Ha ocurrido un problema al ejecutarse la función de guardado.")
        print(f"Error: {e}.\n")
        return False

    
    #Validación n°2 - Escribir la información en el archivo correspondiente
    try:
        json.dump(dictObservatorios, guardarInfo)
    
    except Exception as e:
        print("Ha ocurrido un problema al guardar la información del observatorio ingresado.")
        print(f"Error: {e}.\n")
        return False
    
    guardarInfo.close()
    return True





# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("\n\n==== SERVICIO METEOROLÓGICO ACME ====")
    print("MENU".center(35))

    print("\n1. Listar observatorios")
    print("2. Consultar un observatorio")
    print("3. Listar datos a nivel nacional")
    print("4. Salir")
    return validarOpcionUsuario(msj, 1, 4)


def inicializarPrograma(rutaFile, csvObservatorio):
    csvObservatorioArchivo = validarAbrirInfoArchivo(rutaFile, csvObservatorio)
    csvObservatorio.update(csvObservatorioArchivo)

    dictObservatorios = ordenarInfoArchivo(csvObservatorio)
    validarEscribirInfoArchivo(rutaFile, dictObservatorios)
    return dictObservatorios


def listarObservatorios(msj, dictObservatorios):
    print("\n*** LISTAR OBSERVATORIOS ***\n")
    print("1. Observatorios ordenados ascendentemente por su código")
    print("2. Observatorios ordenados ascendentemente por su nombre")
    print("3. Salir")
    opcionUsuarioMenu = validarOpcionUsuario(msj, 1, 3)

    if opcionUsuarioMenu == 1:
        mostrarListaObservatorios(dictObservatorios, "codigo")
        input()

    elif opcionUsuarioMenu == 2:
        mostrarListaObservatorios(dictObservatorios, "nombre")
        input()

    elif opcionUsuarioMenu == 3:
        input("Regresando al menú principal...")


def consultarObservatorio(msj, dictObservatorios):
    print("\n*** CONSULTAR OBSERVATORIO ***\n")
    print("1. Consultar observatorio por su código")
    print("2. Información promedio de un observatorio")
    print("3. Salir")
    opcionUsuarioMenu = validarOpcionUsuario(msj, 1, 3)

    if opcionUsuarioMenu == 1:
        consultarObs(">> Ingrese el código del observatorio: ", dictObservatorios)

    elif opcionUsuarioMenu == 2:
        cod = validarCodigo(">> Ingrese el código del observatorio a continuación: ", 1, True)
        promedio(dictObservatorios, cod)
        input()

    elif opcionUsuarioMenu == 3:
        input("Regresando al menú principal...")


def listarDatosObservatorios(msj, dictObservatorios):
    print("\n*** LISTAR DATOS OBSERVATORIOS ***\n")
    print("1. Listar datos a nivel nacional")
    print("2. Listar datos agrupado por observatorio")
    print("3. Salir")
    opcionUsuarioMenu = validarOpcionUsuario(msj, 1, 3)

    if opcionUsuarioMenu == 1:
        mostrarListaObservatorios(dictObservatorios, "codigo", 10)
        input()

    elif opcionUsuarioMenu == 2:
        pass

    elif opcionUsuarioMenu == 3:
        input("Regresando al menú principal...")


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    while inicializandoSistema:
        rutaFile = "Filtro Python/data.json"
        rutaCsv = "Filtro Python/datos.csv"

        csvObservatorio = recibirInformacion(rutaCsv, rutaFile)
        dictObservatorios = inicializarPrograma(rutaFile, csvObservatorio)
        break
    
    inicializandoSistema = False
    opcionUsuario = menu("   >> Ingrese una opción: ")


    #Inicia el llamado a las distintas funcionalidades del programa
    if opcionUsuario == 1:
        listarObservatorios(">> Digite una opción: ", dictObservatorios)

    elif opcionUsuario == 2:
        consultarObservatorio(">> Digite una opción: ", dictObservatorios)

    elif opcionUsuario == 3:
        listarDatosObservatorios(">> Digite una opción: ", dictObservatorios)

    elif opcionUsuario == 4:
        isVerdadero = False
        input("¡Gracias por usar nuestro software!")