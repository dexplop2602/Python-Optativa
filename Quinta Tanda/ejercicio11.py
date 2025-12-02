"""Ejercicio 11
Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas y
muestre por pantalla su producto escalar."""

vector = [1,2,3]
vector2 = [-1,0,2]

operacion = (vector[0] * vector2[0]) + (vector[1] * vector2[1]) + (vector[2] * vector2[2])

print(f"{operacion}")