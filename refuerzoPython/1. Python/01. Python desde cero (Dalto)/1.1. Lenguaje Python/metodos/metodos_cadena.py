cadena1 = "Hola,Maquina,Como,Estas"
cadena2 = "Bienvenido maquinola"


#dir() --> Devuelve la lista de atributos válidos del objeto pasado.
listaMetodosDisponibles = dir(cadena1)


#upper() --> Convierte a mayúscula.
mayuscula = cadena1.upper()

#lower() --> Convierte a minúscula.
minuscula = cadena1.lower()

#capitalize() --> Primera letra en mayúscula
primer_letra_mayuscula = cadena1.capitalize()



#find() --> Buscamos una cadena en otra cadena, si no hay conincidencias devuelve "-1"
busqueda_find = cadena1.find("d")

#index() --> Buscamos una cadena en otra cadena, si no hay coincidencias lanza una "Excepción"
busqueda_index = cadena1.index("H")



#isnumeric() --> Si es numérico devuelve "True", de lo contrario devuelve "False"
es_numerico = cadena1.isnumeric()

#isalnum() --> Si es alfabético devuelve "True", de lo contrario devuelve "False"
es_alfabetico = cadena1.isalpha()


#count() --> Contamos las coincidencias de una cadena dentro de otra cadena, devuelve la cantidad de coincidencias
contar_coincidencias = cadena1.count("Hola")

#len() --> Contamos cuantos caracteres tiene una cadena
contar_caracteres = len(cadena1)


#startswith() --> Verificamos si una cadena empieza con otra cadena dada, si es así devuelve "True"
empieza_con = cadena1.startswith("Hola")

#endswith() --> Verificamos si una cadena termina con otra cadena dada, si es así devuelve "True"
termina_con = cadena1.endswith("H")


#replace() --> Reemplaza un pedazo de la cadena dada, por otra dada
cadena_nueva = cadena1.replace(",", " ")

#split() --> Separar cadenas con la cadena que le pasemos
cadena_separada = cadena1.split(",")


print(cadena_separada[0])