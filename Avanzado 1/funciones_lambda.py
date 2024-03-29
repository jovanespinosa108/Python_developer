"""Se recomienda no usar las funciones lambda por que pueden ser 
dificiles de leer, sin embrago se usan normalmente para hacer filtros 
con ayuda de la función filter o para aplicar a una función a los 
elementos de una lista usando la función map"""
#en terminal cmd
#lambda num: num*2
#_(2)

#dentro de parentesis
(lambda num1: num1*2)(2)

#almacenada en una variable
multi = lambda num2: num2*3
multi(6)

#usando "filter()" y convirtiendose en lista con list()
lista_numeros = [1,2,3,4,5,6,7,8,9,10,11]

lista_pares = list(filter(lambda numero: numero %2==0, lista_numeros))
print(lista_pares) #imprime [2, 4, 6, 8, 10]

#se crea la variable lista_numero
#se crea variable lista_pares y se asigna funcion list()
#dentro de esta se usa la funcion filter()
#dentro de filter se declara la como primer argumento la funcion lambda numero %2==0, 
#y como segundo argumento la variable que queremos filtar en este caso lista_numeros


"""tambien se puede usar la funcion map(), pasando 2 argumentos, 
el primero pude ser una funcion lambda o tambien una funcion normal
y el segundo un objeto iterable"""

nueva_lista = list(map(lambda numero: numero*10, lista_numeros))
print(nueva_lista) #[10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]

"""En este caso creamos la varaible nueva_lista, 
pasamos las funciones list() y map(), pasamos como argumento dentro de map
la funcino lamda y despues pasamos la variable lista_numeros
e imprimios la varible creada nueva_lista """