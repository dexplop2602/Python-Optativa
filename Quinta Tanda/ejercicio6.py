"""Ejercicio 6
Escribir un programa que almacene las asignaturas de un curso (por ejemplo
Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la
nota que ha sacado en cada asignatura y elimine de la lista las asignaturas
aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el
usuario tiene que repetir."""

curso = ["Matematicas","Fisica","Quimica","Historia","Lengua"]

nota1 = int(input("Que nota has sacado en Matematicas: "))
nota2 = int(input("Que nota has sacado en Fisica: "))
nota3 = int(input("Que nota has sacado en Quimica: "))
nota4 = int(input("Que nota has sacado en Historia: "))
nota5 = int(input("Que nota has sacado en Lengua: "))


if nota1 < 5:
    curso.remove("Matematicas")
if nota2 < 5:
    curso.remove("Fisica")
if nota3 < 5:
    curso.remove("Quimica")
if nota4 < 5:
    curso.remove("Historia")
if nota5 < 5:
    curso.remove("Lengua")

print(f"El usuario tiene que repetir: {curso}")

