# Reduce una cadena de texto de caracteres minúsculas en rango "ascii['a'..'z']"
# haciendo una serie de operaciones. En cada operación, selecciona un par letras adyacentes
# que coincidan, y elimínalos.
# 
# Eliminar tantos caracteres como sea posible usando este método y retornando el 
# resultado de la cadena de texto. Si la cadena de texto final está vacía, retorna "Empty String".


string = input("Ingrese una cadena de texto a continuación: ").lower()
isVerdadero = True
count = 0
letraRepetida = 0


while isVerdadero:
    numeroAsciiLetra = ord(string[count])

    # Evaluar si la longitud del string es mayor a 0.
    if len(string) > 0:
        isVerdadero = True

        # Ciclo for para evaluar si hay alguna letra repetida dos veces.
        for i in range(ord("a"), ord("z")):
            if numeroAsciiLetra == i:
                letraRepetida += 1

                if letraRepetida == 2:
                    stringArray = string.split(chr(i))
                    nuevoString = "".join(stringArray)

                    string = nuevoString
                    print(string)

                    count += 1
    else:
        isVerdadero = False