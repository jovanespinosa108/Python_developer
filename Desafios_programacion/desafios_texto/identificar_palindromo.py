#instrucciones
#crea una funcion que identifique si un string sin puntuacion o acentuacion es o no palindromo 
#la funcion debe recibir una cadena de texto 
#debe regresar un booleano (True= palindromo/False= no es palindromo) 
#las letras mayusculas y minusculas debes ser tratadas iguales

def texto_es_palindromo(texto):

    texto_minusculas = texto.lower()
    texto_sin_espacios = texto_minusculas.replace(" ", "")
    return texto_sin_espacios == texto_sin_espacios[::-1]

print(texto_es_palindromo("La ruta nos aporto otro paso natural")) #True
print(texto_es_palindromo("La ruta nos aporto otro paso mas rapido")) #False
print(texto_es_palindromo) #<function texto_es_palindromo at 0x000001BE2FC7D120>
