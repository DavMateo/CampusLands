# Diseñe un algoritmo que calcule e imprima el perímetro de un triángulo
# dadas las coordenadas de cada uno de sus vértices.

import math as Math

x1 = 1
y1 = 4
x2 = 3
y2 = 0
x3 = 5
y3 = 3

def distancia(xt, yt, xs, ys):
    d = Math.sqrt((xt - xs) ** 2 + (yt - ys) ** 2)
    return d


def perimetroTriangulo(xp, yp, xq, yq, xr, yr):
    perimetro = 0
    
    perimetro += distancia(xp, yp, xq, yq)
    perimetro += distancia(xq, yq, xr, yr)
    perimetro += distancia(xr, yr, xp, yp)
    
    return perimetro

perimetroResultado = perimetroTriangulo(x1, y1, x2, y2, x3, y3)
print(f"El perímetro del triángulo es: {perimetroResultado:.3f}")