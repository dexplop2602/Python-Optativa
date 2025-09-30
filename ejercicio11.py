"""Ejercicio 11
Imagina que acabas de abrir una nueva cuenta de ahorros que
te ofrece el 4% de interés al año. Estos ahorros debido a
intereses, que no se cobran hasta finales de año, se te añaden
al balance final de tu cuenta de ahorros. Escribir un programa
que comience leyendo la cantidad de dinero depositada en la
cuenta de ahorros, introducida por el usuario. Después el
programa debe calcular y mostrar por pantalla la cantidad de
ahorros tras el primer, segundo y tercer años. Redondear cada
cantidad a dos decimales."""

Interes = 0.04
cantidad = float(input("Pon tu dinero depositado: "))

primer = cantidad - cantidad * Interes
segundo = cantidad - (cantidad * (Interes * 2))
tercer = cantidad - (cantidad * (Interes * 3))

print (f"Cantidad tras el primer año: {primer}, Cantidad tras el segundo año: {segundo}, Cantidad tras el tercer año: {tercer} ")