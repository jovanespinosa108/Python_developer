#Ciclos -> Iterar objetos (for, while)
#Ciclos dentro de ciclos -> ciclos anidados
#Funcion zip() retorna un conjunto de tuplas

lista_nombres = ["Mayra", "Juan", "Angel", "Lupe"]
lista_edad = [25,43,98,21]

datos_zip = zip(lista_nombres, lista_edad)
print(list(datos_zip))

#[('Mayra', 25), ('Juan', 43), ('Angel', 98), ('Lupe', 21)]

#iterando sobre 2 valores para 2 listas creadas con ciclo for
for nombre, edad in zip(lista_nombres, lista_edad):
    print(nombre, edad)
#esto imprime una linea por cada tupla que genera la funcion zip()
#Mayra 25
#Juan 43
#Angel 98
#Lupe 21