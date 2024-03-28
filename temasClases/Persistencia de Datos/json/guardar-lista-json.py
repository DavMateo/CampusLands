import json

fd = open("Persistencia de Datos/json/lista.json", "w")

lista = [
    {"nombre": "Paola", "edad": 25},
    {"nombre": "Carlos", "edad": 28},
    {"nombre": "Juan", "edad": 18},
    {"nombre": "Mateo", "edad": 19},
    {"nombre": "Patricia", "edad": 21}
]

json.dump(lista, fd)

fd.close()