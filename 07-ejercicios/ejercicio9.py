"""
Ejercicio 9. Hacer un programa que pida números al usuario
indefinidamente hasta meter el número 111.
"""
numero = 0
while(numero!=111):
    numero = int(input("Introduce un número: "))
    print(numero)
    print("Para salir introduce el número 111")