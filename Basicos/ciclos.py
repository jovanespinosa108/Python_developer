#iterar las letras de un texto
#iterar el string "texto"

for letra in "Texto":
    print(letra)

#iterar en una lista "[]"

lenguajes = ["python", "Java", "C++", "JavaScript"]
for elemento in lenguajes:
    print(elemento)

#iterar en una lista "[]" con Break and "if"
#la iteracion para al encontrar el elemento y no imprime mas

autos = ["sedan", "pick-up truck", "SUV", "VAN"]
for tipo in autos:
    print(tipo)
    if tipo == "SUV":
        break

#iterar en una lista "[]" con Continue and "if"
#la iteracion al encontrar el elemento no lo imprime y continua imprimendo el resto
#print debe ir al final del codigo
autos = ["sedan", "pick-up truck", "SUV", "VAN"]
for tipo in autos:
    if tipo == "SUV":
        continue
    print(tipo)

#iterar el rango de numeros
#imprimira 7 elementos pero siempre empieza desde "0"
#imprime del 0-6
for elemento in range(7):
    print(elemento)

#iterar lista con "while"
#se cumple una o mas instucciones mientras se cumple el ciclo
#se usa un contador "i" para saber hasta cuando se repite el ciclo
i = 1
while i <= 5:
    print(i)
    i += 1
    #el contador paro en elemnto 5 aunque tenia el incrementador
    #el elemento 6 ya no cumplia con la condicion i <= 5

i = 1
while i <= 4:
    print(i)
    i += 1
    if i == 3:
        break

#el ciclo "while" debe tener una instruccion para detenerse sino se ejecutara infinitamente.
#si no se aumenta el contador "i" osea i += 1 el contador siempre imprimira 1 como valor asignado


#iterar un lista con "index"

lenguajes = ["python", "Java", "C++", "JavaScript"]

for index in range(len(lenguajes)): #indice in el rango length de la varible lenguajes
    print("indice", index) #imprime el string "indice" con el valor de index
    print("elemento", lenguajes[index]) #imprime el string "elemento" con el valor de lenguages dentro de la lista en base al valor index

#iterar lista con "while"

lenguajes = ["python", "Java", "C++", "JavaScript"]

i = 0
while i < len(lenguajes):
    print(lenguajes[i])
    i += 1

# el inclementador "i" empieza en "0" ya que es el primer index
#mientras "i" sea menor en el length de la variable "lenguajes"
#imprime lenguajes basado en el incrementador dentro de la lista
#se incrementa a 1 "i" para parar el ciclo


#iterar en un diccionario {llave + valor} con "for"
lenguaje = {
    "nombre": "Python",
    "creador": "Guido Van Rossum"
}

for llave in lenguaje:
    print("llave:", llave)
    print("valor:", lenguaje[llave])

#3 funciones para iterar sobre un diccionario: keys(), values(), items().
#keys retorna una lista con los nombres de las llaves del diccionario
lenguaje = {
    "nombre": "Python",
    "creador": "Guido Van Rossum"
}

for element in lenguaje.keys():
    print(element)

for element in lenguaje.values():
    print(element)

for llaves, valor in lenguaje.items():
    print(llaves, valor)

#este regresa una tupla o "tuple" en lugar de valores separados
for element in lenguaje.items():
    print(element)