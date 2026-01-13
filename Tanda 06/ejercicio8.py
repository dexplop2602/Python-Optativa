"""Ejercicio 8
Escribir un programa que cree un diccionario de traducción español-inglés. El
usuario introducirá las palabras en español e inglés separadas por dos puntos, y
cada par <palabra>:<traducción> separados por comas. El programa debe
crear un diccionario con las palabras y sus traducciones. Después pedirá una frase
en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra
no está en el diccionario debe dejarla sin traducir."""

entrada = input("Lista (hola:hello,perro:dog): ")
diccionario = {}

pares = entrada.split(",")

for i in pares:
    lista = i.split(":")
    diccionario[lista[0]] = lista[1]

frase = input("Frase: ")
palabras = frase.split(" ")

for p in palabras:
    if p in diccionario:
        print(diccionario[p], end=" ")
    else:
        print(p, end=" ")