"""
Ejercicio 3. Escribir un programa que muestre los cuadrados
de los 60 primeros numeros naturales (del 1 al 60). Resolverlo
con for y con while
"""

# WHILE
contador = 1
while contador <= 60:
    print(f"WHILE:El cuadrado de {contador} es: {contador*contador}")
    contador+=1

#FOR
for contador2 in range(1,61):
    print(f"FOR:El cuadrado de {contador2} es: {contador2*contador2}")

