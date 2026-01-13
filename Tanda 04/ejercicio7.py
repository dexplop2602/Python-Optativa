"""Ejercicio 7
Escribir un programa que muestre por pantalla la tabla de multiplicar del 1 al 10"""

cont = 1
while cont <= 10:
    contador = 1
    print (f"Tabla del {cont}")
    while contador <= 10:
        print(f"{cont * contador}, ")
        contador += 1
    cont += 1