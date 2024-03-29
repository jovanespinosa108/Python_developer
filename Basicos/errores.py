#crear una funcion donde el length de la lista sea mayor a 0,
#si es menor a 0 entonces imprimira el error con un string explicando el error

#assertion error (descomenta para correr el codigo)
"""def calcular_promedio1(lista):
    assert len(lista) > 0, "La lista esta vacia"
    return sum(lista) /len(lista)

promedio1 = calcular_promedio1(lista=[]) #la lista esta vacia
print(promedio1)"""

#crear funcion donde valide que x es mayor a 1, 
#si es menor a 1 debe imprimir el error mediante "raise Exception"

#exception error with "raise" (descomenta para correr el codigo)
"""def validar_x(x):
    if x < 1:
        raise Exception("La variable 'x' debe ser mayor a 1")
    else:
        print("'x' es mayor a 1")

x = 0.3  #x es menor a 1
validar_x(x)"""


#calcular como funciona "try-except" con una funcion que 
#calcula el promedio a partir de los valores de una lista
#
def calcular_promedio2(lista):
    assert len(lista) > 0, "la lista esta vacia" 
    return sum(lista) / len(lista)

try:
    promedio = calcular_promedio2(lista=["texto"])
    print(promedio)
except AssertionError as assert_error:
    print(assert_error)
except Exception as e:
    print("La funcion no calculo el promedio")
    print(e)


