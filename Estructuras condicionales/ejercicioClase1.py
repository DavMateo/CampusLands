# Diseñe y escriba un programa que solicite tres números enteros
# (pueden ser positivos o negativos) y como salida los muestre en
# orden de mayor a menor.


# DEFINIR LAS VARIABLES
num1 = int(input("1/3: Ingrese un número a continuación: "))
num2 = int(input("2/3: Ingrese otro número a continuación: "))
num3 = int(input("3/3: Ingrese un último número a continuación: "))


# ORDENAR Y MOSTRAR EN PANTALLA
if num1 >= num2 and num1 >= num3 and num2 >= num3:
    print(num1)
    print(num2)
    print(num3)

elif num1 >= num2 and num1 >= num3 and num3 >= num2:
    print(num1)
    print(num3)
    print(num2)

elif num2 >= num1 and num2 >= num3 and num1 >= num3:
    print(num2)
    print(num1)
    print(num3)

elif num2 >= num1 and num2 >= num3 and num3 >= num1:
    print(num2)
    print(num3)
    print(num1)

elif num3 >= num1 and num3 >= num2 and num1 >= num2:
    print(num3)
    print(num1)
    print(num2)

elif num3 >= num1 and num3 >= num2 and num2 >= num1:
    print(num3)
    print(num2)
    print(num1)