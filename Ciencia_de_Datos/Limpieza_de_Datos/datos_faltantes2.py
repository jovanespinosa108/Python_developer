import pandas as pd

df = pd.read_csv("empleados.csv", delimiter=";")

print(df.head(20))
print(df.shape)
print(df.isnull().sum())
print(df.notnull().sum())

"""
       Nombre  Apellido       Sexo  ... Salario  Gerencia          Departamento
0   Alexandro       NaN  Masculino  ...  2423.0        No            Publicidad     
1      Carlos       NaN  Masculino  ...  3132.0        Sí                   NaN     
2      Felipa       NaN   Femenino  ...  2639.0        No             Comercial     
3      Daniel       NaN  Masculino  ...  3122.0        No             Comercial     
4        John       NaN  Masculino  ...  3431.0        Sí  Servicios al cliente     
5      Edward       NaN  Masculino  ...  4500.0        No                 Legal     
6     Ruperta       NaN   Femenino  ...  3962.0        No              Producto     
7       Amaya       NaN   Femenino  ...  2450.0       NaN             Comercial     
8   Francisca       NaN   Femenino  ...  2564.0        No                    IT     
9      Selena       NaN   Femenino  ...  2709.0        Sí          Contabilidad     
10       Febe       NaN   Femenino  ...  4359.0        No                   NaN     
11     Ximena       NaN   Femenino  ...  4532.0        No                 Legal     
12      David       NaN  Masculino  ...  1977.0        No      Recursos Humanos     
13        Max       NaN  Masculino  ...  2953.0        No                Ventas     
14     Selena       NaN   Femenino  ...  2709.0        Sí          Contabilidad     
15        NaN       NaN   Femenino  ...     NaN       NaN                   NaN     
16      Paula       NaN   Femenino  ...  3306.0        No              Producto     
17        Tim       NaN  Masculino  ...  2518.0        No      Recursos Humanos     
18     Andrew       NaN  Masculino  ...  3194.0        No              Producto     
19     Gloria       NaN   Femenino  ...  3267.0        No  Servicios al cliente     

[20 rows x 9 columns]
(251, 9)
Nombre            6
Apellido        251
Sexo             37
Estado_Civil      4
Edad             61
Experiencia       4
Salario           6
Gerencia         21
Departamento     12
dtype: int64
Nombre          245
Apellido          0
Sexo            214
Estado_Civil    247
Edad            190
Experiencia     247
Salario         245
Gerencia        230
Departamento    239
dtype: int64 """

#crea una nueva variable para guardar la tabla actualizada
#usa la funcion drop para eliminar
#axis=1 sirve para borrar las columnas
#declara el nombre de la columna a eliminar dentro de una lista
df_updated = df.drop(axis=1, columns=["Apellido"])

print(df_updated.head(20))
