"""
Escribir un programa que almacene las asignaturas de un curso
(por ejemplo Matemáticas, Física, Química, Historia y Lengua) en
una lista, pregunte al usuario la nota que ha sacado en cada
asignatura y elimine de la lista las asignaturas aprobadas. Al final
el programa debe mostrar por pantalla las asignaturas que el
usuario tiene que repetir.
"""

asignaturas = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
notas = []
indices = []

# Ingreso de notas de las asignaturas
for asignatura in asignaturas:
    nota = float(input("cuanto ha sacado en la asignatura  de " + asignatura ))
    notas.append(nota)

print(notas)

# Indices de notas aprobadas 
for i in range(0, len(notas)):
    if notas[i] >= 3:
        indices.append(i)

print(indices)

# Eliminar de las lista las asignaturas aprobadas
for indice in indices:
    asignaturas.pop(indice)
    notas.pop(indice)



#for nota in notas:
    #if nota >= 3.0:
        #indice = notas.index(nota)
        #indices.append(indice)
        #notas.pop(indice)
        #asignaturas.pop(indice)

print(notas)
print(indices)

for i in range(0, len(asignaturas)):
    print(f" desbes recuperar {asignaturas[i]}  con una nota de: {notas[i]}")