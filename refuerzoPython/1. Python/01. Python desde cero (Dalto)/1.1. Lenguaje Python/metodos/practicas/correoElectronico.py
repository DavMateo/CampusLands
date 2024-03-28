# Programa para practicar el tema de cadenas de texto.

correo = input("Ingrese su correo electrónico (Ej: correo@ejemplo.com): ").strip()
reemplazar = correo.split("@")[1]
print(correo.replace(reemplazar, "ceu.es"))