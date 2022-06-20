"""
Escribir un programa que pida al usuario una palabra y muestre
por pantalla el número de veces que contiene cada vocal.
"""

vocales = ["a", "e", "i", "o", "u"]

palabra = input("Ingrese una palabra")

#validaciones
palabra2 = palabra.lower()
print(palabra2)
palabra3 = "".join(palabra2)
print(palabra3)

for vocal in vocales:
    conteo_vocales = palabra3.count(vocal)
    print(f"vocal {vocal} hay {conteo_vocales}")




