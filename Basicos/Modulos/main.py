#aqui llamaremos los modulos creados en modulos_paquetes.py
#del file "cuadrado" importamos las variables/modulos "perimetro y area cuadrado"
from figuras.cuadrado import area_cuadrado, perimentro_cuadrado
from figuras.circulo import area_circulo, perimentro_circulo


#crea una variable
lado = 4
#crea objeto "cuadrado" como diccionario
cuadrado = {
    "lado": lado,
    "area": area_cuadrado(lado),
    "perimetro": perimentro_cuadrado(lado)
}

print("Cuadrado: ", cuadrado)

radio = 5

circulo = {
    "radio": radio,
    "area": area_circulo(radio),
    "perimetro": perimentro_circulo(radio)
}

print("Circulo: ", circulo)

"""veremos que todas las funciones fueron ejecutadas correctamente, 
sin importar que las funciones vinieran de módulos diferentes, 
ya que los importamos a partir de un paquete, 
y de cada paquete importamos el módulo y las funciones que necesitábamos 
para cada uno de nuestros cálculos.

Cuadrado:  {'lado': 4, 'area': 16, 'perimetro': 16}
Circulo:  {'radio': 5, 'area': 78.5, 'perimetro': 31.400000000000002}"""



