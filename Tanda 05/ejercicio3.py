"""Ejercicio 3
Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura, y después las muestre por pantalla con el
mensaje En <asignatura> has sacado <nota> donde <asignatura> es
cada una des las asignaturas de la lista y <nota> cada una de las correspondientes
notas introducidas por el usuario."""

asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]

nota0 = input("Que nota has sacado en Matematicas:")
nota1 = input("Que nota has sacado en Fisica:")
nota2 = input("Que nota has sacado en Quimica:")
nota3 = input("Que nota has sacado en Historia:")
nota4 = input("Que nota has sacado en Lengua:")

notas = [nota0, nota1, nota2, nota3, nota4]

tamaño = len(asignaturas)
cont = 0
while cont < tamaño:
    print(f"En {asignaturas[cont]} has sacado {notas[cont]}")
    cont += 1