# Python permite leer archivos pero no solo para leerlo, también para editar
# o recuperar información para usarse posteriormente en el programa.


archivo = open("Persistencia de Datos/nombres.txt", "r")

texto = archivo.read()
print(texto)
print("\n")


archivo.seek(0) # Posición en donde el puntero se ubicará en el archivo.
texto2 = archivo.readline()
print(texto2)
print("\n")


texto3 = archivo.readlines()
print(texto3)
print("\n")

archivo.close()