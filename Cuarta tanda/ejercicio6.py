"""Ejercicio 6
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo, de altura el número introducido.
*
**
***
****
*****"""

numero = int(input("Escriba un numero entero: "))

a = 0
b = ""
while a <= numero:
    print(f"{b}")
    a += 1
    b += "*"