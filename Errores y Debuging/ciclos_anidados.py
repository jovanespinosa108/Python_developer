import itertools

lista_marca = ["Toyota", "Ford", "Mitsubishi", "Mazda", "Jeep"]
lista_anios = [2012, 2010, 2021, 2023, 2019]

marca_anios = []
for marca in lista_marca:
    for anio in lista_anios:
        marca_anios.append((marca, anio))

print(marca_anios)

#usando itertools se evita los 2 ciclos for (cilos anidados)
marca_anios= list(itertools.product(lista_marca, lista_anios))
print(marca_anios)

#imprime cada elemento de la primera lista y la conbina con cada elemento de la lista 2
"""[('Toyota', 2012), ('Toyota', 2010), ('Toyota', 2021), ('Toyota', 2023), ('Toyota', 2019), 
('Ford', 2012), ('Ford', 2010), ('Ford', 2021), ('Ford', 2023), ('Ford', 2019), 
('Mitsubishi', 2012), ('Mitsubishi', 2010), ('Mitsubishi', 2021), ('Mitsubishi', 2023), ('Mitsubishi', 2019), 
('Mazda', 2012), ('Mazda', 2010), ('Mazda', 2021), ('Mazda', 2023), ('Mazda', 2019), 
('Jeep', 2012), ('Jeep', 2010), ('Jeep', 2021), ('Jeep', 2023), ('Jeep', 2019)]"""