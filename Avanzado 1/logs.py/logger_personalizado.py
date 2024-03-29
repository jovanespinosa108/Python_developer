#se importa la libreria logging, y se crea una variable para el logger personalizado

import logging

#en la variable se llama la libreria "logging" y se usa la funcion getLogger()
logger = logging.getLogger(__name__)
print(logger)

logger.warning("log de advertencia")

#imprime en consola:
"""<Logger logger_personalizado (WARNING)>
log de advertencia"""

#si usamos como argumento en getLogger(__name__) este regresara __main__
"""logger = logging.getLogger(__name__)
print(logger)

logger.warning("log de advertencia")"""

#imprime en consola
"""<Logger __main__ (WARNING)>
log de advertencia"""

#si se importa el archivo a un nuevo por ejemplo a: principal.py
#import logger_personalizado

#imprime en consola
"""<Logger logger_personalizado (WARNING)>
log de advertencia"""