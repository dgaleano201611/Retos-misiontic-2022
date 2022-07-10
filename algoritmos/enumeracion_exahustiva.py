# El algoritmo de enumeración exahustiva consiste en probar todas las posibilidades, 
# se pensaría que es ineficiente pero debido a la velocidad de los computadores modernos
# la ejecucion es rapida.

# Ejemplo programa que calcula la raíz cuadrada exácta de un número.

objetivo = int(input("Escoge un entero: "))
respuesta = 0

while respuesta **2 < objetivo:
    #108638929print(respuesta)
    respuesta += 1

if respuesta ** 2 == objetivo:
    print(f"La raiz cuadrada de {objetivo} es {respuesta}")

else:
    print(f"{objetivo} no tiene una raiz cuadrada exacta")

