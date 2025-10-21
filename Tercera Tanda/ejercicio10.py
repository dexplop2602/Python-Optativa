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

tipopizza = input("Quieres una pizza vegetariana o no vegetariana: ")

if tipopizza == "vegetariana":
    ingredientes2 = input ("Eliga unos de los ingredientes entre mozzarella y tomate: ")
    print (f"Los ingredientes son {ingredientes2}")
    ingredientesvegana = ("Ingredientes vegetarianos: Pimiento y tofu.")
    print (f"Los ingredientes son {ingredientes2} y {ingredientesvegana}")

if tipopizza == "no vegetariana":
    ingredientes2 = input ("Eliga unos de los ingredientes entre mozzarella y tomate: ")
    ingredientescarnivora = ("Ingredientes no vegetarianos: Peperoni, Jamón y Salmón.")
    print (f"Los ingredientes son {ingredientes2} y {ingredientescarnivora}")