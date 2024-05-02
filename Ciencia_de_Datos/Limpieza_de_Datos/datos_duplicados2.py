import pandas as pd

df= pd.read_csv('empleados.csv', delimiter=";") #assign table with delimiter to a dataframe variable
print(df.shape) #(251, 9)

duplicates = df.duplicated() #duplicated() function finds duplicated data
print(df[duplicates]) #prints duplicates calling dataframe and as a list call the variable

"""
    Nombre  Apellido       Sexo  ... Salario  Gerencia      Departamento
14  Selena       NaN   Femenino  ...  2709.0        Sí      Contabilidad
65   Lucio       NaN  Masculino  ...  3317.0        No  Recursos Humanos

[2 rows x 9 columns]"""

df = df.drop_duplicates()
print(df) #[249 rows x 9 columns]

print(df.isnull().sum()) #imprime valores faltantes
"""
Nombre            6
Apellido        249
Sexo             37
Estado_Civil      4
Edad             61
Experiencia       4
Salario           6
Gerencia         21
Departamento     12
dtype: int64"""

df["Edad"] = df["Edad"].fillna(df["Edad"].mean()) #rellena con la media los espacios vacios 
print(df.isnull().sum())

"""
Gerencia         21
Departamento     12
dtype: int64
Nombre            6
Apellido        249
Sexo             37
Estado_Civil      4 
Edad              0  #Edad en 0s
Experiencia       4
Salario           6
Gerencia         21
Departamento     12
dtype: int64"""

