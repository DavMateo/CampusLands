# Programa para la empresa SweetCO para responder sus dudas sobre las ventas semanales.


# VARIABLES PRINCIPALES
matrizPrecios = [1500, 5000, 6500, 2500, 22500]
matrizVentas = [
    [100, 88, 92, 94, 85, 110, 118],
    [30, 42, 31, 32, 38, 40, 37],
    [23, 35, 39, 45, 55, 60, 61],
    [45, 50, 56, 65, 47, 57, 68],
    [18, 25, 33, 21, 22, 28, 32]
]
diaSemana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]


# FUNCIONES PRINCIPALES
def calcularProductoMaxIngresoSemana(matrizVentas, matrizPrecios):
    filas = len(matrizVentas)
    listaTotalVentas = [0] * filas

    for f in range(filas):
        listaTotalVentas[f] = sum(matrizVentas[f]) * matrizPrecios[f]
    
    maxVentas = max(listaTotalVentas)
    productoMaxVentas = listaTotalVentas.index(maxVentas) + 1
    
    return productoMaxVentas


def calcularDiaSemanaMaxIngresos(matrizVentas, matrizPrecios):
    columnas = len(matrizVentas[0])
    listaTotalIngresos = [0] * columnas
    count = 0
    countCol = 0
    
    
    while count < columnas:
        for f in range(len(matrizVentas)):
            for c in range(countCol, countCol+1):
                listaTotalIngresos[c] += matrizVentas[f][c]
                
        countCol += 1 
        count += 1
    
    maxIngresos = max(listaTotalIngresos)
    diaMaxIngresos = listaTotalIngresos.index(maxIngresos) + 1
    
    return diaMaxIngresos


# ESTRUCTURA DEL PROGRAMA
print("")
productoMaxIngresoSemana = calcularProductoMaxIngresoSemana(matrizVentas, matrizPrecios)
print(f"El producto que más genera ingresos en la semana es: {productoMaxIngresoSemana}")

diaMaxIngresoSemana = calcularDiaSemanaMaxIngresos(matrizVentas, matrizPrecios)

for i in range(diaMaxIngresoSemana):
    if i == diaMaxIngresoSemana - 1:
        print(f"El día que más se genera ingresos es el: {diaSemana[i]}")