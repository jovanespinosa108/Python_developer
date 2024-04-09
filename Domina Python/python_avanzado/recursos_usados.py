#se importa la libreria psutil con pip install
import psutil

def recursos_usados_cpu():
    nucleos = psutil.cpu_count(logical=False)
    print("Cantidad de nucleos usados", nucleos)

    carga = psutil.getloadavg()
    print("Carga promedio", carga)

    uso = psutil.cpu_percent(interval=5, percpu=True)
    print("Porcentage de uso de CPU", uso)

recursos_usados_cpu()

#Cantidad de nucleos usados 4
#Carga promedio (0.0, 0.0, 0.0)
#Porcentage de uso de CPU [7.7, 4.7, 2.5, 0.9, 0.3, 0.0, 0.0, 0.0]
