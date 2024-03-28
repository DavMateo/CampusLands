# for a in range(10):
#     print(a)

# for c in range(0, 10, 2):
#     print(c)

# for i in range(10, 0, -1):
#     print(i, end=", ")


# for i in range(6):
#     print("*", end="")

# print("")
# for i in range(3):
#     print("*    *")

# for i in range(6):
#     print("*", end="")
# print("")


# EJERCICIO 1: El usuario le dice el tamaño de la pirámide:

filas = int(input("¿De cuántas líneas deseas que tenga tu pirámide?: "))

for i in range(1, filas + 1):
    print("*" * i)