"""Ejercicio 4
Escribir un programa que pida al usuario un número entero y muestre por pantalla si
es par o impar."""

numero = float(input("Escriba un numero entero: "))

resto = numero % 2

if resto == 0:
    print("El numero es par")
else:
    print("El numero es impar")