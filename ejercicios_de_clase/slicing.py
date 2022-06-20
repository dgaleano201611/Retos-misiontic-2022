from filecmp import cmp


num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# invertir una lista
num.reverse()
print(num)

longitud_1 = len(num)
# Ordear una lista 

desorden = [5, 4, 7, 9, 3, 2, 1, 8, 9, 10]
desorden.sort()
print(desorden)

longitud_2 = len(desorden)
print(longitud_1, longitud_2)

#print(cmp(longitud_1, longitud_2))

a = 5
b = 3

