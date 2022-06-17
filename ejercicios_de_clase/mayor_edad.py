"""
programa que introduzca numbre y edades y dé como salida el nombre de la persona de mayor edad
qué edad tiene y el promedio de edades, y al oprimir * salir. 

"""
#listas a llenar
nombres = []
edades = []

# pedir nombres y edad y guardarlos en las listas
for i in range(1,10):
    nombre = input("ingrese el nombre:   ")
    if nombre == "*":
        break
    nombres.append(nombre)
    edad = int(input("ingrese la edad:  "))
    edades.append(edad)

print(nombres)
print(edades)  


# verificar cuál es el indice de la persona de mayor edad.
mayor = edades[0]
for edad in range(1, len(edades)):
    if mayor >= edades[edad]:
        obj = mayor
    else:
        mayor = edades[edad]

indice = edades.index(mayor)

#variables de la persona con mayor edad
nombre_mayor = nombres[indice]
edad_mayor = edades[indice]

#Promedio de edades
sum = 0
for i in edades:
    sum = sum + i 
prom = sum / len(edades)

#salidas
print(f"la persona de mayor edad es: {nombre_mayor} con {edad_mayor} años")
print("El promedio de edades es: ", prom)
    
    






