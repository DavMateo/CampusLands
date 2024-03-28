# Este programa es un videojuego del clásico Piedra, Papel o Tijera en el cuál el jugador (mediante consola) podrá
# enfrentarse contra la computadora o contra otro jugador. Contará también con tabla de clasificación local y global.


# IMPORTANDO LAS LIBRERÍAS INDISPENSABLES
import random
import json
import time
import colorama


# DECLARANDO LAS VARIABLES NECESARIAS
rutaFileConfig = "Ejercicios adicionales/PiedraPapelTijera/data/config.json"
lstKeysPersonalizados = []
isVerdadero = True
iniciandoSistema = True
configMod = False


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS
def filtrarTexto(texto):
    textoFinalArray = []
    
    for i in range(len(texto)):
        if texto[i] != "":
            textoFinalArray.append(texto[i])
    
    textoValidar = "".join(textoFinalArray)
    textoFinal = " ".join(textoFinalArray)
    
    return [textoValidar, textoFinal]


def accederConfig(rutaFileLocal, rutaFileGlobal, dictInfoReturn, lstConfigDefault, checked=False):
    print("DICTINFORETURN: ", dictInfoReturn) #eliminarLuego
    countError = 0
    continuarConfig = True
    
    #Verificando que el jugador ya tenga una configuración previamente aplicada al juego
    if (rutaFileLocal == "" and rutaFileGlobal == "") or checked:
        opcionUsuarioConfig = validarOpcionUsuario(">> ¿Desea configurar la app (Escribir 1) o quieres aplicar la configuración por defecto? (Escribir 0): ", 0, 1)
        
        #Si el jugador desea aplicar una configuración personalizada, entonces:

        if opcionUsuarioConfig == 1:
            #El bucle while es por si acaso el usuario desea configurar más parámetros del juego
            while continuarConfig:
                opcionElegida, configuracionAplicada = configuracion("Ejercicios adicionales/PiedraPapelTijera/data", "Ejercicios adicionales/PiedraPapelTijera/data", ">> ¿Cómo quieres que se llame la IA?: ", ">> ¿Cuántas rondas deseas que tenga una partida? (Default 3 rondas): ")
                
                if opcionElegida == 1:
                    rutaFileLocal = configuracionAplicada
                    print("\nCONFIG:", rutaFileLocal) #eliminarLuego
                    dictInfoReturn[str(opcionElegida)] = rutaFileLocal
                
                elif opcionElegida == 2:
                    rutaFileGlobal = configuracionAplicada
                    print("\nCONFIG:", rutaFileGlobal) #eliminarLuego
                    dictInfoReturn[str(opcionElegida)] = rutaFileGlobal
                
                elif opcionElegida == 3:
                    nombreIA = configuracionAplicada
                    print("\nCONFIG:", nombreIA) #eliminarLuego
                    dictInfoReturn[str(opcionElegida)] = nombreIA
                
                elif opcionElegida == 4:
                    numRondas = configuracionAplicada
                    print("\nCONFIG:", numRondas) #eliminarLuego
                    dictInfoReturn[str(opcionElegida)] = numRondas
                
                elif opcionElegida == 5:
                    continuarConfig = False
                    return False
                
                #Preguntarle al jugador si ya ha terminado de realizar las configuraciones pertinentes
                continuar = validarOpcionUsuario(">> ¿Desea configurar o modificar otro parámetro? (1 SI / 0 NO): ", 0, 1)
                
                if continuar == 1:
                    continue
                elif continuar == 0:
                    continuarConfig = False
                    
                    #Verificar que el archivo de configuración se haya guardado correctamente
                    try:
                        dictInfoConfig = validarAbrirInfoArchivo(rutaFileConfig, dictInfoReturn, True)
                        
                        #Comprobar la información nueva añadida y reemplazarla en la información recibida del archivo "config.json"
                        # dictInfoConfigKeys = list(dictInfoConfig.keys())
                        # try:
                        for key in list(dictInfoReturn.keys()):
                            for j in range(len(dictInfoConfig)):
                                if dictInfoReturn[key] != dictInfoConfig[str(j+1)] and key == str(j+1):
                                    pass
                                else:
                                    dictInfoReturn[str(j+1)] = dictInfoConfig[str(j+1)]                
                    
                        if validarEscribirInfoArchivo(rutaFileConfig, dictInfoReturn) != False:
                            return dictInfoReturn
                        else:
                            print("Error: La configuración aplicada no fue guardada. Inténtelo de nuevo.\n")
                            countError += 1
                            if countError == 3:
                                return None
                            continue
                        
                    except TypeError as e:
                        print("Error: La configuración aplicada no fue guardada. Inténtelo de nuevo")
                        print(f"Error: {e}.\n")
                        countError += 1
                        if countError == 3:
                            return None
                        continue
        
        #Si el jugador desea una configuración por defecto, entonces:
        elif opcionUsuarioConfig == 0:
            for i in range(len(lstConfigDefault)):
                dictInfoReturn[str(i+1)] = lstConfigDefault[i]
            
            #Verificar que el archivo de configuración se haya guardado correctamente
            if validarEscribirInfoArchivo(rutaFileConfig, dictInfoReturn):
                return dictInfoReturn
            else:
                print("Error: No se ha podido cargar la configuración predeterminada. Inténtelo de nuevo.\n")
                return None
    else:
        dictInfoReturn = validarAbrirInfoArchivo(rutaFileConfig, dictInfoReturn)
        return dictInfoReturn


def organizarInfoDicts(dictJuego, tipoOrden):
    checkedOrdenId = False
    lstValuesdictJuego = []
    lstKeysdictJuego = list(dictJuego.keys())
    
    for i in range(len(lstKeysdictJuego)):
        lstValuesdictJuego.append(list(dictJuego[lstKeysdictJuego[i]].values()))
        lstValuesdictJuego[i].insert(0, lstKeysdictJuego[i])
        
    
    #Inicio del algoritmo de ordenamiento burbuja
    for i in range(0, len(lstValuesdictJuego) - 1):
        for j in range(i+1, len(lstValuesdictJuego)):
            if tipoOrden == "id":
                if lstValuesdictJuego[i][0] > lstValuesdictJuego[j][0]:
                    t = lstValuesdictJuego[i]
                    lstValuesdictJuego[i] = lstValuesdictJuego[j]
                    lstValuesdictJuego[j] = t
                    checkedOrdenId = True
            
            elif tipoOrden == "username":
                if lstValuesdictJuego[i][1] > lstValuesdictJuego[j][1]:
                    t = lstValuesdictJuego[i]
                    lstValuesdictJuego[i] = lstValuesdictJuego[j]
                    lstValuesdictJuego[j] = t
            
            elif tipoOrden == "puntaje":
                if lstValuesdictJuego[i][2] > lstValuesdictJuego[j][2]:
                    t = lstValuesdictJuego[i]
                    lstValuesdictJuego[i] = lstValuesdictJuego[j]
                    lstValuesdictJuego[j] = t
            
            elif tipoOrden == "tiempo":
                if lstValuesdictJuego[i][3] > lstValuesdictJuego[j][3]:
                    t = lstValuesdictJuego[i]
                    lstValuesdictJuego[i] = lstValuesdictJuego[j]
                    lstValuesdictJuego[j] = t
    
    if checkedOrdenId:
        for i in range(len(lstValuesdictJuego)):
            lstValuesdictJuego[i].pop(0)
    
    #Asociar las claves de la información del JSON a sus valores correspondientes
    try:
        for i in range(len(lstKeysdictJuego)):
            for j in range(len(dictJuego)):
                if lstValuesdictJuego[i] == list(dictJuego[lstKeysdictJuego[j]].values()):
                    lstValuesdictJuego[i].insert(0, lstKeysdictJuego[j])
    
    except KeyError:
        print("Error: El ID no corresponde a ningún elemento registrado. Inténtelo de nuevo.\n")
        pass
            
    print(lstValuesdictJuego) #eliminarLuego
    return lstValuesdictJuego


def rellenarInfoConfig(dictConfig, checkedError, isVerdadero):
    if dictConfig != False:
        #Rellenar la información en blanco con la configuración predeterminada en caso de que el 
        #usuario no rellene algún campo
        lstKeysPersonalizados = organizarIdList(keysPersonalizados(dictConfig))
        print("LSTKEYSPERSONALIZADOS", lstKeysPersonalizados, len(lstKeysPersonalizados)) #eliminarLuego
        count = 0
        for i in range(len(lstConfigDefault)):
            try:
                if str(i+1) == lstKeysPersonalizados[count]:
                    count += 1
                else:
                    dictConfig[str(i+1)] = lstConfigDefault[i]
                
            except IndexError:
                for j in range(i, len(lstConfigDefault)):
                    dictConfig[str(j+1)] = lstConfigDefault[j]
                
                #Verificar que la información se haya cargado correctamente
                if validarEscribirInfoArchivo(rutaFileConfig, dictConfig):
                    break
                else:
                    checkedError: False
                    isVerdadero = False
                    input("Error: La configuración aplicada no fue guardada. Inténtelo de nuevo.\n")
                    break
        
    elif dictConfig == None:
        checkedError = True
        isVerdadero = False
        input("Error: La configuración aplicada no fue guardada. Inténtelo de nuevo.\n")
    
    elif not dictConfig:
        input("Regresando al menú principal. Presione Enter para continuar...")
        return False
    
    return [dictConfig, checkedError, isVerdadero]
    # return False #eliminarLuego


def organizarIdList(lstId):
    #Inicio del algoritmo de ordenamiento burbuja
    for i in range(0, len(lstId)):
        for j in range(i+1, len(lstId)):
            if lstId[i] > lstId[j]:
                t = lstId[i]
                lstId[i] = lstId[j]
                lstId[j] = t
                
    print("LSTID: ", lstId) #eliminarLuego
    return lstId


def keysPersonalizados(dictConfig):
    lstDictConfigKeys = list(dictConfig.keys())
    index = 0
    
    #Este bucle tiene como objetivo principal evaluar si hay valores personalizados o no dentro
    #del archivo "config.json" para que así, si el usuario realiza modificaciones en configuración
    #esta no sea sobreescrita
    for i in range(len(lstDictConfigKeys)):
        #Buscará dentro de "lstConfigDefault" el índice correcto para evaluar la condición principal
        for j in range(len(lstConfigDefault)):
            if dictConfig[lstDictConfigKeys[i]] == lstConfigDefault[j]:
                index = j  #Toma el índice necesario de "lstConfigDefault"
                break
        
        if dictConfig[lstDictConfigKeys[i]] != lstConfigDefault[index]:
            lstKeysPersonalizados.append(lstDictConfigKeys[i])
    
    print("LISTA DE CLAVES PERSONALIZADAS:", lstKeysPersonalizados) #eliminarLuego
    return lstKeysPersonalizados
            

# DEFINIENDO LAS FUNCIONES DE VALIDACIÓN
def validarOpcionUsuario(msj, min, max):
    while True:
        try:
            opcionUsuario = int(input(msj))
            
            if opcionUsuario < min or opcionUsuario > max:
                print(f"Error: Debes elegir una opción numérica dentro del rango válido ({min}-{max}).\n")
                continue
            return opcionUsuario
        
        except ValueError:
            print("Ha ocurrido un error al ingresar la opción seleccionada. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarAbrirInfoArchivo(rutaFileJson, dictJuego, checked=False):
    #Validación n°1 - Intentar abrir el archivo en modo lectura / escritura
    try:
        intentarAbrirArchivo = open(rutaFileJson, "r")
    
    except Exception as e:
        try:
            intentarAbrirArchivo = open(rutaFileJson, "w")
        
        except Exception as d:
            print("Ha ocurrido un problema al intentar abrir el archivo necesario.")
            print(f"Error: {d}.\n")
            return False
    intentarAbrirArchivo.close()
    
    
    #Validación n°2 - Recibir la información del archivo ".json" al ejecutarse el programa
    try:
        abrirArchivo = open(rutaFileJson, "r")
        
        #Si checked es falso entonces ejecutar el siguiente código normal
        if not checked:
            linea = abrirArchivo.readline()
            if linea.strip() != "":
                abrirArchivo.seek(0)
                dictJuego.update(json.load(abrirArchivo)) #problema1
            else:
                dictJuego = {}
        
        #De lo contrario, si checked es verdadero entonces ejecutar el fragmento de código anterior con una variante en "json.load()"
        elif checked:
            linea = abrirArchivo.readline()
            if linea.strip() != "":
                abrirArchivo.seek(0)
                dictJuego = json.load(abrirArchivo) #problema1
            else:
                dictJuego = {}
    
    except Exception as e:
        print("Ha ocurrido un problema al intentar recuperar la información del sistema.")
        print(f"Error: {e}.\n")
        return False
    
    return dictJuego


def validarEscribirInfoArchivo(rutaFileJson, dictJuego):
    #Validación n°1 - Abrir el archivo en modo escritura
    try:
        guardarInfo = open(rutaFileJson, "w")
    
    except Exception as e:
        print("Ha ocurrido un problema al ejecutarse la función de guardado.")
        print(f"Error: {e}.\n")
        return False

    
    #Validación n°2 - Escribir la información en el archivo correspondiente
    try:
        json.dump(dictJuego, guardarInfo)
    
    except Exception as e:
        print("Ha ocurrido un problema al guardar la información del libro ingresado.")
        print(f"Error: {e}.\n")
        return False
    
    guardarInfo.close()
    return True


def validarCodigo(msj, min, max):
    while True:
        try:
            codigo = input(msj).strip()
            codigoArray = codigo.split(" ")
            
            if len(codigoArray) < min or len(codigoArray) > max:
                print(f"Error: El código introducido no puede ser menor ni mayor a {min}-{max} palabras.\n")
                continue
            codigoValidar, codigoFinal = filtrarTexto(codigoArray)
            
            if not codigoValidar.isalnum() or len(codigoValidar) == 0:
                print("Error: El código no puede estar vacío ni contener caracteres especiales.\n")
                continue
            return codigoFinal
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar el código. Inténtelo de nuevo.\n")
            print(f"Error: {e}.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


def validarTexto(msj, min):
    while True:
        try:
            texto = input(msj).strip()
            textoArray = texto.split(" ")
            
            if len(textoArray) < min:
                print(f"Error: El texto debe contener al menos {min} palabras.\n")
                continue
            textoValidar, textoFinal = filtrarTexto(textoArray)
            
            if textoValidar.isdigit() or not textoValidar.isalnum() or len(textoValidar) == 0:
                print("Error: El texto ingresado no puede estar vacío, componerse de solo números o contener caracteres especiales.\n")
                continue
            return textoFinal
        
        except Exception as e:
            print("Ha ocurrido un problema al ingresar el texto. Inténtelo de nuevo.\n")
            print(f"Error: {e}.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("\n\n", "JUEGO PIEDRA-PAPEL-TIJERA".center(20))
    print("MENU".center(26))
    
    print(colorama.Style.DIM + "1. Tutorial")
    print("2. Jugador vs IA")
    print("3. Jugador vs Jugador")
    print("4. Tabla de clasificación")
    print("5. Configuración")
    print("6. Salir")
    return validarOpcionUsuario(msj, 1, 6)


def inicializarPrograma(rutaFileLocal, dictJugadorIA, rutaFileGlobal, dictJugadores):
    return [0, 0]


def configuracion(rutaFileGlobal, rutaFileLocal, nameIA, rondasNum):
    print("\n==== CONFIGURACIÓN ====")
    print("1. Ruta personalizada de estadísticas Player vs IA")
    print("2. Ruta personalizada del registro de victorias Player vs Player")
    print("3. Darle un nombre a la IA")
    print("4. Cambiar el número de rondas por partida")
    print("5. Regresar al menú principal")
    opcionUsuario = validarOpcionUsuario(">> Digite una opción: ", 1, 5)
    
    # Estructura de la configuración del programa
    if opcionUsuario == 1:
        print("\n", colorama.Fore.BLUE + "*** RUTA ARCHIVO PvE ***")
        nombreArchivo = validarTexto(colorama.Fore.WHITE + "¿Cómo desea llamar al archivo?: ", 1)
        rutaFileAI = f"{rutaFileLocal}" + f"/{nombreArchivo}.json"
        
        return [opcionUsuario, rutaFileAI]
    
    elif opcionUsuario == 2:
        print("\n", colorama.Fore.BLUE + "*** RUTA ARCHIVO PvP ***")
        nombreArchivo = validarTexto(colorama.Fore.WHITE + "¿Cómo desea llamar al archivo?: ", 1)
        rutaFilePvP = f"{rutaFileGlobal}" + f"/{nombreArchivo}.json"
        
        return [opcionUsuario, rutaFilePvP]
    
    elif opcionUsuario == 3:
        print("\n", colorama.Fore.BLUE + "*** NOMBRE IA ***")
        return [opcionUsuario, validarTexto(colorama.Fore.WHITE + nameIA, 1)]
    
    elif opcionUsuario == 4:
        print("\n", colorama.Fore.BLUE + "*** RONDAS POR PARTIDA ***")
        return [opcionUsuario, validarOpcionUsuario(colorama.Fore.WHITE + rondasNum, 1, 30)]
    
    elif opcionUsuario == 5:
        input("\nRegresando al menú principal. \nPresione cualquier tecla para continuar...")
        return [opcionUsuario, False] 


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    while iniciandoSistema:
        dictInfoConfig = validarAbrirInfoArchivo(rutaFileConfig, {})
        lstConfigDefault = ["Ejercicios adicionales/PiedraPapelTijera/data/datosLocal.json/", "Ejercicios adicionales/PiedraPapelTijera/data/datosGlobal.json", "Computadora", 3]
        checkedError = False
        
        #Asignarle a las variables de "rutaFile" la ruta del archivo. Si no existe, se configura como una
        #ruta vacía y el usuario decidirá si lo configura o aplica una configuración predeterminada.
        try:
            rutaFileLocal = dictInfoConfig["1"]
            rutaFileGlobal = dictInfoConfig["2"]
        except KeyError:
            rutaFileLocal = ''
            rutaFileGlobal = ''
            
                
        #Escribir la configuración del juego en el archivo JSON
        dictConfig = accederConfig(rutaFileLocal, rutaFileGlobal, {}, lstConfigDefault)
        # if rutaFileLocal == "" and rutaFileGlobal == "":
        #     rutaFileLocal = dictInfoConfig["1"]
        #     rutaFileGlobal = dictInfoConfig["2"]
        # #Lo anterior es en caso de que aún no haya nada escrito en las rutas.
        
        print("RESULTADO DICTCONFIG:", dictConfig) #eliminarLuego
        try:
            # dictConfig = False  #eliminarLuego
            dictConfig, checkedError, isVerdadero = rellenarInfoConfig(dictConfig, checkedError, isVerdadero)
        except TypeError as e:
            print("PASÉ POR EL EXCEPT!") #eliminarLuego
            print(e) #eliminarLuego
            pass
        
        
        #Inicializando el juego
        dictJugadorIA, dictJugadores = inicializarPrograma(rutaFileLocal, {}, rutaFileGlobal, {})
        break
    
    
    if not checkedError:
        iniciandoSistema = False
        opcionUsuario = menu("   >> Elija una opción: ")
        
        if opcionUsuario == 1:
            pass
        
        elif opcionUsuario == 2:
            pass
        
        elif opcionUsuario == 3:
            pass
        
        elif opcionUsuario == 4:
            pass
        
        elif opcionUsuario == 5:
            dictConfig = accederConfig(rutaFileLocal, rutaFileGlobal, {}, lstConfigDefault, True)
            print("\nOPCION 5 - RESULTADO DICTCONFIG:", dictConfig) #eliminarLuego
            try:
                # dictConfig = False  #eliminarLuego
                dictConfig, checkedError, isVerdadero = rellenarInfoConfig(dictConfig, checkedError, isVerdadero)
            except TypeError as e:
                print("PASÉ POR EL EXCEPT!") #eliminarLuego
                print(e) #eliminarLuego
                pass
        
        elif opcionUsuario == 6:
            isVerdadero = False
            input("\nSaliendo...")


#CORREGIR:
#   1. Verificar la actualización del diccionario en la función de "accederConfig()". El problema muy posiblemente se encuentre ahí.