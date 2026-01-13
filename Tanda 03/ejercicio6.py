"""Ejercicio 6
Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y
el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y
los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un
programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo
que le corresponde."""

nombre = input("Escriba su nombre: ")
sexo = input("Escriba su sexo: ")

nombre = nombre.lower()
sexo = sexo.lower()

grupo = ""

if sexo == "hombre":
    if nombre > "N":
      grupo = "B"
else:
      grupo = "A"

if sexo == "mujer":
    if nombre < "M":
        grupo = "A"
else:
        grupo = "B"

print(f"Su grupo es {grupo}")