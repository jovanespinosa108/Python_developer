import subprocess

nombre_bash = "bash_ejemplo"
contenido = ""

with open(nombre_bash, mode="rb") as archivo_bash:
    contenido = archivo_bash.read()

print(f"Contenido del archivo: {contenido}")
subprocess.call(contenido, shell=True)

#se debe importar la libreria: subprocess
#se usa bash en sistemas Linux que contengan MacOS o Ubuntu
#para windows existe la herramienta bat
#bash es una herramienta para escribir instrucciones al sistema operativo