"""Ejercicio 3
Escribir un programa que guarde en un diccionario los precios de las frutas de la
tabla, pregunte al usuario por una fruta, un número de kilos y muestre por pantalla el
precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe
mostrar un mensaje informando de ello.

Fruta Precio
Plátano 1.35
Manzana 0.80
Pera 0.85
Naranja 0.70
"""

diccionario = {"Platano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}

fruta = input("Elija una fruta: ")
kilos = float(input("Cuantos kilos quiere: "))

if fruta in diccionario:
    total = diccionario[fruta] * kilos
    print(f"El precio es de {total}")
else:
    print(f"La fruta no esta disponible en el diccionario")