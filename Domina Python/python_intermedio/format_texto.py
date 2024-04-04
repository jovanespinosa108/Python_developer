#Añadir el valor de una variable en un string usando la funcion format()
numero = 5
costo_pasaje = "El pasaje cuesta: {} pesos".format(numero)
print(costo_pasaje)

#imprime: El pasaje cuesta: 5 pesos

#mas de una variable en un string, una {} por variable, se pasan las variables como argumentos
pasaje = 5
entrada = 150
costo_pasaje_entrada = "El pasaje cuesta: {} pesos y la entrada al parque es de: {} pesos".format(pasaje,entrada)
print(costo_pasaje_entrada)

#imprime: El pasaje cuesta: 5 y la entrada al parque es de: 150

#texto "f string"
texto_f_string = "F-string: {entrada}"
print(texto_f_string)
#imprime: F-string: {entrada}

#formato de doubles comillas duplicadas se usa un backslash antes de cada comilla
texto_comillas = "Pedro dijo \"Buenos dias\""
print(texto_comillas)
#imprime: Pedro dijo "Buenos dias"

#usando salto de linea se usa \n
texto_salto_linea = "Linea 1\nLinea 2"
print(texto_salto_linea)
#imprime:
#Linea 1
#Linea 2

#texto tabulador (simulando una tabla) usa \t para tabulador y \n para salto de linea
texto_tabulador = "Nombre\tApellido\nPerla\tSaavedra"
print(texto_tabulador)
#imprime:
#Nombre  Apellido
#Perla   Saavedra