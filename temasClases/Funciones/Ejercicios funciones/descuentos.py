# Algoritmo para determinar un descuento luego de que un artículo
# supere los $150000 pesos.

def descuento(valorArticulo):
    if valorArticulo > 150000:
        descuento = valorArticulo * 0.05
    else:
        descuento = 0
    
    return descuento

valorArticulo = descuento(int(input("¿Cuánto vale el artículo?: ")))
print(f"El descuento es de: ${valorArticulo:,.0f} pesos.")