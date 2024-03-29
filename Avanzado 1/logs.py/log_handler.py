"""Log handler, en inglés, hace referencia a controlador de logs o 
de registros. En Python, un log handler es un elemento que nos permite 
configurar y personalizar los loggers. 
Cada tipo de handler permite enviar los registros de diferente manera; 
StreamHandler para consola y FileHandler para archivos. 
También existen otro tipo de handlers, como el SMTPHandler, 
que permite el envío de logs a través de email. Un log handler se 
compone de dos elementos: un formato que nos permite organizar el mensaje 
para dar contexto al registro y el nivel mínimo que nos indica la severidad 
del log o registro"""
#Los log handlers más comunes son StreamHandler y FileHandler

import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#se crea el objeto del handler
handler_consola = logging.StreamHandler()
formato_log = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
handler_consola.setFormatter(formato_log)
logger.addHandler(handler_consola)

#controlador para definir los logs en un archivo
handler_archivo = logging.FileHandler("archivo.log")
handler_archivo.setLevel(logging.ERROR)
handler_archivo.setFormatter(formato_log)
logger.addHandler(handler_archivo)

#log tipo informativo
logger.info("archivo informativo")

#regresa en consola
#2024-01-18 21:19:56,848 - __main__ - INFO - archivo informativo
# se crea un file de archivo.log que no tendra nada 
#porque pasamos el handler archivo con el nivel de ERROR