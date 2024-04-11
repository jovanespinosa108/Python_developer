#se usa el 0x como identificador representativo antes del numero binario
#se usa la funcion hex() para imprimir los numeros binarios como binarios
#convertir de string a binario se usa la funcion int() convierte en integer
#se usa el 16 como base del numeros hexadecimales, como segundo paramentro

hex_1997 = 0x7cd
hex_2023 = 0x7E7
resultado_int = hex_2023 - hex_1997
print(hex(hex_1997), hex(hex_2023), hex(resultado_int))
#0x7cd 0x7e7 0x1a

#hexadecimales en string
hex_15 = "0xf"
hex_10 = "0xa"
resultado_string = int(hex_10, 16) + int(hex_15, 16)
print(hex_15, hex_10, resultado_string, hex(resultado_string))
#0xf 0xa 25 0x19
