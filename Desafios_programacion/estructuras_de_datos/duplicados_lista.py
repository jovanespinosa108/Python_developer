#crea una funcion que identifique elementos duplicados en una lista
#la funcion recibe una lista
#solo retorna los elementos duplicados
#si no existen elementos repetidos regresara una lista vacia

def encontrar_duplicados(lista):

    lista_elementos = [] #guarda los elementos no repetidos
    duplicados = [] #guarda elementos duplicados

    for elemento in lista: #ciclo for itera cada elementos en la lista
        if elemento in lista_elementos: #si el elemento iterado ya se encuentra en lista_elementos
            duplicados.append(elemento) # entonces agrega estos elementos a la lista duplicados
        else: #de otro modo
            lista_elementos.append(elemento) #si el elemento no esta repetido lo guarda en lista_elementos
    return duplicados

print(encontrar_duplicados(["juan", 2, "carro", "perro", 2, "silla", "juan"]))
#[2,"juan"]
