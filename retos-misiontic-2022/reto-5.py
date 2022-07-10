
# catalogo de articulos y precios con llave codigo del artículo
articulos={1:"Lapiz", 2:"Cuaderno", 3:"Borrador", 4:"Regla", 5:"ColoresX12", 6:"Escuadra", 7:"Calculadora", 8:"CrayonesX6"}
precios={1:2500,2:4500,3:1500,4:5000,5:24000,6:4700,7:45000,8:8900}

# n es el numero de artículos de diferente tipo comprados
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

    nombre = articulos.get(codigo) # el nombre se lee del diccionario articulos
    
    cantidad = float(input("cantidad: "))

    
    valor_unitario = precios.get(codigo) # codigo se lee del diccionario precios.

    tipo_iva = int(input("Tipo de iva: "))
    valor_producto = valor_unitario * cantidad
    
    if tipo_iva == 1:
        iva = 0
    elif tipo_iva == 2:
        iva = valor_producto * 0.05
    else:
        iva = valor_producto * 0.19
    
    # Calculos 
    
    valor_final_producto = valor_producto + iva
    total = total + valor_final_producto
    total_iva = total_iva + iva

    # Introducir datos en la lista producto
    producto.append(codigo)
    producto.append(nombre)
    producto.append(valor_producto)
    producto.append(valor_final_producto)

    # Llenar lista madre productos con sublistas de cada producto
    productos.append(producto)


#Impresion de datos
for producto in productos:
    for datos in range(len(producto)):
        print(producto[datos])

print(total)
print(total_iva)