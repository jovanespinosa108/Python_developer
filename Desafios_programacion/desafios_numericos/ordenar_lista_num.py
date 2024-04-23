#Las listas guardan elementos en forma ordenada 
#osea los mantiene en el orden que fueron añadidos
#en ocasiones los datos se deben guardar en orden alfabetico o de menor a mayor
#Ordernar una lista de numeros enteros de menor a mayor
#usa el algoritmo "ordenamiento burbuja"
#ordenamiento burbuja es: revisar cada elemento en la lista y compararlo con el siguiente
#los elementos cambiaran su posicion si estan en orden incorrecto
#revisar la lista las veces necesarias hasta que los elementos esten en el orden correcto

numeros_enteros = [2,8,6,7,9,1,4,3,5]

numeros_enteros.sort()

print(numeros_enteros)

#usando el algoritmo ordenamiento burbuja

def ordenamiento_burbuja(lista):

    for i in range(len(lista)): #ciclo for itera sobre los elementos de la lista "i"
        for j in range(0, len(lista)-i-1): #itera el length de la lista empezando dese 0 hasta el final de la lista restando una unidad de la lista-i -1
            if lista[j] > lista[j+1]: #valora si el contenido en lista j es mayor a j + la unidad sumada
                print(lista[j])
                temporal = lista[j] #guarda los elementos añadidos en j en la variable "temporal"
                print(lista[j])
                lista[j] = lista[j+1] #actualiza lista j con lo obtenido en j + 1
                print(lista[j])
                lista[j+1] = temporal #asigna lo guardado en lista j+1 en variable temporal
                print(lista[j]) 
    return lista
    

print(ordenamiento_burbuja([2,8,6,7,9,1,4,3,5]))

#en el ciclo for se usa range() para que itere sobre el length de una lista en un rango

