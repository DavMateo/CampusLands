import json

fd = open("Persistencia de Datos/json/lista.json", "r")

lista = []

lista = json.load(fd)

for e in lista:
    print(f"Nombre: {e['nombre']}")
    print(f"Edad: {e['edad']}")
    print(f"-" * 30)

fd.close()