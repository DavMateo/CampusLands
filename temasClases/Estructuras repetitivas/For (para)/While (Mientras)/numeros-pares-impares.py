num = int(input("Ingrese un número: "))
numPares = 0
numImpares = 0

while num != -1:
    if num % 2 == 0:
        print("El número es par")
        numPares += 1
    else:
        print("El número es impar")
        numImpares +=1

    num = int(input("Ingrese un número: "))

print("\n", "=" * 30)
print("Cantidad de números pares es:", numPares)
print("Cantidad de números impares es:", numImpares)