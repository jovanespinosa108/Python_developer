lista_append = [1,2,3]
lista_extend = [4,5,6]
lista_insert = [7,8,9]

lista_concatenar = ["a","b","c"]

#concatena el elemento en la ultima posicion
lista_append.append(lista_concatenar)
print(lista_append)

#concatena extendiendo los elementos de la lista
lista_extend.extend(lista_concatenar)
print(lista_extend)

#concatena insertado los elementos en la posicion index deseada
#la funcion insert() pasa 2 argumentos: index number y variable
lista_insert.insert(1, lista_concatenar)
print(lista_insert)

#[1, 2, 3, ['a', 'b', 'c']]
#[4, 5, 6, 'a', 'b', 'c']
#[7, ['a', 'b', 'c'], 8, 9]
