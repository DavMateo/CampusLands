fd = open("Persistencia de Datos\nombres.txt", "r")
fd2 = open("Persistencia de Datos\Ejercicios\nombres-bak.txt", "w")

for linea in fd:
    fd2.write(linea)

fd2.close()
fd.close()

print("Proceso terminado")