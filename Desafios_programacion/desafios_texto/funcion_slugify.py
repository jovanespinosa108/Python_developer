#Slug: Parte de la URL que utiliza palabras clave para ser legible
#slug solo contiene caracteres alfanumericos y guiones como separador
#slug convierte un string en url's
#Slugify: proceso de convertir un string a un slug
#Crea una funcion que reciba una cadena de texto y la regrese como slug
#el string debe remover caracteres no-alfanumericos: 
#slash /, backslash \, asteriscos *, porcentage %
#los espacios de un string deben ser replazados por un guion
#usar solo libreria "re" si es necesario

import re

def slugify(texto):

    slug = (texto
        .lower()
        .strip()
        .replace(" ", "")
    )
    slug = re.sub("[^\w\-]", "", slug)
    return slug

print(slugify("texto$ con caracteres# especial-es"))
print(slugify("Ejemplo con espacios y caracteres !!!"))

