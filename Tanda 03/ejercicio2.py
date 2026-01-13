"""Ejercicio 2
Escribir un programa que almacene la cadena de caracteres contraseña en una
variable, pregunte al usuario por la contraseña e imprima por pantalla si la
contraseña introducida por el usuario coincide con la guardada en la variable sin
tener en cuenta mayúsculas y minúsculas."""

contra2 = "contraseña"

contra = str(input("Escriba su contraseña: "))
contra = contra.lower()

if contra == contra2:
    print ("Su contraseña es correcta")
else:
    print ("Su contraseña es incorrecta intentelo de nuevo")