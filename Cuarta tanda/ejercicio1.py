"""Ejercicio 1
Escribir un programa que pida al usuario una palabra y la muestre por pantalla 10
veces."""

Palabra = input("Introduzca una palabra: ")

a = 0
while a < 10:
    print(f"{Palabra}")
    a += 1