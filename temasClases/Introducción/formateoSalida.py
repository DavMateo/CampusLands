# Ejemplos de formatear la salida


# CON LA FUNCIÓN FORMAT
sueldo = 5600000
print("Sueldo: ${:,}".format(sueldo))

intereses = 2568.568945808252085045
print("Intereses: ${:,.3f}".format(intereses))



# f-string
print(f"Sueldo: ${sueldo: ,}")
print(f"Intereses: ${intereses:,.3f}")