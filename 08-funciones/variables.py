"""
Variables locales: Se definen dentro de la función y no
se puede usar fuera de ella, sólo están disponibles dentro.
A no ser que hagamos un return.

Variables globales: Son las que se declaran fuera de una función 
y están disponibles dentro y fuera de ellas.
"""

# Variables global
frase = "Ni los genios son tan genios, ni los mediocres tan mediocres"
print (frase)

def holaMundo():
    frase = "Hola mundo!!"
    print("Dentro de la función:")
    print(frase)

    year =2021
    print(year)

    global website
    website ="jonarmendarizweb.es"
    print("DENTRO: ", website)
    return "Dato devuelto " + str(year)
print(holaMundo())
print("FUERA: ", website)

