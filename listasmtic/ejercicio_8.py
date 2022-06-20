"""
Escribir un programa que pida al usuario una palabra y muestre
por pantalla si es un palíndromo.

"""
palabra = input("Ingrese una palabra para verificar si es palíndromo")

#validaciones 
palabra_minuscula = palabra.lower()
palabra_sin_comas = palabra_minuscula.replace(",", "")
palabra_2 = palabra_sin_comas.replace(" ", "")

#convertimos a lista y le damos la vuelta
inverza = list(palabra_2)
inverza.reverse()

#convertimos nuevamente a cadena de caracteres
new_word = "".join(inverza)

#verificamos si es palindromo   
if palabra_2 == new_word:
    print(True)
    
else:
    print(False)

#palabras para probar
#No Mara, sometamos o matemos a Ramon -->True
#ana -->True
#juan -->false
