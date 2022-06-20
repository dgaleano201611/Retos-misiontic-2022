"""
Escribir un programa que almacene en una lista los siguientes
precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y
el mayor de los precios.
"""
# Una forma usando la funcion max y min
precios = [50, 75, 46, 22, 80, 65, 8]
print("El valor maximo de los precios es: ", max(precios))
print("El valor minimo de los precios es: ", min(precios))

# otra forma organizando la lista 
precios.sort()
print("EL valor maximo de los precios es: ", precios[-1])
print("EL valor minimo de los precios es: ", precios[0])
