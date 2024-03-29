#Vamos a crear un decorador que se encargue de contar e imprimir 
#el tiempo que se demora una función en ejecutarse.
import time

def medir_tiempo_ejecucion(funcion):

    def wrapper():
        inicio = time.time()
        funcion()
        final = time.time()
        tiempo_final = final - inicio
        print(f"Tiempo total de ejecucion: {tiempo_final}")
    return wrapper

@medir_tiempo_ejecucion
def recorrer_ciclo(): 
    for i in range(5):
        print(i)
        time.sleep(1)

recorrer_ciclo()


def medir_tiempo_ejecucion_parametro(funcion2):

    def wrapper2(*arg, **kwargs):
        inicio = time.time()
        funcion2(*arg, **kwargs)
        final = time.time()
        tiempo_final_2 = final - inicio
        print(f"Tiempo total de ejecucion: {tiempo_final_2}")
    return wrapper2

@medir_tiempo_ejecucion_parametro
def recorrer_ciclo2(rango): 
    for i in range(rango):
        print(i)
        time.sleep(1)

recorrer_ciclo2(rango=7)

"""Cuando las funciones tienen parametros estos de deben declarar en 
la funcion wrapper y en la funcion dentro de wrapper, pero si tenemos 
multiples funciones con distintos parametros no es aconsejable poner 
todos los paramentros dentro de estas funciones para eso utilizamos 
*arg y **kwargs en ambos, remplazando todos los parametros. 
Con el uso de los parámetros args, kwargs garantizamos que cualquier 
función pueda usar el decorador tenga o no parámetros."""
