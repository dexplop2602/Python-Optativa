"""Ejercicio 9
Escribir un programa que pida al usuario una palabra y muestre por pantalla el
número de veces que contiene cada vocal"""

palabra = input("Escriba una palabra: ")

a = 0
e = 0
i = 0
o = 0
u = 0

for letra in palabra:
    if letra == "a":
        a += 1
    if letra == "e":
        e += 1
    if letra == "i":
        i += 1
    if letra == "o":
        o += 1
    if letra == "u":
        u += 1

print (f"La palabra contiene {a} (a), contiene {e} (e),contiene {i} (i), contiene {o} (o), contiene {u} (u)")