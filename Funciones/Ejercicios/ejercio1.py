# PRIMERO CREAR LA ESTRUCTURA DEL PROGRAMA, TODA LA PARTE LÓGICA, LUEGO CREAR Y DEFINIR LAS FUNCIONES


# DEFINIENDO LAS FUNCIONES
def leerInt(mensaje):
    while True:
        try:
            numero = int(input(mensaje))

            if numero < 1:
                print("Valor inválido. Debe ser mayor a cero.")
            return numero
        
        except ValueError:
            print("Error al ingresar el número.")

def leerNombre(nombreUsuario):
    while True:
        try:
            nombre = input(nombreUsuario)
            nombre = nombre.strip()

            if len(nombre) == 0 or not nombre.isalnum():
                print("Nombre inválido")
            return nombre
        
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def leerEstrato(estratoUsuario):
    while True:
        try:
            estrato = int(input(estratoUsuario))

            if estrato < 1 or estrato > 5:
                print("Estrato inválido. Ingrese del 1 al 5")
            return estrato
        
        except ValueError:
            print("Error al ingresar el estrato.")


def calcularTarifaBasica(estrato):
    if estrato == 1:
        return 10000
    elif estrato == 2:
        return 15000
    elif estrato == 3:
        return 20000
    elif estrato == 4:
        return 25000
    elif estrato == 5:
        return 30000
    

def calcularValorImpulso(impulso):
    return 100 * impulso


# ESTRUCTURA DEL PROGRAMA
cantidadUsuarios = leerInt("Ingrese la cantidad de usuarios: ")
valorTotal = 0

for i in range(1, cantidadUsuarios + 1):
    print("\nDatos del usuario #", i)
    nombre = leerNombre("Nombre: ")
    estrato = leerEstrato("Estrato: ")
    impulsosTelefonicos = leerInt("Impulsos telefónicos: ")
    valorTarifaBasica = calcularTarifaBasica(estrato)
    valorImpulso = calcularValorImpulso(impulsosTelefonicos)

    print("=" * 35)
    print("Nombre:", nombre)
    print("Valor a pagar:", valorTarifaBasica + valorImpulso)
    print("Tarifa básica:", valorTarifaBasica)
    print("Valor de los impulsos telefónicos:", valorImpulso)

    valorTotal += valorTarifaBasica + valorImpulso

print("\n", "*" * 30)
print("El valor total a pagar es:", valorTotal)