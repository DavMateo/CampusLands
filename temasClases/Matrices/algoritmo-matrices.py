def crearMatrices(fil, col):
    m = []
    
    for i in range(fil):
        fila = [0] * col
        m.append(fila)
        
    return m

def mostrarMatriz(matriz):
    for f in range(len(matriz)):
        for c in range(len(matriz[f])):
            print(matriz[f][c], end=" ")
        print("")

def llenarMatriz(matriz):
    for f in range(len(matriz)):
        print(f"\nFila n°{f+1}")
        
        for c in range(len(matriz[f])):
            matriz[f][c] = int(input(f"matriz[{f+1}][{c+1}]?: "))


matriz = crearMatrices(4, 5)
llenarMatriz(matriz)
mostrarMatriz(matriz)