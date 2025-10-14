"""Ejercicio 3
Escribir un programa que pida al usuario dos números y muestre por pantalla su
división. Si el divisor es cero el programa debe mostrar un error."""

numero1 = float(input("Introduzca un numero: "))
numero2 = float(input("Introduzca otro numero: "))


if not numero2 == 0:
    division = numero1 / numero2 
    print(f"La division es {division}")
else: 
    print("Error.")
