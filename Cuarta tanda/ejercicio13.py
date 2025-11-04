"""Ejercicio 13
Escribir un programa que muestre el eco de todo lo que el usuario introduzca hasta
que el usuario escriba “salir” que terminará."""


salir = "salir"

cont = 0
while cont < 1:
    usuario = input()
    print(f"{usuario}")
    if usuario == salir:
        cont += 1
    