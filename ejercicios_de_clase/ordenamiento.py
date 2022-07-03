#Ordenamiento por selección: 

#lista = [56, 46, 20, 10, 59, 1050, 1, 67, 4, 34]
#def seleccion(arreglo):



def seleccion(arreglo):
    longitud = len(arreglo)
    # ciclo de recorrido
    for i in range(longitud-1):
            # ciclo de comparacion 
      for j in range(i+1, longitud):
        if arreglo[i] > arreglo[j]:
          arreglo[i], arreglo[j] = arreglo[j], arreglo[i]
          print(arreglo)
               
                
 
arreglo = [3,12,85,20,23,10,1]
seleccion(arreglo)
print(arreglo)