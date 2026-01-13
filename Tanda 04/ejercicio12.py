"""Ejercicio 12
Escribir un programa en el que se pregunte al usuario por una frase y una letra, y
muestre por pantalla el número de veces que aparece la letra en la frase."""

frase = str(input("Introduzca una frase: "))

letra = str(input("Introduzca una letra: "))

tamano = len(frase) - 1

cont = 0
cont2 = 0
while cont <= tamano:
    letra2 = frase[cont]
    if letra2 == letra:
        cont2 += 1
    cont += 1

print(f"La letra aparece {cont2} veces")