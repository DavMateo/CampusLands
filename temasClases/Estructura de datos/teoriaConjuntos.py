# Creando un conjunto
conjunto = {1, 2, 3, "Hola Mundo"}
print(conjunto)


# Agregando un elemento al conjunto
conjunto.add("Nuevo elemento")
print(conjunto)

# conjunto.add(["MiLista", "34", 21])  -->  Las listas no se pueden añadir a los conjuntos.


# Operaciones conjuntos
A = {1, 3, 5, 7, 9, 12}
B = {5, 7, 9, 15, 20, 30}

# Unión
C = A | B
print(C)

# Común
C = A & B
print(C)

# Diferencia
C = A - B
print(C)