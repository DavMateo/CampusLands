# Python permite escribir archivos pero no solo para leerlo, también para editar
# o recuperar información para usarse posteriormente en el programa.


archivo = open("Persistencia de Datos/salas.txt", "w")

archivo.write("Sputnik\n\t")
archivo.write("Apolo\n")

archivo.writelines(["Houston\n", "Artemis\n"])

archivo.close()