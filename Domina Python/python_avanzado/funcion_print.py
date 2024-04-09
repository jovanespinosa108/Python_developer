#diferentes usos de la funcion print

#imprimir string
print("Imprime una cadena de texto")

#imprimir el valor de una variable con f string
asiento = 798
print(f"tu numero de asiento es: {asiento}")

#imprimir elementos separados
print("Estos", "son", "elementos", "separados")

#imprimir elementos separados con sep= asignando tipo de separador
print("Estos", "son", "elementos", "separados", "con", "sep=", sep=".")
print("Estos", "son", "elementos", "separados", "con", "sep=", sep=None)
print("Estos", "son", "elementos", "separados", "con", "sep=", sep="\n")

#imprimir con end= asigna como queremos terminar el print
#esto hace que "Primero" tengo un punto al final e 
#imprimira a "Segundo" en la misma linea
print("Primero", end=".")
print("Segundo")

#imporimir con file= 
with open("print_ejemplo.txt", "w") as archivo:
    print("Pueba de texto en nuevo archivo", file=archivo)

#imprimir con flush= se usa para limpiar el buffer interno y recibe bulanos
#Buffer es un espacio de memoria para almacenar datos temporales
#usa como valor bulano por defecto "False"
#esto hace esperar a print() hasta que recibe
import time

print("inicio", flush=False)
time.sleep(2) #espera por 2 segundos
print("Fin")
#se imprime primero "inicio" y 2 segundos depues "Fin"

print("principio", end="...", flush=False)
time.sleep(3) #espera por 3 segundos
print("Final")
#se imprime todo al mismo tiempo despues de 3 segundos

print("ahora", end="...", flush=True)
time.sleep(2) #espera por 2 segundos
print("termina")
#si flush le asignamos True, veremos como se ejecuta cada linea
#con flush=True "no" se almacena la respuesta hasta el siguente salto de linea
