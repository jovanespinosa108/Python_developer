#para validar un correo usamos libreria "re"
import re


#creamos funcion para validar el email
def validar_email(email):
    formato_valido = r"^([a-z,0-9]+[-_.])*[a-z,0-9]+@[a-z,0-9]+(\.[a-z]{2,})+$"
    if re.match(formato_valido, email, re.IGNORECASE):
        return True
    return False

validar1 = validar_email("mayra_r@email.com")
print("Email valido:", validar1)
#Email valido: True

validar2 = validar_email("invalido-024_@email.com") #invalido _ antes del @
print("Email valido:", validar2)
#Email valido: False

"""
r significa raw string
^ (Caret)indica que el texto debe coincidir con el inicio
$ indica que el texto debe coincidir con el final
[a-z,0-9] puedes agregar cualquier caracter en los rangos
+ signica al menos un caracter de ese tipo
[-_.] no se le agreaga el mas porque son caracteres no obligatorios
* indica que bucara 1 o mas ocurrencias dentro del nombre de usuario
[a-z,0-9]+ valida que el email no tenga _-. antes del @
(\.[a-z]{2,})+ valida el domino .com, .net etc, captura mas de 1 ocurrencia despues del punto
"""
