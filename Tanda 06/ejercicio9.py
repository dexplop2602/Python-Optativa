"""Ejercicio 9
Escribir un programa que gestione las facturas pendientes de cobro de una
empresa. Las facturas se almacenarán en un diccionario donde la clave de cada
factura será el número de factura y el valor el coste de la factura. El programa debe
preguntar al usuario si quiere añadir una nueva factura, pagar una existente o
terminar. Si desea añadir una nueva factura se preguntará por el número de factura
y su coste y se añadirá al diccionario. Si se desea pagar una factura se preguntará
por el número de factura y se eliminará del diccionario. Después de cada operación
el programa debe mostrar por pantalla la cantidad cobrada hasta el momento y la
cantidad pendiente de cobro."""

facturas = {}
cobrado = 0

while True:
    respuesta = input("Añadir (1) \n Pagar (2) \n Terminar (3): ")
    
    if respuesta == "3":
        break
    elif respuesta == "1":
        clave = input("Numero de factura: ")
        coste = float(input("Coste: "))
        facturas[clave] = coste
    elif respuesta == "2":
        clave = input("Numero de factura: ")
        cobrado += facturas.pop(clave, 0)

    print("Cobrado:", cobrado)
    print("Pendiente:", sum(facturas.values()))