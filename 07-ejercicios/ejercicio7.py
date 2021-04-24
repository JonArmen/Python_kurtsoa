"""
Ejercicio 7. Hacer un programa que muestre todos los números
impares entre dos número que decida el usuario
"""
numero1 = int(input("Introduce el primer número"))
numero2 = int(input("Introduce el segundo número"))
print(f"Los número impares entre el número {numero1} y el {numero2} son: ")
for contador in range(numero1, numero2+1):
    if contador%2 != 0:
        print(contador)