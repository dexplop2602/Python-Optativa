"""Ejercicio 13
Escribir un programa que pregunte por una muestra de números, separados por
comas, los guarde en una lista y muestre por pantalla su media y desviación típica."""

import math

numeros = input("Escriba una lista de numeros separados por coma: ")

separar = numeros.split(",")

suma = 0
for i in separar:
    i = int(i)
    suma = i + suma

media = suma / len(separar)

suma_cuadrados = 0 
for a in separar:
    a = int(a)
    suma_cuadrados = suma_cuadrados + (a - media)**2

varianza = suma_cuadrados / len(separar)

desviacion_tipica = math.sqrt(varianza)

print(f"La suma es {suma}")
print(f"La media de los numeros: {media}")
print(f"La desviacion es: {round(desviacion_tipica, 5)}")