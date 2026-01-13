"""Ejercicio 5
Escribir un programa que pregunte al usuario una cantidad a invertir, el interés anual
y el número de años, y muestre por pantalla el capital obtenido en la inversión cada
año que dura la inversión."""

Capital = float(input("Pon tu capital: "))
Tasa = float(input("Pon tu tasa de interes: "))
anio = float(input("Pon tu tiempo años: "))

a = 1
while a <= anio:
    suma = a * Tasa / 100 * Capital
    print (f"El interes del año {a} es {suma}")
    a += 1