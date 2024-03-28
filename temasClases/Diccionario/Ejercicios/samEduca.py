n = int(input("Cantidad de docentes: "))

dicCategoria = {1:25000, 2:30000, 3:40000, 4:45000, 5:60000}

dicDocentes = {}
totalHonorarios = 0

for i in range(1, n+1):
    print("\nDatos del docente #", i)
    datosDocente = {}
    cedula = input("Cédula: ")
    datosDocente["nombre"] = input("Nombre: ")
    datosDocente["categoria"] = int(input("Categoría (1 al 5): "))
    datosDocente["horasLaboradas"] = int(input("Horas laboradas: "))
    datosDocente["honorarios"] = dicCategoria.get(datosDocente["categoria"], 0) * datosDocente["horasLaboradas"]
    
    totalHonorarios += datosDocente["honorarios"]
    dicDocentes[cedula] = datosDocente
    

print("\n\n", "=" * 30)
print("INFORME")
print("=" * 30)
print("NOMBRE\t\tHONORARIOS")
print("-" * 30)

for k, v in dicDocentes.items():
    print(f'{v["nombre"]}\t\t${v["honorarios"]:,}')
    
print("\n", "-" * 30)
print(f"Total honorarios: ${totalHonorarios:,}")