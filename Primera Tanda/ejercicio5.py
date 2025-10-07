"""Ejercicio 5
Escribir un programa que pregunte al usuario por el número de
horas trabajadas y el coste por hora. Después debe mostrar
por pantalla la paga que le corresponde."""

Horas = float(input("Cuantas horas trabaja: "))
Paga = float(input("Que paga tiene: "))

Calculo = Horas * Paga

print (f"Le corresponde una paga de {Calculo}")