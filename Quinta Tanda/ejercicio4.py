"""Ejercicio 4
Escribir un programa que pregunte al usuario los números ganadores de la lotería
primitiva, los almacene en una lista y los muestre por pantalla ordenados de menor
a mayor."""

primitiva = input("Escriba los numeros ganadores de la loteria separados por comas: ")

separar = primitiva.split(",")

tamaño = len(separar)

ordenar = sorted(separar)

cont = 0
while cont < tamaño:
    print (f"Esta es la lista de menor a mayor: ", (ordenar[cont]))
    cont+= 1