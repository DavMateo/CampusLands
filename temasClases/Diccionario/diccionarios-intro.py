empleado = {}
empleado = {
    "Nombre": "Sergio Medina",
    "Cargo": "Programador",
    "Salario": 4000000
}

print(empleado["Cargo"])
print(empleado.get("Cargo"))
# print(empleado["apellido"])
print(empleado.get("apellido", "llave no existe"))

# Agregar una llave
empleado ["sexo"] = "M"
print(empleado)

# Modificar un valor
empleado["Salario"] = 4500000

# Borrar una llave y su valor
del empleado["sexo"]
print(empleado)

# Borrar todo el diccionario
# empleado = {}
# empleado.clear()
# del empleado    # Borra el diccionario y también la lista como tal.


print("\n\n\n", "MÉTODOS", "\n")


#Copy
oficina = empleado.copy()
print(oficina)
oficina["salario"] = 5000000
print(oficina)
print(empleado)


#Fromkeys
x = ("key1", "key2", "key3")
y = 0
thisDict = dict.fromkeys(x, y)
print(thisDict)


#Items
print(empleado.items()) #Usado mucho al iterar un diccionario.


#Keys
print(empleado.keys())


#Values
print(empleado.values())


#pop
print(empleado.pop("Salario"))
print(empleado)


#popitem
print(empleado.popitem())
print(empleado)


#setdefault
print(empleado.setdefault("Nombre", "Mateo"))
print(empleado.setdefault("Ciudad", "Bucaramanga"))
print(empleado)