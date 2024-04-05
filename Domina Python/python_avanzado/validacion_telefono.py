import phonenumbers

def valid_phonenumber(phonenum_str, country_code=None):
    phonenumber = phonenumbers.parse(phonenum_str, country_code)
    return phonenumbers.is_valid_number(phonenumber)

validate = valid_phonenumber("+513336857489")
print(validate)
#False

validate2 = valid_phonenumber("+523006857489")
print(validate2)
#True

#en lugar del codigo del pais podemos poner su abreviacion
validate3 = valid_phonenumber("3006857489", "MX")
print(validate3)
#True

"""
def valid_phonenumber(phonenum_str, country_code=None):
    try:
        phonenumber = phonenumbers.parse(phonenum_str, country_code)
        return phonenumbers.is_valid_number(phonenumber)
    except Exception as e:
        print(e)
        return False
"""
#usamos try-except para evitar que salga cualquier error 
#se imprimira False y el error que se ha generado
#El código del país que se debe usar es el ISO 3166-1, 
#que es el código de dos letras que representa el nombre de un país. 

