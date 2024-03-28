palabra = input("Ingrese una palabra: ")
palabraReves = palabra[::-1]


if palabra.lower() == palabraReves.lower():
    print(f"La palabra {palabra} es palíndrome!")
else:
    print(f"La palabra {palabra} NO es palíndrome.")