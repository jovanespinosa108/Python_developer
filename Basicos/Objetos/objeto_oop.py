#La funcion __init__ nos ayuda a meter los atributos en la clase, 
#este constructor nos da entrada por medio del parametro "self", 
#por medio de self podemos pedir los atributos, def __init__(self):

class PersonaUno:
    atributo = "Hombre" #atributo clase

    def __init__(self, nombre, edad):  #atributo de instancia
        self.nombre = nombre
        self.edad = edad

pedro = PersonaUno("Pedro", 17)
print(pedro.nombre)
print(pedro.edad)

print(pedro.atributo)


"""Los atributos son la variables que definene las caracteristicas del objeto, 
las clases tiene 2 tipos de atributos, los atributos de la clase 
y de instancia, 
los de instancia se definen dentro de init por ejemplo si queremos 
como atributos de instancia: nombre y edad los ponemos: def __init__(self, nombre, edad): 
Los atributos de clase se declaran fuera del constructor __init__"""

#Los metodos de la clase son funciones que se definen dentro de la clase

class Persona2:
    def __init__(self, nombre, edad):
        self.nombre = nombre  #metodo
        self.edad = edad   #metodo

    def cumple_anios(self):
        self.edad += 1
        print(f"{self.nombre} Felicitaciones por tu aniversario #{self.edad}!!")

Mayra = Persona2(nombre="Marya", edad= 27)
Mayra.cumple_anios()
# Marya Felicitaciones por tu aniversario #28!!

#clase hijo
class Empleado(Persona2):
    def __init__(self, nombre, edad, horas_totales):
        super(Empleado, self).__init__(nombre, edad)
        self.horas_totales = horas_totales #metodo

    def trabajar(self, horas_trabajadas):
        self.horas_totales += horas_trabajadas
        print(f"Haz trabajado {horas_trabajadas} horas")
        print(f"Horas totales trabajadas: {self.horas_totales} horas")

#objetos
Mayra = Empleado(nombre="Mayra", edad=27, horas_totales=30) 
Mayra.trabajar(horas_trabajadas=8)
Mayra.cumple_anios()
