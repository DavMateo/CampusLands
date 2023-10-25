listaInfoEmpleados = []
lstEncabezado = []


infoEmpleados = open("Filtro Python/infoClima.csv", "r")
encabezado = infoEmpleados.readline()
#infoEmpleados.seek(0)
convertirToLista = list(infoEmpleados)


for i in range(len(convertirToLista)):
    listaInfoEmpleados.append(convertirToLista[i].split(";"))


lstEncabezado.append(encabezado.split(";"))
infoEmpleados.close()

print(lstEncabezado)
print("")
print(listaInfoEmpleados)