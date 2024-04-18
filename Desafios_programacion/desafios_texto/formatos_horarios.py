#convierte un string de formato 12 horas a formato 24 hrs
#crea funcion reciba str en formato 12hrs horas:minutos AM/PM
#retorna un string con la hora en el formato 24hrs
#formato posicion[0]hora, posicion[1]miuntos, posicion[2]segundos, posicion[3]"am"/"pm"
#4:25:40pm o 4:25pm

def convertir_horario(hora): #recibe la hora en formato 12hrs como string o texto

    hora_lista = hora.split(":") #divide las horas de los minutos tomando como referencia el signo ":"
    if hora[-2:].lower() == "pm": #identifica si el formato es "pm" al bucar los ultimos 2 caracteres en el texto 
        if hora_lista[0] != "12": #verifica si la posicion "0" no sea igual a "12"
            hora_lista[0] = str(int(hora_lista[0])+ 12) #entonces si no es igual a 12 le suma 12 a la posicion "0"
    else: #de otro modo
        if hora_lista[0] == "12": #si la posicion "0" en hora lista es igual a 12
            hora_lista[0] = "00" #entonces convierte el valor de la posicion "0" a "00"
    hora_convertida = ":".join(hora_lista) #une las partes de la hora en la variable hora lista
    return hora_convertida[:-2] #regresa la hora con excepcion de los 2 ultimos caracteres para que no regrese am o pm

print(convertir_horario("2:30am")) #2:30
print(convertir_horario("10:30PM")) #22:30
print(convertir_horario("7:22pm")) #19:22


#Crea una funcion donde se guardara la hora en formato 12 hrs, osea tendra pm o am
#crea una variable donde se guardara el texto de la funcion y lo dividira cuando encuentre ":"
#eso se hace con la funcion split() llamando al parametro que tenga la funcion
#verifica si el texo del parametro "hora", sus ultimos 2 caracteres convertida a minusculas son iguales a "pm"
#si el texto en hora_lista, en la posicion "0" no es igual a "12"
#entonces al texo en hora en la posicion "0", conviertelo en integral y sumale 12 unidades, despues conviertelo en str otravez
#de otro modo si la pocision "0" en la hora lista es igual a "12"
#convierte el valor de la posicion "0" a "00"
#Crea otra varialbe para el texto convertido "hora_convertida"
#y une los textos cuando encuentres el caracter ":" detro de la variable hora_lista
#regresa el texto procesado que se almaceno el la ultima variable con excepcion de los ultimos 2 caracteres
#esto es para evitar imprimir "am" y "pm"
