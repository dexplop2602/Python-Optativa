"""Ejercicio 8
Escribir un programa que pida al usuario un número entero y muestre por pantalla
un triángulo rectángulo como el de más abajo.
1
3 1
5 3 1
7 5 3 1
9 7 5 3 1"""

numero = int(input("Introduzca un numero entero: "))

cont = 1
while cont <= numero:
    resultado = (cont * 2) - 1
    while resultado >= 1:
        print(resultado, end=" ")
        resultado -= 2 
    print()
    
    cont += 1

