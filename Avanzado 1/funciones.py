APELLIDO = "Pinto" #variable global

def funcion():
    print("bien hecho")
    nombre = "Ana"  #variable local
    print(nombre, APELLIDO) # se usa print para regresar el valor de la variable
funcion()           #variable global sepuede llamar dentro de las funciones

print(APELLIDO) #se puede llamar fuera de las funciones

#Parametros en una funcion son los valores que la funcion recibe dentro de los parentesis
#crea una funcion que calcule el perimetro de un cuadrado

def perimetro_cuadrado(lado, unidades): #parametros "lado" y "unidades"
    perimetro = lado * 4 # se crea la variable con los variables del primer parametro
    print(f"El permetro es {perimetro} {unidades}") #formato de la variable y el segundo parametro 

perimetro_cuadrado(35, "metros") #se invoca la funcion con los valores de los parametros
perimetro_cuadrado(lado=35, unidades="metros") # tambien se invoca la funcion por el nombre del parametro y su valor o "argumento"

#lado (es el parametro) 35 (es el argumento)
#unidades(es el parametro) "metros" (es el argumento)

#para usar el resultado de nuestra funcion en el proceso principal se usa la instruccion "return"

def perimtro_cuadrado(lado):
    perimtro = lado * 4 #se crea una varible local y se le asigna el parametro y un valor
    return perimtro #se regresa la varible creada

def area_cuadrado(lado):
    area = lado * lado
    return area

#se le asigna a las variables la funcion con su parametro y el valor a ejecutar
perimtro = perimtro_cuadrado(lado=8) 
area = area_cuadrado(lado=8)
#se imprime usando las variables creadas en formato
print(f"Area: {area}, Perimetro: {perimtro}")

#una manera de tener 2 variables en el mismo return y con la misma funcion
def resultado_cuadrado(lado):
    perimetro2 = lado *4
    area2 = lado * lado
    return perimetro2, area2

area2, perimetro2 = resultado_cuadrado(lado=5)
print(f"Area: {area}, Perimetro: {perimtro}")

#regresa Area: 25, Perimetro: 20

#si almacenamos "resultado_cuadrado"en una sola variable
#area2 = perimetro_cuadrado(lado=5)
#regresa una tupla: (25,20)

#Documentacion en Pyton
#documentacion corta """ el titulo de la funcion o para que sirve """ entre 3 comillas
"""documentation larga contiene la informacion de todos los paramentros de la funcion 
y de los retornos entre 3 comillas
#la descripcion contine: titulo, descripcion: que hace la funcion, 
descripcion de los parametros como Args: 
y la descripcion de los returs como Returs, ambos declarando para que funcionan
y su tipo de dato, en este caso (int)"""

def perimetro_cuadrado3(lado):
    """Calcular el perimentro de un cuadrado
    
    Esta funcion recibe el valor de un lado de un cuadrado 
    y apartir de este calcula y retorna su perimetro.

    Args: 
        lado (int): medida del lado del cuadrado
    Returns:
        perimetro (int): perimetro del cuadrado
    """

    perimetro3 = lado * 4
    return perimetro3
perimetro_cuadrado3(lado=5)

def mensaje(men):
    y = ""
    for x in men:
        y = y + x
        print(y)

mensaje("Hola")


def calcular_area_cuadrado(lado): #lado es el parametro
    """Calcular el area de un cuadrado""" #este es un docstring
    area = (lado * lado)
    return area

area_cuadrado = calcular_area_cuadrado(lado=20) #lado es el parametro y 20 el argumento
print(area_cuadrado) #resultado =400, 


#parametros args permiten pasar a la funcion muliples datos en una tupla
#se identifican los args cuando vemos un * seguido de un parametro

#este es un ejemplo sin args
def cuadrilatero_perimetro1(lado1, lado2, lado3, lado4):
    perimetro_cuadri1 = lado1+lado2+lado3+lado4
    return perimetro_cuadri1

perimetro_cuadri1 = cuadrilatero_perimetro1(1,2,3,4)
print(perimetro_cuadri1) #resultado =10

#este es un ejempo con *args
def cuadrilatero_perimetro(*args):
    print(args)
    perimetro_cuadri = 0
    for lado in args:
        perimetro_cuadri += lado
    return perimetro_cuadri

perimetro_cuadri = cuadrilatero_perimetro(1,2,3,4)
print(perimetro_cuadri) #resultado =10


#Parametros kwargs permiten enviar datos no declarados a la funcion 
#en forma de diccionario osea llave y valor {key: value, key: value}
def funcion_kwargs(**kwargs):
    print(kwargs)# imprime: {'nombre': 'Alberto', 'apellido': 'Jimenez'}
    for llave, valor in kwargs.items():
        print(f"llave: {llave}, valor: {valor}")# imprime: llave: nombre, valor: Alberto, llave: apellido, valor: Jimenez
    print(kwargs["nombre"], kwargs["apellido"]) # imprime: Alberto Jimenez

funcion_kwargs(nombre= "Alberto", apellido= "Jimenez")#varible donde se pasan los valores de paramentro y argumento

"""Los parámetros que nos permiten enviar datos definidos desde la función o parámetros especiales, 
como los args que enviamos porque no tenemos conocimiento sobre la cantidad de datos que se requieren procesar, 
o los kwargs, cuando queremos definir nuevos parámetros que no están definidos dentro de la función.
Para hacer uso de estos 3 parametros dentro de una funcion debe hacerse en orden
Primero: parametros definidos desde la funcion
Segundo: args
Tercero: kwargs
ejemplo correcto:
def orden_correcto(nombre, apellido, *args, **kwargs):
    pass
    
ejemplo incorrecto regresara error: invalid syntax
def def orden_incorrecto(nombre, apellido, **kwargs, *args)
    pass
"""