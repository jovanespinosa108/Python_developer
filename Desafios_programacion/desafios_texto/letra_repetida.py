#crea una funcion que reciba un string o texto
#retorne el primer caracter repetido
#no debe retornar un espacio vacio como primer caracter
#si no hay caracteres repetidos regresara "None"

def caracter_repetido(texto):

    texto_minuscula = texto.lower() #recibe el texto para convertirlo en minusculas
    texto_sin_espacios = texto_minuscula.replace(" ", "") #replazamos los espacios por strings vacios
    lista_letras = []
    for letra in texto_sin_espacios:  #itera sobre cada letra en "texto"
        if letra in lista_letras:
            return letra # retorna la primera letra repetida
        else:
            lista_letras.append(letra) #agrega las letras no repetidas a la lista vacia

    return None

print(caracter_repetido("hola")) #None
print(caracter_repetido("hola paola")) #a
