"""
Escribir un programa que almacene el abecedario en una lista,
elimine de la lista las letras que ocupen posiciones múltiplos de 3,
y muestre por pantalla la lista resultante.
"""
import string 

alphabet_string = string.ascii_uppercase
alphabet_list = list(alphabet_string)

print(alphabet_list)
# eso imprime la siguiente lista
"""['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 
'U', 'V', 'W', 'X', 'Y', 'Z']"""

# las letras a eliminar ocupan posiciones multiplos de 3 son: D G J M P S V Y
#los indices despues de cada eliminacion quedaria: 3, 5, 7, 9, 11 ...
indice = 3
while indice <= len(alphabet_list):
    alphabet_list.pop(indice)
    indice = indice + 2 #empezamos en 3 y sumamos dos en cada iteracion
print(alphabet_list)

