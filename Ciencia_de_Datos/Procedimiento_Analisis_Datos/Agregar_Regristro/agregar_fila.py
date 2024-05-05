import pandas as pd

df = pd.read_csv("temperaturas.csv", delimiter=";")

print(df)

#nueva variable usa pandas DataFrame y el metodo from_dict() agrega fila como lista formato diccionario key-value
nueva_temperatura = pd.DataFrame.from_dict([{"Año": "2022", "temperatura": "73.8"},{"Año": "2023", "temperatura": "74.3"}])

#concatena la info existente del df con la nueva informacion en la nueva variable, 
#ignora el index
df = pd.concat([df, nueva_temperatura], ignore_index=True)

print(df)
