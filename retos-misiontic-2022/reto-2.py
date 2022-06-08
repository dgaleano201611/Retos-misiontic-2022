n = int(input())
total = 0
total_iva = 0
datos = []
for i in range(1, n+1, 1):
    codigo = int(input())
    nombre = input()
    cantidad = int(input())
    valor_unitario = float(input())
    tipo_iva = int(input())
    if tipo_iva == 1:
        iva = 0
    elif tipo_iva == 2:
        iva = 5
    else:
        iva = 19
    valor_producto = valor_unitario * cantidad
    valor_iva = valor_producto * (iva/100)
    valor_final_producto = valor_producto + valor_iva
    total = total + valor_final_producto
    total_iva = total_iva + valor_iva
    datos.append(codigo)
    datos.append(nombre)
    datos.append(valor_producto)
    datos.append(valor_final_producto)
for i in datos:
    print(i)
print(total)
if total_iva == 0:
    total_iva = int(total_iva)
    print(total_iva)
else:  
    print(total_iva)


    
    



