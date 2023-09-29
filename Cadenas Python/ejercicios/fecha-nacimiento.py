fecha = input("\nFecha: ")
fechaArray = fecha.split("/")
isValid = True

if len(fechaArray[0] == 2) and len(fechaArray[1] == 2) and len(fechaArray[2] == 4):
    isValid = True

    for i in fechaArray:
        if not i.isdigit():
            isValid = False
            break
    
    if isValid:
        print(f"Día: {fechaArray[0]}, mes: {fechaArray[1]}, año: {fechaArray[2]}")
    else:
        print("Formato no válido")
else:
    print("Formato no válido")