nada = None
cadena = "Hola soy Jon Armendariz WEB"
cadena = "Desarrollador web"
entero = 99
flotante = 5.3
booleano = True
lista = [10, 20, 30, 100, 200]
listaString = [44, "treinta", 30, "cuarenta"]
tuplaNoCambia = ("master", "en", "python")
diccionario = {
    "nombre": "Jon",
    "apellido": "Armenddariz",
    "curso": "Master en Python"
}
rango = range(9)
dato_byte = b"Probando"


# imprimir variables
print(cadena)
print(entero)
print(flotante)
print(booleano)
print(lista)
print(diccionario)
print(rango)
print(dato_byte)

# Mostrar el tipo de dato
print(type(nada))
print(type(cadena))
print(type(entero))
print(type(flotante))
print(type(booleano))
print(type(lista))
print(type(tuplaNoCambia))
print(type(diccionario))
print(type(rango))
print(type(dato_byte))


texto = "Hola soy un texto"
numerito = str(776)
print(texto + " "+ numerito)

numerito = int(numerito)
numerito = float(numerito)
print(numerito)
print(type(numerito))