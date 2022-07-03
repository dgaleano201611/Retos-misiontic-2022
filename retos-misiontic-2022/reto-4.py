n = int(input("cantidad de productos diferentes: "))

#inicialización de cantidades sumativas
total = 0
total_iva = 0

#lista que va a contener los datos de cada producto en sublistas
productos = []

# Datos a ingresar
for i in range(1, n+1, 1):
    producto = []
    codigo = int(input("codigo: "))
    nombre = input("nombre: ")
    cantidad = int(input("cantidad: "))
    valor_unitario = float(input("Valor unitario: "))
    tipo_iva = int(input("Tipo de iva: "))
    valor_producto = valor_unitario * cantidad
    
    if tipo_iva == 1:
        iva = 0
    elif tipo_iva == 2:
        iva = valor_producto * 0.5
    else:
        iva = valor_producto * 0.19
    
    # Calculos 
    
    valor_final_producto = valor_producto + iva
    total = total + valor_final_producto
    total_iva = total_iva + iva

    # Introducir datos en la lista producto
    producto.append(nombre)
    producto.append(codigo)
    producto.append(iva)
    producto.append(valor_producto)
    producto.append(valor_final_producto)

    # Llenar lista madre productos con sublistas de cada producto
    productos.append(producto)

#ordenado de lista por orden alfabetico del nombre del producto
productos.sort()  

#Impresion de datos
for producto in productos:
    for datos in range(1,len(producto)):
        print(producto[datos])

print(total)
print(total_iva)