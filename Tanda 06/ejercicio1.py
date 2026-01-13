"""Ejercicio 1
Escribir un programa que guarde en una variable el diccionario {'Euro':'€',
'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su
símbolo o un mensaje de aviso si la divisa no está en el diccionario"""

diccionario =  {'Euro':'€','Dollar':'$', 'Yen':'¥'}

divisa = input("Escriba una divisa, Euro, Dollar, Yen: ")

divisa2 = 0
for i in diccionario:
    if i != divisa:
        divisa2 = 0
    else:
        divisa2 += 1
        break

if divisa2 == 1:
    print(f"La divisa {divisa} si existe en el diccionario")
else:
    print(f"La divisa {divisa} no esta disponible en el diccionario")