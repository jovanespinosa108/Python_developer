import time
import asyncio

def funcion_sincrona():
    print("Ejecutando funcion sincrona")
    time.sleep(1)
    print("Fin funcion sincrona")

async def funcion_asincrona():
    print("Ejecutando funcion asincrona")
    await asyncio.sleep(1)
    print("Fin funcion asincrona")


#Para correr las funciones Async debe hacerlo una funcion principal que ejecute las corrutinas
#por convencion esta funcion debe llamarse main()

async def main():
    corrutinas = [funcion_asincrona(), funcion_asincrona()]
    await asyncio.gather(*corrutinas)

inicio = time.time()
asyncio.run(main())  #esto ejecuta solo las funciones asincronas
print(f"Tiempo asincrono: {time.time() - inicio}")

#aqui se corrio 2 veces la funcion 

inicio = time.time()
funcion_sincrona()
funcion_sincrona() #esto ejecuta la funcion sincrona en forma consecutiva
print(f"Tiempo sincrono: {time.time() - inicio}")
