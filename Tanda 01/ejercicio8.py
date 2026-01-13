"""Ejercicio 8
Escribir un programa que pida al usuario dos números enteros
y muestre por pantalla la <n> entre <m> da un cociente <c>
y un resto <r> donde <n> y <m> son los números introducidos
por el usuario, y <c> y <r> son el cociente y el resto de la
división entera respectivamente."""

Numero1 = float(input("Introduce un numero entero:"))
Numero2 = float(input("Introduce un numero entero:"))

cociente = Numero1 // Numero2
resto = Numero1 % Numero2

print (f"{Numero1}, / {Numero2}, da un cociente de {cociente} y un resto de {resto}")