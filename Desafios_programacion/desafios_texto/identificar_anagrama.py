#Anagrama: palabras que continene las mismas letras: ramo, mora, amor etc
#crea una funcion que determine si 2 palabras son anagramas
#la funcion retorna True si es anagrama o False si no es
#no distincion de mayusculas-minusculas

def es_anagrama(palabra1, palabra2): #recibe 2 palabras como argumentos para saber si son anagramas

    letras_palabra1 = sorted(palabra1.lower()) #la funcion sorted ordena los caracteres de forma alfabetica, lower para minusculas
    letras_palabra2 = sorted(palabra2.lower()) #la funcion sorted ordena los caracteres de forma alfabetica, lower para minusculas
    return letras_palabra1 == letras_palabra2 #retorna true or false si la palabra 1 tiene las mismas letras que la palabra 2

print(es_anagrama("ramo", "caro")) #False
print(es_anagrama("ramo", "mora")) #True
print(es_anagrama("loma", "malo")) #True

#crea una funcion que contenga 2 argumentos que guardaran el texto del print de 2 palabras
#crea 2 variables, una para cada palabra, 
#se usa la funcion sorted() para ordenar las letras de cada palabra en orden alfabetico
#dentro de la funcion sorted se usa la funcion lower() para convertir las letras a minusculas
#en return comparamos las 2 varibles para saber si contienen palabras con las mismas letras
#se son iguales retornara True, si no lo son, retornara False
