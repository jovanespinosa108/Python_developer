#RUTAS DE ARCHIVO
#Hay 2 tipos de rutas, relativas o absolutas, 
#las relativas son relativas a la ubicacion del archivo
#las absolutas contienen la ruta donde se esta achivando toda la carpeta
#C:\Users\jovan\Python\Desarrollador Python>, si alguna carpeta tuviera un numero al principio
#entonces debemos poner doble \\ al principio de cada carpeta para que python lo pueda leer
#ejemplo: 'C:\\Users\\jovan\\Python\\Desarrollador Python\\05_cvs_files>
#para usar rutas absolutas en otras computadoras debemos usar la libreria OS (operative system)
#esto evita generar un error si estamos usando otra compu"""

import csv
import os

ruta = "csv_vacio.csv"
ruta_absoluta = "C:\\Users\\jovan\\Python\\Desarrollador Python\\csv_vacio.csv" 
ruta_absoluta_os = os.path.join(os.getcwd(), "csv_vacio.csv")

print(ruta_absoluta)
print(ruta_absoluta_os)