"""
Ejercicio 6. Mostrar todas las tablas de multiplicar del 1 al 10.
Mostrando el título de la tabla y luego las multiplicaciones del 1 al 10.
"""
for contador1 in range(1, 11):
    print(f"Tabla de multiplicar del {contador1}")
    for contador2 in range(1,11):
        print(f"{contador1}*{contador2} = {contador1*contador2}")
