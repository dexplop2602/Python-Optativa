"""Ejercicio 7
Escribir un programa que cree un diccionario simulando una cesta de la compra. El
programa debe preguntar el artículo y su precio y añadir el par al diccionario, hasta
que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la
compra y el coste total, con el siguiente formato
Lista de la compra
Artículo 1 Precio
Artículo 2 Precio
Artículo 3 Precio
… …
Total Coste"""

compra = {}

while True:
    articulo = input("Escriba su Artículo (o escriba 'salir' para terminar): ")
    
    if articulo == "salir":
        break
    else:
        precio = float(input(f"Escriba el precio de {articulo}: "))
        compra[articulo] = precio

print("\nLista de la compra")
total = 0

for nombre_articulo, coste in compra.items():
    print(f"{nombre_articulo}\t{coste}")
    total += coste 

print(f"Total\t{total}")