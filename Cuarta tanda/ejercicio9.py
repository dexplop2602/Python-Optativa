"""Ejercicio 9
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña
correcta."""

contraseña = input("Escriba su contraseña: ")

correcta = "hola"

while contraseña != correcta:
    print(f"Introduzca una contraseña correcta")
    contraseña = input("Escriba su contraseña: ")