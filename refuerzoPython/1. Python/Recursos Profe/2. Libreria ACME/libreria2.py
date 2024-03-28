# Este programa permite llevar el control de los libros presentes en una librería, con toda su
# respectiva información de manera ordenada, almacenada permanentamente en disco.


# IMPORTAR LAS LIBRERÍAS NECESARIAS
import json


# DECLARANDO LAS VARIABLES PRINCIPALES
isVerdadero = True
inicializandoSistema = True
dictLibros = {}


# DEFINIENDO LAS FUNCIONES COMPLEMENTARIAS
def filtrarTexto(texto):
    textoFinalArray = []
    
    for i in range(len(texto)):
        if texto[i] != "":
            textoFinalArray.append(texto[i])
    
    textoValidar = "".join(textoFinalArray)
    textoFinal = " ".join(textoFinalArray)
    
    return [textoValidar, textoFinal]


def organizarInfoLibros(dictLibros, tipoOrden):
    checkedOrdenCod = False
    lstKeysDictLibros = list(dictLibros.keys())
    lstValuesDictLibros = []
    
    for i in range(len(lstKeysDictLibros)):
        lstValuesDictLibros.append(list(dictLibros[lstKeysDictLibros[i]].values()))
        lstValuesDictLibros[i].insert(0, lstKeysDictLibros[i])
        
    
    #Inicio del algoritmo de ordenamiento burbuja
    for i in range(0, len(lstValuesDictLibros) - 1):
        for j in range(i+1, len(lstValuesDictLibros)):
            if tipoOrden == "codigo":
                if lstValuesDictLibros[i][0] > lstValuesDictLibros[j][0]:
                    t = lstValuesDictLibros[i]
                    lstValuesDictLibros[i] = lstValuesDictLibros[j]
                    lstValuesDictLibros[j] = t
                    checkedOrdenCod = True
            
            elif tipoOrden == "titulo":
                if lstValuesDictLibros[i][1] > lstValuesDictLibros[j][1]:
                    t = lstValuesDictLibros[i]
                    lstValuesDictLibros[i] = lstValuesDictLibros[j]
                    lstValuesDictLibros[j] = t
            
            elif tipoOrden == "autor":
                if lstValuesDictLibros[i][2] > lstValuesDictLibros[j][2]:
                    t = lstValuesDictLibros[i]
                    lstValuesDictLibros[i] = lstValuesDictLibros[j]
                    lstValuesDictLibros[j] = t
            
            elif tipoOrden == "precio":
                if lstValuesDictLibros[i][3] > lstValuesDictLibros[j][3]:
                    t = lstValuesDictLibros[i]
                    lstValuesDictLibros[i] = lstValuesDictLibros[j]
                    lstValuesDictLibros[j] = t
    
    if checkedOrdenCod:
        for i in range(len(lstValuesDictLibros)):
            lstValuesDictLibros[i].pop(0)
    
    #Asociar las claves de los libros a sus valores correspondientes
    try:
        for i in range(len(lstKeysDictLibros)):
            for j in range(len(dictLibros)):
                if lstValuesDictLibros[i] == list(dictLibros[lstKeysDictLibros[j]].values()):
                    lstValuesDictLibros[i].insert(0, lstKeysDictLibros[j])
    
    except KeyError:
        print("Error: El código no corresponde a ningún libro registrado. Inténtelo de nuevo.\n")
        pass
            
    return lstValuesDictLibros


def existeLibro(cod, dictLibros, checked=False):
    if checked:
        validarExisteLibro = dictLibros.get(cod)
    else:
        codigo = validarCodigo(cod, 1, 1).upper()
        validarExisteLibro = dictLibros.get(codigo)
    
    
    if validarExisteLibro == None:
        return False
    else: 
        return codigo, validarExisteLibro


def modificarInfoLibro(codigo, infoLibroTab, infoLibroText, infoModVar, infoModText, min, rutaFile, isTexto):
    tituloTab, autorTab, precioTab = infoLibroTab
    tituloLibro, autorLibro, precioLibro = infoLibroText
    
    while True:
        print(f"\n==== {codigo} ====")
        
        #Validar si se debe verificar con "validarTexto()" o con "validarPrecio()" de acuerdo al valor del parámetro "isTexto" (True / False).
        if isTexto:
            print(f"Anterior {infoModText.title()}: {infoModVar}")
            nuevaModificacion = validarTexto(f">> Ingrese el nuevo {infoModText.lower()}: ", min).title()
        else:
            print(f"Anterior {infoModText.title()}: ${infoModVar:,.0f} COP")
            nuevaModificacion = validarPrecio(f">> Ingrese el nuevo {infoModText.lower()}: ", min)


        #Rectificando que el usuario haya ingresado bien la información
        if infoModText.lower() == "titulo":
            print(f"\n==== Código: {codigo} ====")
            print(f"--> {tituloTab.upper()}: {nuevaModificacion.title()}")
            print(f"{autorTab.upper()}: {autorLibro.title()}")
            print(f"{precioTab.upper()}: ${precioLibro:,.0f} COP")
            isInfoCorrecta = validarOpcionUsuario("\n>> ¿Desea guardar los cambios? (1 SI / 0 NO / 2 SALIR): ", 0, 2)
        
        elif infoModText.lower() == "autor":
            print(f"\n==== Código: {codigo} ====")
            print(f"{tituloTab.upper()}: {tituloLibro.title()}")
            print(f"--> {autorTab.upper()}: {nuevaModificacion.title()}")
            print(f"{precioTab.upper()}: ${precioLibro:,.0f} COP")
            isInfoCorrecta = validarOpcionUsuario("\n>> ¿Desea guardar los cambios? (1 SI / 0 NO / 2 SALIR): ", 0, 2)
        
        elif infoModText.lower() == "precio":
            print(f"\n==== Código: {codigo} ====")
            print(f"{tituloTab.upper()}: {tituloLibro.title()}")
            print(f"{autorTab.upper()}: {autorLibro.title()}")
            print(f"--> {precioTab.upper()}: ${nuevaModificacion:,.0f} COP")
            isInfoCorrecta = validarOpcionUsuario("\n>> ¿Desea guardar los cambios? (1 SI / 0 NO / 2 SALIR): ", 0, 2)
        
        
        #Validando si el usuario está seguro de la información ingresada
        if isInfoCorrecta == 1:
            #Actualizar información en el diccionario de libros y verificando su escritura en disco
            dictLibros[codigo][f"{infoModText.lower()}"] = nuevaModificacion
            
            if validarEscribirInfoArchivo(rutaFile, dictLibros):
                input("¡La información se ha actualizado con éxito!")
                return True
            else:
                print("Ha ocurrido un error al actualizar la información.")
                return False
            
        elif isInfoCorrecta == 0:
            input("Antes de confirmar la información verifique que los datos sean correctos.")
            continue
        
        elif isInfoCorrecta == 2:
            return False


def mostrarListaLibros(dictLibros, paginacion, tipoOrden):
    lstValoresLibrosOrdenados =  organizarInfoLibros(dictLibros, f"{tipoOrden}")
    # lstKeysDictLibros = list(dictLibros.keys())
    limitePaginacion = paginacion
    inicioBucle = 0
    checked = False
    print("\n==== ORDENAR POR TÍTULO ====\n")
    
    if len(dictLibros) <= 3:
        print("{:<8} {:<12} {:<30} {:<30} {:<14}".format("N°", "CÓDIGO", "TÍTULO DEL LIBRO", "AUTOR DEL LIBRO", "PRECIO"))
        
        for i in range(paginacion):
            try:
                # codigoLibro = lstKeysDictLibros[i]
                codigo, titulo, autor, precio = lstValoresLibrosOrdenados[i]
                print("{:<8} {:<12} {:<30} {:<30} {:<14}".format(i+1, codigo, titulo, autor, f"${precio:,.0f} COP"))
            
            except IndexError:
                break
    
    else:
        print("{:<8} {:<12} {:<30} {:<30} {:<14}".format("N°", "CÓDIGO", "TÍTULO DEL LIBRO", "AUTOR DEL LIBRO", "PRECIO"))
        
        while True:
            for i in range(inicioBucle, limitePaginacion):
                try:
                    # codigoLibro = lstKeysDictLibros[i]
                    codigo, titulo, autor, precio = lstValoresLibrosOrdenados[i]
                    print("{:<8} {:<12} {:<30} {:<30} {:<14}".format(i+1, codigo, titulo, autor, f"${precio:,.0f} COP"))
                    
                    if i+1 == limitePaginacion:
                        break
                
                except IndexError:
                    checked = True
                    break
            
            if checked:
                break
            else:
                continuarListaLibros = validarOpcionUsuario("\n>> ¿Deseas listar más libros? (1 SI / 0 NO): ", 0, 1)
                print("")
                
                if continuarListaLibros == 0:
                    break
                elif continuarListaLibros == 1:
                    #Estas variables establecen el rango de inicio y fin en el bucle for
                    inicioBucle = limitePaginacion
                    limitePaginacion += paginacion
                    continue


def ordenarInfoArchivo(dictLibros):
    lstConvDict = []
    lstValueDictLibrosOrdenado = organizarInfoLibros(dictLibros, "codigo")
    
    for i in range(len(lstValueDictLibrosOrdenado)):
        codTupla, titTupla, autorTupla, precioTupla = lstValueDictLibrosOrdenado[i]
        lstConvDict.append((codTupla, {'titulo': titTupla, 'autor': autorTupla, 'precio': precioTupla}))
    
    dictLibros = {}
    dictLibros = dict(lstConvDict)
    return dictLibros


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


def validarAbrirInfoArchivo(rutaFile, dictLibros):
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
            dictLibros.update(json.load(abrirArchivo))
        
        else:
            dictLibros = {}
    
    except Exception as e:
        print("Ha ocurrido un problema al intentar recuperar la información del sistema.")
        print(f"Error: {e}.\n")
        return False
    
    return dictLibros


def validarEscribirInfoArchivo(rutaFile, dictLibros):
    #Validación n°1 - Abrir el archivo en modo escritura
    try:
        guardarInfo = open(rutaFile, "w")
    
    except Exception as e:
        print("Ha ocurrido un problema al ejecutarse la función de guardado.")
        print(f"Error: {e}.\n")
        return False

    
    #Validación n°2 - Escribir la información en el archivo correspondiente
    try:
        json.dump(dictLibros, guardarInfo)
    
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


def validarPrecio(msj, min):
    while True:
        try:
            precio = int(input(msj))
            
            if precio < min:
                print(f"Error: El precio no puede ser menor a ${min:,.0f} COP.\n")
                continue
            return precio
        
        except ValueError:
            print("Ha ocurrido un error al ingresar el precio. Inténtelo de nuevo.\n")
        except:
            print("Ha ocurrido un error inesperado. Inténtelo de nuevo o comuníquese con un administrador.\n")


# DEFINIENDO LAS FUNCIONES PRINCIPALES
def menu(msj):
    print("\n\n", "LIBRERÍA ACME".center(20))
    print("MENU".center(21))
    
    print("1. Insertar Libro")
    print("2. Consultar Libro")
    print("3. Editar Libro")
    print("4. Borrar Libro")
    print("5. Listar Libro")
    print("6. Salir")
    return validarOpcionUsuario(msj, 1, 6)


def inicializarPrograma(rutaFile, dictLibros):
    dictLibrosArchivo = validarAbrirInfoArchivo(rutaFile, dictLibros)
    dictLibrosOrganizado = ordenarInfoArchivo(dictLibrosArchivo)
    validarEscribirInfoArchivo(rutaFile, dictLibrosOrganizado)
    return dictLibrosOrganizado
    
    # return validarAbrirInfoArchivo


def insertarLibro(cod, tit, autor, precio, dictLibros):
    print("\n*** INSERTAR LIBRO ***")
    print("Ingrese a continuación la siguiente información sobre el libro:\n")
    
    #Verificar que el código sea válido y no esté registrado
    while True:
        codigo = validarCodigo(cod, 1, 1)
        validarExisteLibro = dictLibros.get(codigo)
        
        if validarExisteLibro == None:
            titulo = validarTexto(tit, 1)
            autorLibro = validarTexto(autor, 1)
            precioLibro = validarPrecio(precio, 1000)
            return [codigo, titulo, autorLibro, precioLibro]
        
        else:
            print("Error: El código ingresado ya pertenece a un libro registrado.")
            reintentar = validarOpcionUsuario(">> ¿Deseas volver a intentarlo? (1 SI / 0 NO): ", 0, 1)
            print("")
            
            if reintentar == 1:
                continue
            elif reintentar == 0:
                return False


def consultarLibro(cod, dictLibros):
    print("\n*** CONSULTAR LIBRO ***\n")
    
    while True:
        verificarExisteLibro = existeLibro(cod, dictLibros)
        
        if verificarExisteLibro == False:
            print("Error: El código ingresado no corresponde a ningún libro registrado. Inténtelo de nuevo.\n")
            volverIntentar = validarOpcionUsuario(">> ¿Desea volver a buscar el libro? (1 SI / 0 NO): ", 0, 1)
            
            if volverIntentar == 1:
                input("Asegúrate de que el código está escrito correctamente...")
                continue
            elif volverIntentar == 0:
                input("Regresando al menú principal. Presione cualquier tecla para continuar...")
                break
        
        else:  
            tituloTab, autorTab, precioTab = list(verificarExisteLibro[1].keys())
            tituloLibro, autorLibro, precioLibro = list(verificarExisteLibro[1].values())
            
            print(f"\n==== Código: {verificarExisteLibro[0]} ====")
            print(f"{tituloTab.upper()}: {tituloLibro.title()}")
            print(f"{autorTab.upper()}: {autorLibro.title()}")
            print(f"{precioTab}: ${precioLibro:,.0f} COP")
        
        
        seguirConsultando = validarOpcionUsuario("\n>> ¿Deseas consultar otro libro? (1 SI / 0 NO): ", 0, 1)
        
        if seguirConsultando == 1:
            continue
        elif seguirConsultando == 0:
            input("Presione cualquier tecla para regresar al menú...")
            break


def editarLibro(cod, dictLibros, rutaFile):
    print("\n*** EDITAR LIBRO ***\n")
    
    while True:
        verificarExisteLibro = existeLibro(cod, dictLibros)
        
        if verificarExisteLibro == False:
            print("Error: El código ingresado no corresponde a ningún libro registrado. Inténtelo de nuevo.\n")
            volverIntentar = validarOpcionUsuario(">> ¿Desea volver a buscar el libro a editar? (1 SI / 0 NO): ", 0, 1)
            
            if volverIntentar == 1:
                continue
            
            elif volverIntentar == 0:
                input("Regresando al menú principal. Presione cualquier tecla para continuar...")
                return
        
        else:
            tituloTab, autorTab, precioTab = list(verificarExisteLibro[1].keys())
            tituloLibro, autorLibro, precioLibro = list(verificarExisteLibro[1].values())
            
            print("\n|| ¿Qué desea modificar? ||")
            print("1. Modificar Título")
            print("2. Modificar Autor")
            print("3. Modificar Precio")
            print("4. Regresar al menú principal")
            opcionUsuario = validarOpcionUsuario(">> Digite una opción: ", 1, 4)
            
            if opcionUsuario == 1:
                checkedModInfoLibro = modificarInfoLibro(verificarExisteLibro[0], list(verificarExisteLibro[1].keys()), list(verificarExisteLibro[1].values()), tituloLibro, tituloTab, 1, rutaFile, True)
                
            elif opcionUsuario == 2:
                checkedModInfoLibro = modificarInfoLibro(verificarExisteLibro[0], list(verificarExisteLibro[1].keys()), list(verificarExisteLibro[1].values()), autorLibro, autorTab, 1, rutaFile, True)
            
            elif opcionUsuario == 3:
                checkedModInfoLibro = modificarInfoLibro(verificarExisteLibro[0], list(verificarExisteLibro[1].keys()), list(verificarExisteLibro[1].values()), precioLibro, precioTab, 1000, rutaFile, False)
            
            elif opcionUsuario == 4:
                input("Saliendo...")
                break
            
            if not checkedModInfoLibro:
                input("Regresando al menú principal. Presione cualquier tecla para continuar...")
                return
            else:
                pass
            
            
        #Preguntarle al usuario si desea editar otro libro y actuar en consecuencia
        seguirConsultando = validarOpcionUsuario("\n>> ¿Deseas editar otro libro? (1 SI / 0 NO): ", 0, 1)
        
        if seguirConsultando == 1:
            continue
        elif seguirConsultando == 0:
            input("Presione cualquier tecla para regresar al menú...")
            break


def borrarLibro(cod, dictLibros, rutaFile):
    print("\n*** BORRAR LIBRO ***\n")
    
    while True:
        verificarExisteLibro = existeLibro(cod, dictLibros)
        if verificarExisteLibro == False:
            print("Error: El código ingresado no corresponde a ningún libro registrado. Inténtelo de nuevo.\n")
            volverIntentar = validarOpcionUsuario(">> ¿Desea volver a buscar el libro a editar? (1 SI / 0 NO): ", 0, 1)
            
            if volverIntentar == 1:
                continue
            
            elif volverIntentar == 0:
                input("Regresando al menú principal. Presione cualquier tecla para continuar...")
                return
        
        else:
            infoElementoEliminar = list(dictLibros[verificarExisteLibro[0]].values())
            confirmarEliminar = validarOpcionUsuario(f"¿Seguro que desea eliminar el libro '{infoElementoEliminar[0]}' cuyo código es '{verificarExisteLibro[0]}'? (1 SI / 0 NO / 2 SALIR): ", 0, 2)

            if confirmarEliminar == 1:
                titulo = dictLibros[verificarExisteLibro[0]]["titulo"]
                codigo = verificarExisteLibro[0]
                del dictLibros[verificarExisteLibro[0]]
                
                if not existeLibro(codigo, dictLibros, True) and validarEscribirInfoArchivo(rutaFile, dictLibros):
                    print(f"¡El libro '{titulo} con código '{codigo}' ha sido eliminado con éxito!")
                    input("Presione cualquier tecla para continuar...")
                    break
                else:
                    print("Ha ocurrido un error al eliminar la información del libro.")
                    input("Regresando al menú principal. Presione cualquier tecla para continuar...")
                    return
            
            elif confirmarEliminar == 0:
                print("")
                continue
            
            elif confirmarEliminar == 2:
                input("Regresando al menú principal. Presione cualquier tecla para continuar...")
                return


def listarLibros(msj, dictLibros, paginacion):
    print("\n*** LISTAR LIBROS ***\n")
    
    print("|| ¿En qué orden le gustaría ordenar la lista de libros? ||")
    print("1. Listar por título")
    print("2. Listar por autor")
    print("3. Listar por precio")
    print("4. Regresar al menú")
    opcionUsuario = validarOpcionUsuario(msj, 1, 4)
    
    
    if opcionUsuario == 1:
        mostrarListaLibros(dictLibros, paginacion, "titulo")
    
    elif opcionUsuario == 2:
        mostrarListaLibros(dictLibros, paginacion, "autor")
    
    elif opcionUsuario == 3:
        mostrarListaLibros(dictLibros, paginacion, "precio")
    
    elif opcionUsuario == 4:
        return False
    
    input("\nPresione cualquier tecla para continuar...")


# CREANDO LA ESTRUCTURA DEL PROGRAMA
while isVerdadero:
    while inicializandoSistema:
        rutaFile = "1. Python/Recursos Profe/2. Libreria ACME/data.json"
        dictLibros = inicializarPrograma(rutaFile, {})
        break
    
    inicializandoSistema = False
    opcionUsuario = menu("   >> Elije una opción: ")
    
    if opcionUsuario == 1:
        while True:
            infoLibroAgregar = insertarLibro(">> Código: ", ">> Título: ", ">> Autor: ", ">> Precio: ", dictLibros)
            
            #Verifica si el código del libro existe o no mediante la respuesta de la función "insertarLibro()" por parte de la función "existeLibro()"
            if infoLibroAgregar == False:
                break
            else:
                codigo, titulo, autor, precio = infoLibroAgregar
            
            
            #Agregar la información del libro a un diccionario vacío
            dictLibrosMemoria = {}
            dictLibrosMemoria[codigo.upper()] = {
                "titulo": titulo.title(),
                "autor": autor.title(),
                "precio": precio
            }
            dictLibros.update(dictLibrosMemoria)
            
            #Cargar información al archivo JSON
            if validarEscribirInfoArchivo(rutaFile, dictLibros):
                print(f"\n¡El libro '{titulo.title()}' con el código '{codigo.upper()}' ha sido guardado con éxito!")
            else:
                break
            
            
            #Verificar si el usuario desea continuar agregando libros
            dictLibrosOrganizar = ordenarInfoArchivo(dictLibros)
            validarEscribirInfoArchivo(rutaFile, dictLibrosOrganizar)
            
            continuar = validarOpcionUsuario(">> ¿Desea agregar otro libro? (1 SI / 0 NO): ", 0, 1)
            if continuar == 1:
                continue
            elif continuar == 0:
                input("Presione cualquier tecla para regresar al menú...")
                break
        

    elif opcionUsuario == 2:
        consultarLibro(">> Ingrese el código del libro a consultar: ", dictLibros)
    
    elif opcionUsuario == 3:
        editarLibro(">> Ingrese el código del libro a editar: ", dictLibros, rutaFile)
    
    elif opcionUsuario == 4:
        borrarLibro(">> Ingrese el código del libro a borrar: ", dictLibros, rutaFile)
    
    elif opcionUsuario == 5:
        checked = listarLibros(">> Seleccione una opción: ", dictLibros, 3)
        
        if not checked:
            input("\nRegresando al menú principal. Presione cualquier tecla para continuar...")
    
    elif opcionUsuario == 6:
        isVerdadero = False
        print("Saliendo...")