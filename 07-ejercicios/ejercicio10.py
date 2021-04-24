"""
Ejercicio 10. El programa tiene que pedir la nota de 15 alumnos y sacar por pantalla cuantos han aprobado y cuantos han suspendido
"""
alumnos = 15
contador = 1
aprobados = 0
suspendidos = 0
while contador <= alumnos:
    nota = int(input("Introduce la nota del alumno: "))
    contador += 1
    if (nota >= 5):
        aprobados += 1
    else:
        suspendidos += 1
print(f"El número de aprobados es: {aprobados}")
print(f"El número de suspendidos es: {suspendidos}")