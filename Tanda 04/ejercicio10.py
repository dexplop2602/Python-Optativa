"""Ejercicio 10
Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es un número primo o no."""

numero = int(input("Introduzca un numero entero: "))

cont = 1
primo = 0
while cont <= numero:
    if numero % cont == 0:
        primo += 1
    cont += 1

if primo > 2 or numero == 1:
    print("El numero no es primo")
else:
    print("El numero es primo")
