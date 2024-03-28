# Programa que simula el envío de mensajes a los correos del "From".


# DEFINIENDO LAS VARIABLES PRINCIPALES
email = set()


# CREANDO LA ESTRUCTURA DEL PROGRAMA
fd = open("Persistencia de Datos\\Ejercicios\\mbox-short.txt", "r")

for linea in fd:
    if linea.startswith("To:"):
        email.add(linea.split()[1])
fd.close()

for email in sorted(email, reverse=True):
    print(f"\nMensaje enviado: {email}  [ok]")