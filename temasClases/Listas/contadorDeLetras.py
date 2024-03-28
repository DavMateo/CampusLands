letras = []

while True:
    letra = input("Ingrese una letra del abecedario: ")
    
    if not letra.isalpha():
        print(">> Error. Letra no válida.\n")
        continue
    
    letras.append(letra)
    
    op = input("\nDesea continuar (S/N)?")
    if op.lower() != "s":
        break


print("\n", "=" * 30)
vocales = ["a", "e", "i", "o", "u"]
cantidadVocales = [0] * 5   #Creando una lista de 5 posiciones fácil y rápido xd

# Recorrer la lista por elementos
for l in letras:
    if l.lower() in vocales:
        p = vocales.index(l.lower())
        cantidadVocales[p] += 1
    

# RECORRIDO POR POSICIÓN.
for p in range(len(vocales)):
    print(vocales[p], " = ", cantidadVocales[p])