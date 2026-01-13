""" Ejercicio 10
Escribir un programa que pregunte por consola por los productos de una cesta de la
compra, separados por comas, y muestre por pantalla cada uno de los productos en
una línea distinta."""

productos = input("Introduzca la cesta de la compra separada por comas: ")

partir = productos.split(",") 

print (*partir , sep="\n")

# ( * ) Desenpaqueta el contenido de la variable
# sep es una funcion que tiene python que indica que el contenido de la variable anterior lo va a separan por salto de linea