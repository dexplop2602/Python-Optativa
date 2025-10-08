""" Ejercicio 11
Escribir un programa que pregunte el nombre el un producto, su precio y un número
de unidades y muestre por pantalla una cadena con el nombre del producto seguido
de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con
3 dígitos y el coste total con 8 dígitos enteros y 2 decimales."""

nombre = input("Introduzca el nombre del producto: ")
unidades = float(input("Introduzca las unidades que quiere comprar: "))
precio = float(input("Introduzca el precio de compra: "))

preciototal = precio * unidades

precio = str(precio)

unidades = str(unidades)

preciototal = str(preciototal)

print (f"Nombre:{nombre}, Precio:{precio[:-6]}{precio[-2:]}, Numero de unidades: {unidades[:-3]}, Precio Total {preciototal[:-8]}{preciototal[:-2]}")
