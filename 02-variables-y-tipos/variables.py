"""
Una variable es un contenedor de información
que dentro guardará un dato. Se pueden crear
muchas variables y que cada una tenga un dato distinto.
"""

#Crear variables y asignar un valor
texto = "Máster en Python"
texto2 = "con Jon Armendariz"
numero = 15
decimal = 6.7

#Mostrar valor de las variables
print(texto)
print(texto2)
print(numero)
print(decimal)


print("____________________________________________")

#Sustituir el valor de algunas variables
numero = 77
decimal = 8.9

print(numero)
print(decimal)

print("_______________________________________")

# Concatenación
nombre = "Jon"
apellidos ="Armendariz"
web = "jonarmendarizweb.es"

print(nombre + " " + apellidos + " - "+ web)
print(f"{nombre} {apellidos} - {web}")
print("Hola me llamo {} {} y mi web es: {}".format(nombre, apellidos, web))
print(nombre, apellidos, web)