"""Ejercicio 8
Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un
palíndromo."""

palabra = input("Escriba una palabra: ")

delreves = palabra[::-1]

if palabra == delreves:
    print(f"{palabra} es un palindromo")
else:
    print(f"{palabra} no es un palindromo")