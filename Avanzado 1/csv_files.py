"""CSV es acronimo de Comma Separated Values y nos permite guardar datos
de manera sencilla, y se guarda con la extencion .csv, los datos en estos
archivos representan tablas, donde cada valor separado por una coma
pertenece a una columna y cada linea del archivo es una fila"""

#crear unarchivo csv con python, usa 2 funciones:
#"csv.writter" nos permite escribir datos sobre un archivo csv
#"open" que nos permite abrir y mantener un archivo abierto ya sea existente o creadi en el momento

#importa la libreria csv que no se debe descargar ya que es nativa de python
import csv
import os

#crea una variable que sera la ruta de ubicacion del archivo en la maquina ya sea absoluta o relativa

#esta es una ruta relativa: osea el csv guardado/creado estara al mismo nivel 
#y en la misma carpeta del archivo de python que estamos trabajando
ruta = "csv_vacio.csv"

#crea una nueva varible con la funcion open para abrir el archivo con 2 argumentos
#primer argumento: la variable ruta y segundo argumento: modo de apertura "w" de writte
archivo_abierto = open(ruta, "w")

#crea variable con funcion writer.csv y pasa como argumento la variable del achivo abierto
#y como 2do argumento (opcional) delimiter= "," que separa las columnas
writer = csv.writer(archivo_abierto, delimiter=",")

#despues cierra el archivo abierto
archivo_abierto.close()

#Esto creara un archivo tipo csv aparecera asi: "cvs_vacio.cvs"


#Escritura de ARCHIVO CSV
#escribir en archivo usando funciones open(), close() y csv.writer(parametro1, paramentro2)
 
archivo1 = open("datos.csv", "w")
writer1 = csv.writer(archivo1, delimiter=",")
archivo1.close()

#import csv   Este ya esta importado arriba

columnas = ["nombre", "apellido", "edad"]
dato = ['Peter', 'Faust', 48]

datos_lista = [
    ["Peter", "Faust", 48],
    ["James", "White", 25],
    ["Mary", "Smith", 78]
]

datos_dict = [
    {"nombre": "Cristina", "apellido": "Sanchez", "edad": 32},
    {"nombre": "Julia", "apellido": "Fernandez", "edad": 41},
    {"nombre": "Javier", "apellido": "Mina", "edad": 19}
]

#Tambien se puede escribir con la sentecia "with" con variable "columnas"
with open("datos.csv", "w", newline="") as archivo2:
    writer = csv.writer(archivo2, delimiter=",")
    writer.writerow(columnas)
    writer.writerow(dato)
    writer.writerows(datos_lista)

#Se puede escribir con "with" y la variable "datos_lista"
with open("datos.csv", "w", newline="") as archivo3:
    writer2 = csv.DictWriter(archivo3, fieldnames=columnas)
    writer2.writeheader()
    writer2.writerows(datos_dict)

#LECTURA DE ARCHIVOS CSV
#1-se importa la libreria csv, se usa "with" y la funcion open()
#como argumentos de open() se pasa la carpeta con los datos a leer, 
#la "r" de read, el encoding="UTF-8" y se asigna un alias para manejar ese archivo
#with open("datos.csv", "r", encoding="UTF") as archivo_read
#2-despues se crea la variable para usar el metodo csv.reader() 
#y como argumento pasamos el alias del archivo creado anteriormente
#  reader = csv.reader(archivo_read)
#3- Se usa el ciclo "for" asignando una variable donde se pasara 
#la variable del metodo reader y se imprime esa ultima variable
#   for fila in reader:
#       print(fila) 
# la funcion "next()" antes del ciclo for nos ayudara a no leer 
#la fila de los titulos de las columnas y pasamos la variable reader como argumento
#import csv
    
with open("datos.csv", "r", encoding="UTF") as archivo_read:
    reader = csv.reader(archivo_read)
    nombres_columna = next(reader)
    print("Columnas", nombres_columna) #nos ayuda a imprir el nombre de las columnas con el titulo "Columnas"
    for fila in reader:
        print(fila)

#si queremos correr el codigo como diccionario debemos 
#cambiar el metodo "csv.reader" por "csv.DictReader"
#y eliminar la variable nombres_columnas con su print
#en print fila podemos iterar por elemento al pasar si index
#por ejem: si queremos imprimir los nombres imprimimos print(fila[0]) index 0
#por ejem: si queremos imprimir los apellidos imprimimos print(fila[1]) index 1
