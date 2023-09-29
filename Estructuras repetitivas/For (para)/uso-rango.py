# FUNCIÓN range([valorInicial], valorFinal, [incremento]) -> Lo que está entre corchetes es opcional.

print(list(range(5)))  # --> 0, 1, 2, 3, 4.
print(list(range(19)))  # --> 0, 1, 2, 3 ... 18.

print(list(range(2, 10))) # --> 2, 3, 4, 5, 6, 7, 8, 9.
print(list(range(-2, 10))) # --> -2, -1, 0, 1, 2 ... 9.
print(list(range(15, -3))) # --> Vacío. Esto se da porque el incremento por defecto es en +1.

print(list(range(2, 10, 3))) # --> 2, 5, 8. Se incrementa de 3 en 3.
print(list(range(15, -3, -1))) # --> 15, 14, 13, 12 ... -2. Inicia en 15, finaliza en -3 y decrementa en -1.

print(list(range(1, 5, 3))) # --> 1, 4.