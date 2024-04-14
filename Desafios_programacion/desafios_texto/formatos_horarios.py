#convierte un string de formato 12 horas a formato 24 hrs
#crea funcion reciba str en formato 12hrs horas:minutos AM/PM
#retorna un string con la hora en el formato 24hrs
def convertir_horario(hora):

    hora_lista = hora.split(":") #divide las horas de los minutos
    if hora[-2:].lower() == "pm": #convierte en minusculas si son "pm" 
        if hora_lista[0] != "12":
            hora_lista[0] = str(int(hora_lista[0])+ 12) #si no es igual a 12 le agrega 12 caracteres
    else:
        if hora_lista[0] == "12": 
            hora_lista[0] = "00" #si es igual a 12 lo convierte a "00"
    hora_convertida = ":".join(hora_lista) #junta hora lista con hora convertida
    return hora_convertida[:-2] #regresa la hora con excepcion de los 2 ultimos caracteres

print(convertir_horario("2:30am")) #2:30
print(convertir_horario("10:30PM")) #22:30
print(convertir_horario("7:22pm")) #19:22







