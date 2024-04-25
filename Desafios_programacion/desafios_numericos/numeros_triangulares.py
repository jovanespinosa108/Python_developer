#numero triangular: resultado de la suma de numeros naturales sucesivos
#Pueden representarse en conjuntos de puntos que forman un triangulo equilatero
#se obtiene
#crea una funcion que reciba el numero de la fila del triangulo de puntos
#la funcion calculara el numero triangular correspondiente a la fila
"""el primer punto se representa con un 1 esta es la 1ra fila
en la segunda fila se representas 2 numero2 1
la tercera fila se representan 3 numeros 1
cada fila siguente contiene la cantidad de puntos
del siguiente numero natural
1  un punto
11 dos puntos
111 tres puntos"""

def numero_triangular(fila):

    triangulo = 0  #suma la cantidad de puntos por fila

    for i in range(1, fila +1): #itera en un rango de 1 al numero de la fila mas 1
        triangulo += i  #suma el numero iterado al valor acomulado en la variable
    return triangulo  #resultado de calcular el numero en la variable a partir de la fila del triangulo

print(numero_triangular(3)) #6
print(numero_triangular(5)) #15
print(numero_triangular(7)) #28
        