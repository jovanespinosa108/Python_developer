#Uso de las fechas
# -creacion de reportes
# -bases de datos
# -tareas programadas

from datetime import datetime

ahora = datetime.now()
print(ahora, type(ahora))

fecha_anio = ahora.strftime("%Y:%M:%d")
print(fecha_anio, type(fecha_anio))

horas_24 = ahora.strftime("%H:%M:%S")
print("Formato 24 hrs", horas_24, type(horas_24))

horas_12 = ahora.strftime("%I:%M:%S %p")
print("Formato 12 hrs", horas_12, type(horas_12))

#2024-03-30 20:56:02.296477 <class 'datetime.datetime'>
#2024:56:30 <class 'str'>
#Formato 24 hrs 20:56:02 <class 'str'>
#Formato 12 hrs 08:56:02 PM <class 'str'>
