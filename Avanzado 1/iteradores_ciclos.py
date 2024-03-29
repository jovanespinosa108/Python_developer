"""Objetos iterables son un conjunto de elementos que permiten retornar 
los elementons que los componen y se pueden recorrer usando ciclos como 
las las cadenas de texto (strings), listas, tuplas y diccionarios
Los iteradores son Objetos, estos nos permiten recorrer un objeto iterable, 
en python tenemos 2 funciones nativas que nos permiten crear iteradores 
y trabajar con elementos iterables sin usar ciclos. 
La funcion iter() permite recorrer el objeto iterable y 
la funcion next() retorna el elemento siguente en el iterable."""

#crear una lista para usar iter() y next()

iterador_numeros = [1,2,3,4]

iterador = iter(iterador_numeros)

print(next(iterador), next(iterador), next(iterador))
print(next(iterador)) #cada vez que imprimions la funcion next() imprimira un elemento de la lista
# imprime 1 2 3
#4 
#ya se son 4 elementos en la lista y el 4 lo imprime aparte por estar en un print separado de los demas
#No es comun usar las funciones iter() por si mismos sino en conjunto con zip(), map() o filter()

#CICLOS FOR
"""Los ciclos for nos permiter iterar un objeto sin necesidad de un 
indice que indique la posicion de cada elemento, los elemento for 
en otros lenguajes tienen la palabra "for" y entre parentesis 
el inicializador, la condicion y el iterador"""

#Ejemplo en JS
"""let nombres = ["Ernesto", "Julio", "Amanda"]
   for(let i = 0; i < nombres.length; i += 1){ 
      console.log(nombres[i])
   }"""

#en python llamamos la sentencia for y el nombre del elemento sobre el cual vamos a iterar y el objeto iterable

nombres = ["Ernesto", "Julio", "Amanda"]
for elemento in nombres:
    print(elemento)


#SENTENCIAS BREAK & CONTINUE
#Break and continue se usan para evaluar una condicion y 
#parar el ciclo o pasar a iter el siguiente elemento
    
nombres_bk = ["Sandra", "Ernesto", "Julio", "Amanda"]

for elemento_bk in nombres_bk:
    if "Ernesto" in elemento_bk:
        break
    print(elemento_bk) 
#imprime solo "Sandra" ya que el ciclo se cumple en Ernesto y hace el break

nombres_conti = ["Sandra", "Ernesto", "Julio", "Amanda"]

for elemento_conti in nombres_conti:
    if "Ernesto" in elemento_conti:
        continue
    print(elemento_conti)
# imprime Sandra, Julio, Amanda y solo salta "Ernesto" y continua
    
nombres_noif = ["Sandra", "Ernesto", "Julio", "Amanda"]

for elemento_noif in nombres_noif:
    print(elemento_noif)
    continue
#imprime todos los elementos


#FUNCION RANGE()
"""La función range() crea una serie de números consecutivos por defecto 
iniciando en 0 y terminando un número antes del argumento que se le 
entrega a la función. Cada numbero de la serie se incrementa en 1: 
sintaxis  range(inicio, fin, paso)"""

serie_1 = range(5) #solo con argumento "fin" ya que inicio por default es 0
print(list(serie_1))
#imprime lista [0, 1, 2, 3, 4] por default 0 siempre es el primer elemeto

serie_2 = range(5, 10) #con argumento inicio y fin
print(list(serie_2))
#imprime lista [5, 6, 7, 8, 9] 

serie_2 = range(3, 10, 3) #con argumento inicio, fin, paso
print(list(serie_2))
#imprime lista [3, 6, 9] empieza a iterar desde el 3 y Pasa hasta el 3 numero

#FUNCION ZIP()
#la funcion zip() une uno o mas elemento iterables y esto resulta en un a tupla

nombres = ["Maria", "Ana", "Alejandra"]
apellidos = ["Cornejo", "Vazquez", "Pedregal"]

nombre_completo = list(zip(nombres, apellidos))
print(nombre_completo)
#imprime una lista de tuplas: [('Maria', 'Cornejo'), ('Ana', 'Vazquez'), ('Alejandra', 'Pedregal')]
#cada tupla usa el index correspondiente en cada lista iterada osea index 0 con 0, 1 con 1, 2 con 2 etc.

#para unzip debemos crear 2 varibles para alamcenar las 2 listas
#en el zip() se usa un * y la variable que se va a unzip
nombres_unzip, apellidos_unzip = zip(*nombre_completo)
print(nombres_unzip)
print(apellidos_unzip)
#imprime listas ('Maria', 'Ana', 'Alejandra') y ('Cornejo', 'Vazquez', 'Pedregal')

#si se necesita iterar con 2 elements al mismo tiempo se puede usar "for"
for nombre, apellido in zip(nombres, apellidos):
    print(nombre, apellido)

#imprime Maria Cornejo, Ana Vazquez, Alejandra Pedregal
"""La función enumerate recibe un objeto iterable y retorna tuplas en 
las que cada una contiene un elemento del objeto que recibe. 
y un índice que indica su posición. Por defecto, 
la función enumerate retorna el índice iniciando en 0, 
aunque podemos cambiar este índice desde el cual iniciará la cuenta
Sintaxis: enumerate(iterable, start = 0) con 2 argumentos, el objeto 
y iterable y donde empezara a asingar el numero de index"""

nombres2 = ["Pedro", "Santiago", "Juan", "Jose"]
nombres_enumerados = enumerate(nombres2, start = 4)
print(list(nombres_enumerados))
#imprimira: [(4, 'Pedro'), (5, 'Santiago'), (6, 'Juan'), (7, 'Jose')]
#añadiendo al principio de cada tupla el index asignado en el argumento "start"

nombres3 = ["Amanda","Pedro", "Kenia", "Santiago", "Juan", "Ignacio"]
nombres_enumerados = enumerate(nombres3, start = 4)

for indice, elemento_enumerado in enumerate(nombres3):
    print(indice, elemento_enumerado)

#imprime: cada elemento por separado con su index respectivo
#0 Amanda
#1 Pedro
#2 Kenia
#3 Santiago
#4 Juan
#5 Ignacio
    
#SENTENCIA "ELSE" Y CICLO "FOR"
    
nombres4 = ["Ana","Pedro", "Kenia", "Julio", "Ignacio"]

for nombres_else in nombres4:
    print(nombres_else)
else:
    print("Ciclo terminado")
#imprime
#Ana
#Pedro
#Kenia
#Julio
#Ignacio
#Ciclo terminado


for nombres_else in nombres4:
    print(nombres_else)
    if nombres_else == "Kenia":
        break
else:
    print("Ciclo terminado")

#imprime
#Ana
#Pedro
#Kenia