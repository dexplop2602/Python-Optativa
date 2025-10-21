"""Ejercicio 3
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla todos los números impares desde 1 hasta ese número separados por
comas."""

numero = int(input("Escriba un numero entero positivo: "))

a = 0
while a <= numero:
    if a % 2 != 0:
        print (f"{a}, ")
    a += 1