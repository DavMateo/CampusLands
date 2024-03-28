# EJERCICIO 1
# Hacer un programa en Python que genere el siguiente número de la secuencia:
    #1,1,2,-1,1,-2,


num1 = 1
num2 = 1
signo = -1
print(num1, num2, end=", ")

for i in range(100):
    suma = num1 + (signo**i) * num2
    num1 = num2
    num2 = suma
    print(suma, end=", ")