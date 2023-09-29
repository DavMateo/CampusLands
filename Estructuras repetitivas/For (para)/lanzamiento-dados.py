# De lanzar un dado 100 veces, imprimir en pantalla cuántas veces cae
# la cara de 5.

import random


caeCinco = 0    # Variable de tipo contador.

for i in range(100):
    dado = random.randrange(1, 7)

    if dado == 5:
        caeCinco += 1

print(f"El lado 5 cayó {caeCinco} veces.")