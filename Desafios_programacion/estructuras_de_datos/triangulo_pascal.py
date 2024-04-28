#crea una funcion que reciba el numero de filas necesarias para crear el triangulo de pascal
#retornara lista anidada 
#cada elemento sera la lista que corresponde a cada fila del triangulo
#triangulo de Pascal: coeficientes binomiales ordenados en forma de triangulo
#cada fila se forma de la suma de los numeros a la derecha e izquireda de la fila superior

def triangulo_pascal(numero_filas):

    triangulo = []
    for nueva_fila in range(numero_filas): #crea filas del triangulo
        fila = [] #almacena los valores de cada fila del triangulo
        for posicion in range(nueva_fila +1): #calcula cada valor de la fila
            if posicion == 0 or posicion == nueva_fila: #agrega los valores de los lados del triangulo a las filas
                fila.append(1) #si la condicion se cumple agrega a la fila un "1"
            else: #almacena los valores de la suma de las fila de arriba a la izq y derecha
                valor = triangulo[nueva_fila-1][posicion-1] + triangulo[nueva_fila-1][posicion]
                fila.append(valor) #agrega a la fila el valor calculado
        triangulo.append(fila) #agrego a la variable "triangula" la fila modificada
    return triangulo

print(triangulo_pascal(4))
#[[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]]
