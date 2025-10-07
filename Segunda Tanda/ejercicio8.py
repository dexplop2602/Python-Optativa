"""Ejercicio 8
Escribir un programa que pregunte por consola el precio de un producto en euros
con dos decimales y muestre por pantalla el número de euros y el número de
céntimos del precio introducido."""

precio = input("Cual es el precio de producto con dos decimales (Euros): ")

print(f"El numero de euros es: {precio[:-3]}, los centimos: {precio[-2:]} ")