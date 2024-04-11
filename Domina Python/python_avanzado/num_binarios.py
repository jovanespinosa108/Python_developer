#se usa el 0b como representativo antes del numero binario
#se usa la funcion bin() para imprimir los numeros binarios como binarios
#convertir de string a binario se usa la funcion int() convierte en integer
#se usa el 2 como base del numero binario, como segundo paramentro  

bin_5 = 0b101
bin_10 = 0b1010
resultado_int = bin_5 + bin_10
print(bin_5)
print(bin_10)
print(resultado_int)
print(bin(resultado_int))

#binarios en string
bin_7 = "0b111"
bin_12 = "0b1100"
resultado_string = int(bin_7, 2) + int(bin_12, 2)
print(bin_7)
print(bin_12)
print(resultado_string)
print(bin(resultado_string))

#5
#10
#15
#0b1111
#0b111
#0b1100
#19
#0b1001
