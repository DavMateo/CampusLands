s = "Yo soy tu padre"

# print(s[7])
# print(s[-8])
# print("\n")

# Recorrer las cadenas
# Recorrido por índice
for i in range(len(s)):
    print(s[i], end=", ")

print("")
# Recorrido por elemento
for e in s:
    print(e, end=", ")


print("")
# Slice --> Porción.
print(s[2:])    # Desde el índice 2 hasta el final.
print(s[4:7])  # Desde el índice 4 hasta el índice 6.
print(s[::-1])  # Es como imprimir desde el 0 hasta el último índice - 1.
                # El doble punto es para invertir el orden en como se imprime la salida.