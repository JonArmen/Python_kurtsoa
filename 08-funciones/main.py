"""
FUNCIONES:
Una función es un conjunto de instrucciones agrupadas bajo
un nombre concreto que pueden reutilizarse invocando a
la función tantas veces como sea necesario.

def nombreDeMiFuncion(parametros):
        # BLOQUE / CONJUNTO DE INSTRUCCIONES

nombreDeMiFuncion(mi_parametro)
nombreDeMiFuncion(mi_parametro)

"""

# Ejemplo 1
print("##### EJEMPLO 1 ############")

def muestraNombre():
    print("Jon")
    print("Juan")
    print("Iñaki")
    print("Mikel")
    print("Julen")
    print("\n")

# Invocar función 
muestraNombre()
muestraNombre()
muestraNombre()

# Ejempñlo 2: parámetros
print("########### EJEMPLO 2 #############")

#nombre = "Jon armendariz"
def mostrarTuNombre(nombre, edad):
    print(f"Tu nombre es: {nombre}")
    if edad >= 18:
        print("Y eres mayor de edad")

"""
nombre = input("Introduce tu nombre: ")
edad = int(input("Introduce tu edad: "))
mostrarTuNombre(nombre, edad)
"""

# Ejemplo 3
print("########### EJEMPLO 3 #############")

def tabla(numero):
    print(f"Tabla de multiplicar del número {numero}")
    for contador in range(11):
        operacion = numero*contador
        print(f"{numero} * {contador} = {operacion}")
        print("\n")

tabla(3)
tabla(7)
tabla(12)

# Ejemplo 3.1
print("----------------------------------------------")

for numero_tabla in range(1, 11):
    tabla(numero_tabla)


# Ejemplo 4
print("########### EJEMPLO 3 #############")

# Parámetros opcionales

def getEmpleado(nombre, dni = None):
    print("EMPLEADO")
    print(f"Nombre: {nombre}")
    if dni != None:
        print(f"DNI: {dni}")

getEmpleado("Jon Armendariz", "74859585K")
getEmpleado("Mikel Armendariz")


# Ejemplo 5. parámetros opciones y return o devolver datos

print("########### EJEMPLO 5 #############")
 


# Ejemplo 6.
print("\n########### EJEMPLO 6 #############")

def calculadora(numero1, numero2, basicas = False):

    suma = numero1 + numero2
    resta = numero1 - numero2
    multi = numero1 * numero2
    division = numero1 / numero2

    cadena = ""

    if basicas != False:
        cadena += "Suma: " + str(suma)
        cadena += "\n"
        cadena += "Resta: " + str(resta)
        cadena += "\n"
    else:
        cadena += "Multiplicación: " + str(multi)
        cadena += "\n"
        cadena += "División:" + str(division)

    return cadena

print(calculadora(5,5, True))
print(calculadora(5,5))

# Ejemplo 7
print("\n########### EJEMPLO 7 #############")
def getNombre(nombre):
    texto = f"El nombre es: {nombre}"
    return texto
def getApellidos(apellidos):
    texto = f"Los apellidos son: {apellidos}"
    return texto
def devuelveTodo(nombre, apellidos):
    texto = getNombre(nombre) + "\n" + getApellidos(apellidos)
    return texto

print(devuelveTodo("Jon","Armendariz Gabirondo"))

# Ejemplo 8. Funciones Lambda: Tareas cortitas y concretas
print("\n########### EJEMPLO 8 #############")

dime_el_year = lambda year: f"El año es {year * 50}"
print(dime_el_year(2034))
