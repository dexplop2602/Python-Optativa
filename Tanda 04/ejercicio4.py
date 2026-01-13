"""Ejercicio 4
Escribir un programa que pida al usuario un número entero positivo y muestre por
pantalla la cuenta atrás desde ese número hasta cero separados por comas."""

numero = int(input("Escriba un numero entero positivo: "))


a = numero
while a >= 1:
    print(a)
    a -= 1