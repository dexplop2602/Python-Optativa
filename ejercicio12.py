"""Ejercicio 12
Una panadería vende barras de pan a 3.49€ cada una. El pan
que no es el día tiene un descuento del 60%. Escribir un
programa que comience leyendo el número de barras vendidas
que no son del día. Después el programa debe mostrar el
precio habitual de una barra de pan, el descuento que se le
hace por no ser fresca y el coste final total."""

precio = 3.49
descuento = 0.6

numero = float(input("Ingresa el numero de barras vendidas: "))

CosteNormal = numero * precio
Costefinal = numero * (precio * descuento)

print(f"El precio habitual por barra {precio}")
print(f"El de las barras que usted ha comprado: {CosteNormal:.2f}")
print(f"Se le hace un descuento del 60%")
print(f"El precio total es de {Costefinal:.2f}")