# Diseñe un algoritmo que permita determinar la distancia entre dos puntos "T" y "S" (Ver figura).

import math as Math

def distancia(xt, yt, xs, ys):
    d = Math.sqrt((xt - xs) ** 2 + (yt - ys) ** 2)
    return d

xt = 1
xs = 3
yt = 2
ys = 4

dist = distancia(xt, yt, xs, ys)
print(f"La distancia es: {dist:.3f}")