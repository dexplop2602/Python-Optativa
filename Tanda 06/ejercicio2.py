"""Ejercicio 2
Escribir un programa que pregunte al usuario su nombre, edad, dirección y teléfono
y lo guarde en un diccionario. Después debe mostrar por pantalla el mensaje
<nombre> tiene <edad> años, vive en <dirección> y su número de
teléfono es <teléfono>."""

nombre = input("Escriba su nombre: ")
edad = input("Escriba su edad: ")
direccion = input("Escriba su direccion: ")
telefono = input("Indique su telefono: ")

usuario = {}

usuario['nombre'] = nombre
usuario['edad'] = edad
usuario['direccion'] = direccion
usuario['telefono'] = telefono

print(f"El nombre es {usuario['nombre']}, tiene {usuario['edad']} años, vive en {usuario['direccion']} y su numero de telefono es {usuario['telefono']} ")