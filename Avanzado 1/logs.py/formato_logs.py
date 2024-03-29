#FORMATO A LOGS
#en el archivo o en consola se ven 3 partes: el nivel, el logger y el mensaje
#se define el formato desde basicConfig()
#se puede definir el fomato impresion atraves de los atributos de log record de la libreria
#hay diferentes argumentos como: nivel, mensaje, numero de proceso, la hora etc
#estos argumentos se encuentran el la documentacion de logging

#imprimir el nivel y el formato separado por un guion - usando basicConfig

import logging

logging.basicConfig(
    level=logging.DEBUG,
    format="%(levelname)s - %(message)s - %(asctime)s", #la "s" es de string
    datefmt="%H:%M:%S" 
)

nombre = "Pancho"

logging.error(f"{nombre} creo el error")
logging.warning("log de advertencia")
logging.error("log de error")
logging.critical("log de error critico")

try:
    division = 2 / 0
except:
    logging.exception("Division por cero")

#Regresa en consola
#WARNING - log de advertencia
#ERROR - log de error
#CRITICAL - log de error critico

#cuando agregamos en basicConfig > format %(asctime)s regresa 
#en consola el nivel, el mensaje y el tiempo exacto que se ejecuto
#WARNING - log de advertencia - 2024-01-18 20:16:59,643
#ERROR - log de error - 2024-01-18 20:16:59,644
#CRITICAL - log de error critico - 2024-01-18 20:16:59,644

#si solo queremos el tiempo añadimos el paramentro datefmt=
#cambia el fomato del tiempo, el la libreria "time" encontramos todos los formatos
#WARNING - log de advertencia - 20:23:37
#ERROR - log de error - 20:23:37
#CRITICAL - log de error critico - 20:23:37

#usar el valor que tiene una variable en el momento del registro para un mejor conocimento del evento
#ERROR - Pancho creo el error - 20:32:06

#usarlos dentro de excepciones que son bloques de codigo que capturan errores
#ERROR - Division por cero - 20:35:39
"""try:
    division = 2 / 0
except:
    logging.error("Division por cero")"""
    
#logging.exception muestra tanto el error y como el mensaje de lo ocurrido
#en este caso el error es que se dividio por cero
"""ERROR - Division por cero - 20:38:05
Traceback (most recent call last):
  File "C:\Users\jovan\Python\Desarrollador Python\Avanzado 1\logs.py\formato_logs.py", line 26, in <module>
    division = 2 / 0
               ~~^~~
ZeroDivisionError: division by zero"""