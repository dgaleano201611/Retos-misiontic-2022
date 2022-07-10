with open("./ejercicios_de_clase/archivos/informacion.txt", "a") as f:
    for i in range(1, 3):
        nombre = input("Nombre del estudiante")
        codigo = input("Ingrese el codigo")
        f.write(nombre)
        f.write(codigo)



