#crea una funcion que reciba una lista anidada de 2 dimensiones
#regresara una nueva lista de una sola dimension
#contendra todos los elementos de la lista exteriory la lista anidada
#deben tener el mismo orden

def flatten_list(lista):

    new_list = []  #guardara los elementos de la lista
    for element in lista: #itera cada elemento en la lista argumento de la funcion
        if type(element) is list: #revisa que el tipo de elemento en la lista, sea tipo "list" 
            new_list.extend(element) #si el elemento es un tipo "list" agrega los elementos separados en "new_list"
        else:
            new_list.append(element) #si el elemento iterado no es lista, lo agrega a "new_list" sin cambios
    return new_list #retorna "new_list" con los nuevos datos

print(flatten_list([3,5,7,["Jose", "Xochitl", "Victor"]])) #lista de 2 dimensiones
#[3, 5, 7, 'Jose', 'Xochitl', 'Victor']
print(flatten_list([5,9,7,["gonzalez",["Pedro", "julian", "Cristian"]]])) #lista de 3 dimensiones
#[5, 9, 7, 'gonzalez', ['Pedro', 'julian', 'Cristian']] regreso lista de 2 dimensiones
