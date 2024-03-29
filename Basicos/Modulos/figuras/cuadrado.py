#se importa desde la terminal llamando al modulo datetime
#import datetime
#se llama el modulo datetime y el submodulo datetime con el now()
#hora_actual = datetime.datetime.now()
#print(hora_actual)

#se puede importas con un alias
#import datetime as dt
#hora_actual = dt.datetime.now()

#se puede importar desde el submodulo sin llamar al modulo pricipal
#from datetime import datetime
#y solo se llama al submodulo con now()
#hora_actual = datetime.now()
#print(hora_actual)

#MODULOS 
#Contienen funciones o clases, separan y organizan el codigo

#modulo area_cuadrado
def area_cuadrado(lado):
    return lado * lado

#modulo perimetro_cuadrado
def perimentro_cuadrado(lado):
    return lado * 4

#vamos a exportar los dos modulos a main.py
