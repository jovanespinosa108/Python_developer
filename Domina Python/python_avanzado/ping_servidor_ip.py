#ping: enviar una señar a un servidor
#se hace ping a servidores o dominios

import os


def hacer_ping(hostname):
    respuesta = os.system(f"ping {hostname}")
    if respuesta == 0:
        print(f"{hostname} esta activo")
    else:
        print(f"{hostname} esta incativo")

hacer_ping("linkedin.com")