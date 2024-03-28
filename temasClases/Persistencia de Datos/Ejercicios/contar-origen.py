def miFuncion(email):
    return len(email)


fd = open("Persistencia de Datos\\Ejercicios\\mbox-short.txt", "r")

# contarLineas = 0
setEmail = set()

for linea in fd:
    if linea.startswith("From:"):
        # contarLineas += 1
        # email = linea.split()[1]
        # print(email)
        setEmail.add(linea.split()[1])
        

fd.close()
contarLineas = len(setEmail)
print("\nCantidad de correos de origen distintos:", contarLineas, "\n")

for email in sorted(setEmail, reverse=False, key=miFuncion):
    print(email)


# El método "sorted(param)" es el ".sort()" de los conjuntos. Sirve para ordenar
# los datos en orden alfabético. También se puede usar programación funcional (Lambda) o
# una función propia para ordenar no en orden alfabético sino en un valor determinado.
# (Por ejemplo, números)