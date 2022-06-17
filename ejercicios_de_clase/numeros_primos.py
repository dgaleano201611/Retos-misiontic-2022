#se define la lista vacia donde van los numeros primos
primos = []

#contadores
i = 2 #contador externo
j = 2 #cobtador interno


while i <= 1000:   
  while i%j != 0:
    j += 1
  if i == j:
    primos.append(i)
  j=2 
  i += 1

print(primos)