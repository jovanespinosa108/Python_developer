def calcular_factorial_recursivo(numero):
    if numero == 0 or numero == 1:
        return 1
    return numero * calcular_factorial_recursivo(numero -1)

import sys

sys.setrecursionlimit(1000)
print(sys.getrecursionlimit())

try:
    print(calcular_factorial_recursivo(1000))
except RecursionError as e:
    print("El numero es muy grande, no se puede calcular su factorial")

#1000
#El numero es muy grande, no se puede calcular su factorial