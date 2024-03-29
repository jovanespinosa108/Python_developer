#Crear un closure que se encargue de agregar a un diccionario 
#el nombre de una persona y algunos de sus datos personales, 
#como la edad y la ciudad donde viven.

def agregar_persona_directorio():
    directorio = {}
    def agregar(nombre, edad, cuidad):
        directorio[nombre] = {"edad":edad, "cuidad":cuidad}
        return directorio
    return agregar

almacenar = agregar_persona_directorio()
directorio = almacenar("Juan", 35, "San Pedro")
directorio = almacenar("Nancy", 78, "Madrid")
directorio = almacenar("Rosalio", 23, "Montevideo")
print(directorio)

# Closure: debe cumplir tres condiciones. 
#1 Debe haber una función anidada, "def agregar" (una funcion dentro de una funcion principal)
#2 la función anidada debe usar o referenciar una variable del scope superior. osea la variable "directorio"
#3 la función superior o principal debe retornar la función anidada. 