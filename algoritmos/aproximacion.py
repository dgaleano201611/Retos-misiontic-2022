

objetivo = int(input("Escoge un numero: "))
epsilon = 0.001
paso = epsilon**2
respuesta = 0.0

while abs(respuesta ** 2 - objetivo) >= epsilon and respuesta <= objetivo:
    respuesta += paso
    print(abs(respuesta ** 2 - objetivo), respuesta)

if abs(respuesta ** 2 - objetivo) >= epsilon:
    print("No se encuentra la raiz cuadrada")

else:
    print(f"la raiz cuadrada de {objetivo} es {respuesta}")


