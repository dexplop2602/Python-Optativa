"""Ejercicio 11
Escribir un programa que pida al usuario una palabra y luego muestre por pantalla
una a una las letras de la palabra introducida empezando por la última."""

palabra = str(input("Escriba una palabra: "))
tamano = len(palabra) - 1

cont = tamano
while cont >= 0:
    print(f"{palabra[cont]}")
    cont -= 1