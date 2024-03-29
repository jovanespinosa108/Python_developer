import logging

#este basicConfig se declara solo una vez en cada archivo
#sintaxis: basicConfig("primer nivel", crea achivo con los logs, evita que se sobre escriban los logs)
logging.basicConfig(level=logging.DEBUG, filename="ejemplo_logs.log", filemode="w")

logging.debug("Log de debugging")
logging.info("log de Informacion")
logging.warning("log de advertencia")
logging.error("log de error")
logging.critical("log de error critico")


"""Proceso para obtener los logs (registros) del programa,
un log nos ayuda a entender el comportamiento del programa,
nos ayuda a entender cuando se produce un error, python usa
la libreria loggin, esta libreria nos permite usar un objeto llamado
Loger, para definir la manera de crear los logs, estos son creados 
con un nivel de seguridad que indica si el programa es informativo, 
de desarrollo, advertencia o errores, existen 5 niveles de seguridad """
#Debug: info detallada mientras se desarrolla partes de codigo a revisar
#Info: Reporte de eventos donde se requirere informacion
#warning: reporte de algo inesperado que a sucedido o susedera en el codigo
#error: Reporte de algo que no se ejecuto por que se produjo un error en el codigo
#critical: Reporte de error grave y puede indicar que el programa se detendra
#Se invoca cada nivel y se pasa como argumento el mensaje: logging.nivel("mensaje")

