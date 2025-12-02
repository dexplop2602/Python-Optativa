"""Ejercicio 12
Escribir un programa que almacene las matrices
en una lista y muestre por pantalla su producto.
Nota: Para representar matrices mediante listas usar listas anidadas, representando
cada vector fila en una lista"""

A = [[1, 2, 3],
     [4, 5, 6]]

B = [[-1, 0],
     [0, 1],
     [1, 1]]

resultado = []

for i in range(len(A)):
    fila_nueva = []
    for j in range(len(B[0])):
        suma = 0
        for k in range(len(B)):
            suma += A[i][k] * B[k][j]
        fila_nueva.append(suma)
    resultado.append(fila_nueva)

for fila in resultado:
    print(fila)