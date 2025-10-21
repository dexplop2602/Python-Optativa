"""Ejercicio 10
La pizzería Bella Napoli ofrece pizzas vegetarianas y no vegetarianas a sus clientes.
Los ingredientes para cada tipo de pizza aparecen a continuación.

● Ingredientes vegetarianos: Pimiento y tofu.
● Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.

Escribir un programa que pregunte al usuario si quiere una pizza vegetariana o no, y
en función de su respuesta le muestre un menú con los ingredientes disponibles
para que elija. Solo se puede elegir un ingrediente además de la mozzarella y el
tomate que están en todas las pizzas. Al final se debe mostrar por pantalla si la
pizza elegida es vegetariana o no y todos los ingredientes que lleva."""

tipopizza = input("Quieres una pizza vegetariana si o no: ")

if tipopizza == "si":
    ingredientes = "Los ingredientes son: Pimiento, Tofu"
    print (f"{ingredientes}")
if tipopizza == "no":
    ingredientes = "Los ingredientes son: Peperoni, Jamon y Salmon"
    print (f"{ingredientes}")