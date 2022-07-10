"""
Escribe una función llamada numDuplicados​ que reciba un string y retorne el número 
de caracteres que aparecen más de una vez.
​​
​​console.log(numDuplicados("abcaa")); // 1
​​console.log(numDuplicados("abab")); // 2
​​console.log(numDuplicados("abc")); // 0 
"""
# usando el metodo .count que devuelve el nuemro de veces que se repite una cadena

def numDuplicados(string):
    #contador de caracteres
    contador = 0
    for letra in string:
        if string.count(letra) > 1:
            contador += 1
            print(string)
            string = string.replace(letra, "")
            print(string)
            letra = 0
           
        else:
            pass
    
    return contador


print(numDuplicados("abbcaa"))
#print(numDuplicados("abab"))
#print(numDuplicados("abccbbbaaaddff"))