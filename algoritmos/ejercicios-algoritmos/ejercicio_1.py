

#annos = [15,20,18,35,15,16,17,28,9,10]



def seleccion_des(arreglo):
    longitud = len(arreglo)
    for i in range(longitud-1):
        for j in range(i+1, longitud):
            if arreglo[i] > arreglo[j]:
                # Intercambiar
                arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
   


nombres = ["carlos", "maria", "pedro", "juan", "yaha", "diego", "paola", "luis", "flor", "andres"]
seleccion_des(nombres)

nombres = ["carlos", "maria", "pedro", "juan", "yaha", "diego", "paola", "luis", "flor", "andres"]
nombres.sort()
print(nombres)
