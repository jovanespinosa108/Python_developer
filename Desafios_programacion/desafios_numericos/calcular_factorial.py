# crea funcion para calcular el factorial de un numero "n"
#el factorial de un numero positivo es la multiplicacion de todos los numeros enteros menores a "n"
#la funcion calculara el factorial usando un ciclo o una funcion recursiva

def factorial_num(numero): #funcion que guarda el valor de numero

    factorial = 1 # la variable empieza con el numero 1 y acomula el factorial con cada pasada del ciclo
    for i in range(2, numero+1): #para i en el rango desde 2, hasta el valor de numero mas 1 por que range excluye el ultimo numero del rango
        factorial = factorial * i #el resultado de multiplicar el numero iterado por el valor que tenia el factorial anteriormente
    return factorial

print(factorial_num(0)) #1
print(factorial_num(3)) #6
print(factorial_num(6)) #720
print(factorial_num(7)) #5040

#funcion recursiva

def calcular_factorial_recursivo(numeroR):

    if numeroR == 0 or numeroR == 1:
        return 1
    return numeroR * calcular_factorial_recursivo(numeroR -1)

print(calcular_factorial_recursivo(0)) #1
print(calcular_factorial_recursivo(3)) #6
print(calcular_factorial_recursivo(6)) #720
print(calcular_factorial_recursivo(7)) #5040

