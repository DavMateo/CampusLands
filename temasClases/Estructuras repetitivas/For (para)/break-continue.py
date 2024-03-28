# BREAK

# Calcular si un número es primo.
# num primo: divisible por si mismo y por 1.


# num = int(input("Ingrese un número: "))

# if num < 2:
#     print("No es primo.")
# elif num == 2:
#     print("Es primo.")
# else:
#     esPrimo = True  # variables banderas o switch
    
#     for i in range(2, num):
#         if num % i == 0:
#             esPrimo = False
#             break
    
#     if esPrimo:
#         print("Es primo")
#     else:
#         print("No es primo. Lo divide", i)





# CONTINUE
# Saltar una iteración de un ciclo.

# Imprima los números del 1 al 100 excepto los múltiplos de 7.

for i in range(1, 101):
    if i % 7 == 0:
        continue
    else:
        print(i, end=", ")