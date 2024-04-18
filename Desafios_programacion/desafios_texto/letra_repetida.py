#crea una funcion que reciba un string o texto
#retorne el primer caracter repetido
#no debe retornar un espacio vacio como primer caracter
#si no hay caracteres repetidos regresara "None"

def caracter_repetido(texto):

    texto_minuscula = texto.lower() #recibe el texto para convertirlo en minusculas
    texto_sin_espacios = texto_minuscula.replace(" ", "") #1er argumento es lo que se va a remplazar, 2do arg es lo que remplaza
    lista_letras = [] #lista vacia para almacenar letras iteradas
    for letra in texto_sin_espacios:  #itera sobre cada letra en "texto"
        if letra in lista_letras: # si la letra esta en texto sin espacios entonces
            return letra # retorna la letra repetida
        else: #de otro modo
            lista_letras.append(letra) #agrega las letra iteradas a la lista vacia y continua iterando

    return None # si no encuentra letras repetidas retornara None

print(caracter_repetido("hola")) #None
print(caracter_repetido("hola paola")) #a


#Se crea una funcion donde se almacenara el texto
#dentro de la funcion se crea una variable para cambiar todas las letras a minusculas
#Se crea otra variable donde se llamara a la varible que ya contiene el texo en minusculas
#esta variable eliminara todos los espacios que tenga el texto
#se crea una lista para que el programa almacene las letras mientras vaya iterando
#se crea un ciclo for para iterar letra por letra el texto listo sin mayusculas y sin espacios
#osea la variable: texto_sin_espacios
#se crea la condicion para encontrar la letra repetida
#esto es: si la letra iterada ya se encuentra en la lista vacia, entonces retornala
#de otra manera, almacenala en la lista vacia y sigue iterando
#esta iteracion se repite hasta que termine el texto
#Si el programa no encuentra palabras repetidas regresa None
