"""Ejercicio 4
Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre
por pantalla la misma fecha en formato dd de <mes> de aaaa donde <mes> es
el nombre del mes"""

fecha = input("Introduzca una fecha con este formato dd/mm/aaaa: ")

partir = fecha.split("/")

usuario = {}

usuario['dd'] = partir[0]
usuario['mm'] = partir[1]
usuario['aaaa'] = partir[2]

print(f"El dia es el {usuario["dd"]} del mes {usuario['mm']} del año {usuario['aaaa']}")
