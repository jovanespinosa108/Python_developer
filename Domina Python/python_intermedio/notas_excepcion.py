#usamos try: except:
#para version python 3.10 hacia atras usamos "rise Exeption"
try:
    print("Texto con formato {}".format()) #Error: Falta argumento en format()
except Exception as e:
    raise Exception("Ha ocurrido un error")

"""Traceback (most recent call last):
  File "C:\Users\jovan\Python\Desarrollador Python\Domina Python\python_intermedio\notas_excepcion.py", 
  line 5, in <module>
    raise Exception("Ha ocurrido un error")
Exception: Ha ocurrido un error"""

#para versiones python 3.10 hacia adelante usamos add_note() method

#except Exception as e:
    #e.add_note("Ha ocurrido un error")
    #print(e.__notes__)
