codigo = int(input())
nombre = input()
cantidad = int(input())
valor_unitario = float(input())
valor_producto = valor_unitario * cantidad
valor_final_producto = valor_producto + valor_producto * (0.19)
print(codigo)
print(nombre)
print(valor_producto)
print(valor_final_producto)