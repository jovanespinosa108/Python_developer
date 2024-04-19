#crea una funcion que revise un string que solo contiene parentesis
#la funcion determinara si los parentesis estan balanceados o no lo estan
#parentesis balancedo tiene parentesis de apertura y cierre ()
#parentesis desbalanceados tiene parentesis incompletos ())
#retornara True para balanceados y False para desbalanceados

def parentesis_balanceados(texto): #funcion que guarda el texto

    apertura = 0  #variable que da valor 0 para balancear
    for parentesis in texto: #ciclo for para comparar parentesis
        if parentesis == "(": # si tiene un parentesis de apertura
            apertura += 1       #entonces suma 1 a la variable apertura
        elif parentesis == ")": #si tiene un parentesis de cierre
            apertura -= 1   #entonces resta 1 a la varible, asi la variable queda en 0
            if apertura < 0: #si la variable apertura tiene un valor menor a 0
                return False  #entonces regresa False
    return apertura == 0 #retorna True si la variable apertura es igual a 0
        
print(parentesis_balanceados("())"))
print(parentesis_balanceados("(()) () (())"))
print(parentesis_balanceados(")) () (()"))

