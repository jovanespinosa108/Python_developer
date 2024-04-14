#Anagrama: palabras que continene las mismas letras: ramo, mora, amor etc
#crea una funcion que determine si 2 palabras son anagramas
#la funcion retorna True si es anagrama o False si no es
#no distincion de mayusculas-minusculas

def es_anagrama(palabra1, palabra2):

    letras_palabra1 = sorted(palabra1.lower())
    letras_palabra2 = sorted(palabra2.lower())
    return letras_palabra1 == letras_palabra2

print(es_anagrama("ramo", "caro")) #False
print(es_anagrama("ramo", "mora")) #True
print(es_anagrama("loma", "malo")) #True

