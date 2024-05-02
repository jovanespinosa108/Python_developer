import pandas as pd
from sklearn.linear_model import LinearRegression

#crea modelo regresion lineal
regresion_lineal = LinearRegression()

#se asigna a df leer el csv file por medio de pandas, con delimiter ";"
df = pd.read_csv("empleados_regresion.csv", delimiter=";")

#muestra las columnas del dataframe con las primeras 20 lineas
print(df.head(20))

#imprime todos los valores nulos de todas las columnas
print(df.isnull().sum())

#guarda datos nulos de la columna "Edad"
datos_test = df[df["Edad"].isnull()==True]


datos_entrenamiento = df[df["Edad"].isnull()==False]

#contiene datos de "Edad"
y_entrenamiento = datos_entrenamiento["Edad"]

#contiene datos de "Experiencia" y "Salario", Elimina datos de "Edad"
x_entrenamiento = datos_entrenamiento.drop("Edad", axis=1)

#construye el model de regresion lineal con los datos de "x" y "y"
regresion_lineal.fit(x_entrenamiento, y_entrenamiento)

#elimina de "datos_test" la columna "Edad"
datos_test = datos_test.drop("Edad", axis=1)

#funcion predict() hace prediciones de la regresion lineal
predicciones = regresion_lineal.predict(datos_test)

print(predicciones)

#remplaza valores de test por los de predicciones
datos_test["Edad"] = predicciones

print(datos_test)
