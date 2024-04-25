#crea una funcion que identifique si un numero positivo es primo
#si es primo return True
#si no es primo return False
#Numero primo: es un numero mayor a 1, divisible entre 1 y por el mismo numero

def numero_primo(numero):

    if numero <= 1: # el 1 no es primo
        return False
    
    for i in range(2, numero): #itera en un rango del 2 al numero
        if numero % i == 0: #si el residuo del numero que se itera es igual a 0 es falso
            return False
    return True   #cualquier numero mayor a 1 divisible enre si mismo es Verdadero
            
print(numero_primo(22)) #False
print(numero_primo(13)) #True
print(numero_primo(18)) #False
