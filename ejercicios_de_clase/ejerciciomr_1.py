def calcular_impuestos(edad, ingresos):
    if edad >= 18 and ingresos >= 1000:
        valor = ingresos*0.4
        return valor
    else:
        return 0

    

print(calcular_impuestos(18, 1000))
print(calcular_impuestos(40, 10000))
print(calcular_impuestos(17, 5000))