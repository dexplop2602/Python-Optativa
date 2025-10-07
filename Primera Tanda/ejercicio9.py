"""Ejercicio 9
Escribir un programa que pregunte al usuario una cantidad a
invertir, el interés anual y el número de años, y muestre por
pantalla el capital obtenido en la inversión."""

Capital = float(input("Pon tu capital: "))
Tasa = float(input("Pon tu tasa de interes: "))
Tiempo = float(input("Pon tu tiempo años: "))

Resultado = Capital * Tasa / 100 * Tiempo

print((f"El precio de interes es de: {Resultado}"))