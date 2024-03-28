fd = open("Persistencia de Datos\\Ejercicios\\mbox-short.txt", "r")

contarLineas = 0
contarPalabras = 0

for linea in fd:
    linea = linea.strip()
    # contarPalabras += len(linea.split(" "))
    for lin in linea.split(" "):
        if lin.isalpha():
            contarPalabras += 1
    contarLineas += 1

fd.close()

print(f"Cantidad de líneas: {contarLineas}")
print(f"Cantidad de palabras: {contarPalabras}")