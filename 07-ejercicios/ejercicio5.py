"""
Ejercicio 5. Hacer un programa que muestre todos los número entre
dos números que diga el usuario
"""

numero1 = int(input("Introduce el primer número: "))
numero2 = int(input("Introduce el segundo número: "))
numeros=""
print(f"Los número que hay entre el {numero1} y {numero2} son: ")
for contador in range(numero1, numero2+1):
    if contador != numero2:
        numeros = numeros + str(contador) + ","
        #print(f"{contador}, ")
    else:
        numeros = numeros + str(contador)
        #print(f"{contador}")
print(numeros)

    

