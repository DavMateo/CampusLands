s = "Yo soy tu padre"


# count()
print(s.count("o"))
print("")


# find() --> Arranca desde cero. Recorre de izquierda a derecha.
print(s.find("pa"))
print(s.find("ma"))


# rfind() --> Devuelve el índice en el que aparece la subcadena, empezando por el final (de derecha a izquierda).
print("")


# isdigit()
snum = "100"
print(snum.isdigit())

snum = "100a"
print(snum.isdigit())
print("")


#isalnum()
c = "ABC10034po"
print(c.isalnum())

c = "ABC10034po@"
print(c.isalnum())


# split()
nombre = "Juan Daniel  Ramirez Salazar"
email = "juandaniel@gmail.com"
miles = "1.234.231"
print(nombre.split())
print(nombre.split("Daniel"))
print(email.split("@"))
print(miles.split("."))

print("")


# strip()
a = "       Hola mundo        "
print(a.strip())
print("")


# replace()
b = "Hola mundo"
print("Antes de Replace:", b)
print("Después de Replace:", b.replace("o", "0"))