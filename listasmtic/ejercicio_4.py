"""
Escribir un programa que pregunte al usuario los números
ganadores de la lotería primitiva, los almacene en una lista y los
muestre por pantalla ordenados de menor a mayor.
"""

numeros_ganadores = []

for i in range(0,6):
    numeros = input("Ingrese los numeros ganadores  ")
    numeros_ganadores.append(numeros)

numeros_ganadores.sort()
print(numeros_ganadores)
