lista_divisores = [1,2,3,0,4,5]

for numero in lista_divisores:
    if numero != 0:
        resultado = 5 / numero
        print(resultado)
    else:
        print("El divisor es cero, no se ejecutara la operacion")

#Si no se pone la condicion, el codigo ejecutara hasta donde el cero aparezca
#despues arrojara un error
#5.0
#2.5
#1.6666666666666667
#El divisor es cero, no se ejecutara la operacion
#1.25
#1.0