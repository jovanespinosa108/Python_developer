#usar pdb para debugging, en la terminal usamos
#python -m pdb <nombre del file>
#regresara hasta el numbre del file>num de linea y el codigo que contine>
#(Pdb) podemos poner los comandos para seguir ejecutando los debuggings
#break point son puntos donde detenemos el codigo para entender su funcionamiento
#(Pdb) b(reak) <numero de linea donde se va a detener el debbuging)
#(Pdb) continue, corre el codigo hasta dode esta el break point, el numero de linea con break point tendra un B mayusula en la terminal
#(Pdb) next, no lleva directo a la linea con el break point y nos dice que contiene la linea
#(Pdb) l(ist) imprime el codigo para verificar si se ha ejecutado los comandos pasados
#inspecionar vairble sin print
#(Pdb) display + variable muestra el contenido de una variable y si ha tenido cambios
#(Pdb) undisplay deja de mostrar el contenido de la variable
#(Pdb) restart, permiten reiniciar la ejecucion e inspecion del codigo pero no borra los break-point creados

def calcular_area_cuadrado_pdb(Lado):
    "Calcula el area de un cuadrado al recibir la longitud del lado"
    area = Lado * Lado
    return area

lado_cuadrados = [3,7,9]
area_cuadrados = []
for lado in lado_cuadrados:
    area = calcular_area_cuadrado_pdb(lado)
    area_cuadrados.append(area)