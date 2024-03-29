from typing import Union

def calcular_perimetro_cuadrado(lado: Union[int, float]) -> Union[int, float]:
    return 4 * lado

print(calcular_perimetro_cuadrado(lado=5.8))