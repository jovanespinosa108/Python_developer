import os


def listar_archivos(ruta):
    lista_archivos = os.listdir(ruta)
    return lista_archivos

ruta_absoluta = os.getcwd()
ruta_relativa = "python_intermedio/"
archivos = listar_archivos(ruta_relativa)
print(archivos)

#Con "ruta absoluta" en variable archivos obtenemos este listado de directorios:
"""['abrir_mostrar_img.py', 'concatenar.py', 'formato_tiempo.py', 
'funcion_zip.py', 'listar_archivos.py', 'Lost Lamb.jpg', 
'notas_excepcion.py', 'type_hinting.py']"""

