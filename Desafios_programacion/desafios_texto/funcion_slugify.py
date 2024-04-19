#Slug: Parte de la URL que utiliza palabras clave para ser legible
#slug solo contiene caracteres alfanumericos y guiones como separador
#no contienen caracteres especiales
#slug convierte un string en url's
#Slugify: proceso de convertir un string a un slug
#Crea una funcion que reciba una cadena de texto y la regrese como slug
#el string debe remover caracteres no-alfanumericos: 
#slash /, backslash \, asteriscos *, porcentage %
#los espacios de un string deben ser replazados por un guion
#usar solo libreria "re" si es necesario

import re   #libreira regular expressions

def slugify(texto): #la funcion guarda el texto como parametro que sera convertido a url

    slug = (texto
        .lower() #convierte el texto en minusculas
        .strip() #remueve los espacios que tiene el texto antes y despues
        .replace(" ", "-") #remplaza los espacios por guiones
    )
    slug = re.sub("[^\w\-]", "", slug) #modifica varaible para que remueva los caracetes especiales
    return slug

print(slugify("texto$ con caracteres# especial-es")) #texto-con-caracteres-especial-es
print(slugify("Ejemplo con espacios y caracteres!!!")) #ejemplo-con-espacios-y-caracteres   

#importa la libreria re para regular expressions
#crea la funcion slugify para guardar el texto a modificar
#crea una variable para modificar el texto asignando como valor el argumento de la funcion y otras funciones
#usa las funciones lower(), strip() para modificar, pon un "." al principo de las funciones
#en la funcion replace() el primer argumento es para lo que queremos modificar y el segundo para lo que queremos remplazar
#modifica la primera varible usando la funcion sub() de la libreria re para remover los caracteres especiales
#en una lista como primer argumento y dentro el caracter: ^\ es para los caracteres que no estan en la expresion
#el segundo caracter: w\ es para los caracteres alfa-numericos
#el tercer caracter: "-" es para los guiones
#el segundo argumento es para remplazar estos caracteres
#el tercer agumento es la variable a modificar
#se retorna la variable modificada

