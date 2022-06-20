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


# Ingreso de notas de las asignaturas
for asignatura in asignaturas:
    nota = float(input(f"cuanto ha sacado en la asignatura  de  {asignatura}: " ))
    notas.append(nota)

print(notas)

# Eliminar de las lista las asignaturas aprobadas
indice = 0
while indice < len(notas):
    if notas[indice] >= 3:
        notas.pop(indice)
        asignaturas.pop(indice)
    else:
        indice += 1

# impresión de las asignaturas a recuperar
for i in range(0, len(asignaturas)):
    print(f" desbes recuperar {asignaturas[i]}  con una nota de: {notas[i]}")