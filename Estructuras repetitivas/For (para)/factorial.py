# Calcular el factorial de un número
# factorial de 5 = 1 * 2 * 3 * 4 * 5 = 120

factorial = int(input("¿Cuál es el factorial que deseas calcular?: "))
resultadoFactorial = 1

for i in range(1, factorial + 1):
    resultadoFactorial *= i

print(f"El factorial de {factorial} es {resultadoFactorial:,}")