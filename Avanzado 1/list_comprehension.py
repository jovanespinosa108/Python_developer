#FUNCION MAP()
#Crear una Lista usando map()
"""La función map retorna un objeto de tipo map que entrega el resultado 
de aplicar una función a cada uno de los elementos de la lista que 
recibe. El objeto map es un iterador. Esta función nos permite reemplazar 
lo que podemos hacer con un ciclo para aplicar una función a todos los 
elementos de una lista."""

#transforma y aplica una funcion a una lista y compara contra la funcion map()
def calcular_cuadrado(numero):
    return numero**2

lista_num = [1,2,3,4,5,6,7,8,9,10]
"""lista_cuadrado = []

for num in lista_num:
    cuadrado = calcular_cuadrado(num)
    lista_cuadrado.append(cuadrado)

print(lista_cuadrado)"""

map_cuadrado = list(map(calcular_cuadrado, lista_num))
print("Lista map ", map_cuadrado)

#en la funcion map(funcion, variable_lista) pasamos como 1er argumento la funcion y como 2do la lista donde pasara

#LIST COMPREHENSION
"""List comprehension en Python es una manera de construir listas 
u objetos iterables usando una sola línea de código. es mejor que crear 
un ciclo for para crear una lista ya que es mas simple, no dejamos de usar ciclos, 
solo los definimos de tal manera que sea corto y elegante. Se aplica una
operacion a cada elemento del objeto iterable, puede ser una lista,
un set o un diccionario"""

#sintaxis: List = [expresion(elementos) for elemento in objeto_iterable]

lista_num2 = [1,2,3,4,5,6,7,8,9,10,11,12]
lista_cuadrado2 = []

for num in lista_num2:
    cuadrado = num**2
    lista_cuadrado2.append(cuadrado)

print("Cilco for ", lista_cuadrado2)

#list_comprehension es simple, una sola linea
lista_comprehension = [num**2 for num in lista_num2]
print("List Comprehension ", lista_comprehension)

lista_comprehension = [calcular_cuadrado(num) for num in lista_num2]
print("List Comprehension con funcion", lista_comprehension)

#list comprehension nos permite aplicar condiciones a las expresiones
#para que sean o no calculadas en cada iteracion, hay 2 formas de hacerlo


#sintaxis: List = [expresion(elementos) for elemento in objeto_iterable if condition]
#sintaxis: List = [expresion(condicion) for elemento in objeto_iterable]

def es_par(numero):
    return numero % 2 == 0

lista_cuadrados_pares = [calcular_cuadrado(num) for num in lista_num2 if es_par(num)]
print("Lista Condicion 'if' pares", lista_cuadrados_pares)

lista_resultados = [calcular_cuadrado(num) if es_par(num) else 0 for num in lista_num2]
print("Lista dos condiciones", lista_resultados)

#CREAR SET O DICCIONARIOS CON LIST COMPREHENSION

lista_num_set = [2,8,4,6,3,5,2,8,3]

set_pares = {num for num in lista_num_set if num % 2 == 0}
print("Set creado con List Comprehension", set_pares)


vocales = "aeiou"

dicc_vocales = {vocal.lower(): vocal.upper() for vocal in vocales}
print("Diccionario creado con List Comprehension", dicc_vocales)

"""El operador de walrus es el nombre que recibe un operador que 
permite asignar a un valor una variable mientras se evalúa como 
expresión. Se escribe como :="""

#Operador walrus syntaxis: (variable a almacenar := funcion(parametro)) codigo para evaluar la condicion

#Walrus con "for" y condicional, itera cada numero y regresa pares e impares al cuadrado
lista_pares = []
for num in lista_num:
    if (cuadrado := calcular_cuadrado(num)) %2 == 0: #Walrus con "for" y condicional
        lista_pares.append(cuadrado)
        print(f"el cuadrado de {num} es {cuadrado}, es un numero par")
    else:
        print(f"El cuadrado de {num} es {cuadrado}, es un numero impar")

"""Imprime: El cuadrado de 1 es 1, es un numero impar
el cuadrado de 2 es 4, es un numero par
El cuadrado de 3 es 9, es un numero impar
el cuadrado de 4 es 16, es un numero par etc..."""

#operador walrus con list comprehension solo regresa numeros pares al cuadrado
pares_comprehension = [cuadrado for num in lista_num if (cuadrado := calcular_cuadrado(num)) %2 == 0]
print(pares_comprehension) #imprime [4, 16, 36, 64, 100]

"""List Comprehension no debe usarse en expresiones muy largas
ya que las hace dificil de leer, estos ejemplos son cuano 'no'
necesitamos usar List Comprehension"""

#no se usa lista para obtener un resultado en un rago muy alto
#caso 1
total = sum([num for num in range(100)])# no usar lista []
#correccion
total = sum(num for num in range(100))# solo se sum() sin lista []

#caso 2 imprimir una variable de un objeto iterable, no se debe crear una lista [] no sirve
[print(element) for element in range(1)]
#correccion: mejor usa el metodo "for" de manera convencional
for element in range(10):
    print(element)

#caso 3 evita usar ciclos anidados con list comprehension
#lista con listas de 2 elementos
lista_anidada = [[1,2], [3,4], [5,6]]

valores_lista = [numero for elemento in lista_anidada for numero in elemento]
print(valores_lista)#dificil de leer

#correccion
valores_lista = []
for elemento in lista_anidada:
    for numero in elemento:
        valores_lista.append(numero)

print(valores_lista)
"""es mejor hacerlo con 2 "for", donde valores lista le asingnamos 
el valor de una lista vacia
despues para cada elemeno in la varibale lista_anindada queremos 
que cada numero en cada elemento de lista_anidada vamos a añadir a
valores_lista el numero sobre el cual estamos iterando con .append()"""
