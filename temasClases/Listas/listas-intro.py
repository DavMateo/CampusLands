miLista = []    # Lista vacía
miLista2 = list()   # Lista vacía

nombreCampers = ["Juan", "Yulieth", "Lorenzo", "Manuel", "David"]
print(nombreCampers)
print(nombreCampers[1])
nombreCampers[1] = "Julieth"
print(nombreCampers[1])


# SLICES
print(nombreCampers[2:4])
print(nombreCampers[::-1])

nombreCampers_juan = ["Rut", "Daniela", "Maria", "Juliana", "Sandra", "Carolina"]
print(nombreCampers_juan)
# nombreCampers += nombreCampers_juan
# print(nombreCampers)

# MÉTODOS DE LISTAS
nombreCampers.append("Kevin")
print(nombreCampers)


nombreCampers.extend(nombreCampers_juan)
print(nombreCampers)
print(nombreCampers[-1])


nombreCampers.insert(1, "Carlos")
print(nombreCampers)


nombreCampers.pop()
print(nombreCampers)

nombreCampers.pop(-3)
print(nombreCampers)


nombreCampers.remove("Sandra")
print(nombreCampers)


nombreCampers.sort() # Ordena de izquierda a derecha en nombre alfabético
print(nombreCampers)

nombreCampers.insert(2, "Daniel")
nombreCampers.sort()
print(nombreCampers)



#ERROR:
# list2 = [0, 1, 15, "115"]
# list2.sort()
# print(list2)



nombreCampers.sort(reverse=True)
print(nombreCampers)

nombreCampers.reverse()
print(nombreCampers)