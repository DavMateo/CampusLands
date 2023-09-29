# Definir la función
def longString(str):
    try:
        longitudCadena = 0
        
        while str[longitudCadena] != None:
            longitudCadena += 1
    except:
        pass    # Es distinto de Continue. Significa que siga de largo y no continue en el bucle
    
    return longitudCadena


def prepararCafe(insumo1, insumo2):
    salida = ""
    if insumo1.lower() == "cafe" and insumo2.lower() == "agua":
        salida = "tinto"
    else:
        salida = "Se dañó la cafetera :c"

    return salida


# Uso de la función
taza = prepararCafe("cafe", "agua")
print(taza)
print(longString(taza))
print(len(taza))