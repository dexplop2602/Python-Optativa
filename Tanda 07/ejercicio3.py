"""Escribir una función que reciba un número entero positivo y devuelva su factorial."""


def factorial(numero):
    total = 1
    while numero > 1:
        total*= numero
        numero= numero - 1
    return print(f"{total}")

factorial(4)
