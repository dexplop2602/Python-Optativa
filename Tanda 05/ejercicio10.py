"""Ejercicio 10
Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46,
22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios"""

lista = [50, 75, 46, 22, 80, 65, 8]

mayor = lista[0]
menor = lista[0]

for precio in lista:
    if precio > mayor:
        mayor = precio
    if precio < menor:
        menor = precio

print("El precio mayor es:", mayor)
print("El precio menor es:", menor)