#instrucciones
#crea una funcion que identifique si un string sin puntuacion o acentuacion es o no palindromo 
#la funcion debe recibir una cadena de texto 
#debe regresar un booleano (True= palindromo/False= no es palindromo) 
#las letras mayusculas y minusculas debes ser tratadas iguales

def texto_es_palindromo(texto): # funcion que almacena el texto de print

    texto_minusculas = texto.lower() # se crea una variable para convertir en minusculas todo el texto
    texto_sin_espacios = texto_minusculas.replace(" ", "") #remplaza el espacio del texto por no espacio
    return texto_sin_espacios == texto_sin_espacios[::-1] # Itera el texto de atras hacia adelante

print(texto_es_palindromo("La ruta nos aporto otro paso natural")) #True
print(texto_es_palindromo("La ruta nos aporto otro paso mas rapido")) #False
print(texto_es_palindromo) #<function texto_es_palindromo at 0x000001BE2FC7D120>


#crea una funcion que almacene el texto en print
#crea una variable que convierta todo el texo en minusculas
#crea una variable con el texto convertido en minusculas y usa replace() para reemplazar los espacios vacios por no espacios
#si la variable texto_sin_espacios es igual a texto_sin_espacios leida alrevez entonces regresa True de otra manera regresa False
