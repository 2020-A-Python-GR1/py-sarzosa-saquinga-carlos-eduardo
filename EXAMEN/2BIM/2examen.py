import numpy as np
import pandas as pd
from datetime import date, datetime
import pandas.util.testing

## 1) Crea un Dataframe de 10 registros y 6 columnas y consigue las 5 primeros y los 5 ultimos registros
arr1 = np.random.randint(0, 10, 60).reshape(10,6)

df1 = pd.DataFrame(arr1)

print(df1[:5])
print(df1[5:])

## 2) Crear un dataframe pasando un arreglo de numpy de 6 x 4 con una fecha como indice y con columnas A, B, C, D randomico
arr2 = np.random.randint(0,10,24).reshape(6, 4)
columnas = ['A', 'B', 'C', 'D']
indices = [date.today().strftime("%B %d, %Y"),
           date.today().strftime("%B %d, %Y"),
           date.today().strftime("%B %d, %Y"),
           date.today().strftime("%B %d, %Y"),
           date.today().strftime("%B %d, %Y"),
           date.today().strftime("%B %d, %Y")
        ]

df2 = pd.DataFrame(arr2, columns = columnas, index = indices)


## 4) Crear un Dataframe con 10 registros y 6 columnas y con una propiedad del Dataframe mostrar las columnas, con otro comando mostrar los valores.
arr4 = np.random.randint(0,10,60).reshape(10, 6)

df4 = pd.DataFrame(arr4)
col_df4 = df4.columns.values
val_df4 = df4.values


## 5) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe describir estadisticamente el Dataframe
arr5 = np.random.randint(0,10,60).reshape(10, 6)
df5 = pd.DataFrame(arr5)

desc = df5.describe()


## 6) Crear un Dataframe con 10 registros y 6 columnas y con una funcion del Dataframe transponer los datos
arr6 = np.random.randint(0,10,60).reshape(10, 6)
df6 = pd.DataFrame(arr6)

df6_transpuesto = df6.transpose()


## 7) Crear un Dataframe con 10 registros y 6 columnas y Ordenar el dataframe 1 vez por cada columna, ascendente y descendente
arr7 = np.random.randint(0,10,60).reshape(10, 6)
df7 = pd.DataFrame(arr7)

df7_asc = df7.apply(lambda x: x.sort_values().values)
df7_des = df7.apply(lambda x: x.sort_values(ascending = False).values)


## 8) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y seleccionar en un nuevo Dataframe solo los valores mayores a 7
arr8 = np.random.randint(1,10,60).reshape(10, 6)
df8 = pd.DataFrame(arr8)

condicion7 = df8 > 7
df_mayores_7 = df8[condicion7]

## 9) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 o valores NaN. Luego llenar los valores NaN con 0.
arr9 = np.random.randint(1,10,60).reshape(10, 6)
df9 = pd.DataFrame(arr9)

condicion5 = df9 > 5
df9_nan   = df9[condicion5]
df9_nan_0 = df9_nan.fillna(0)


## 10) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y sacar la media, la mediana, el promedio
arr10 = np.random.randint(0,10,60).reshape(10, 6)
df10 = pd.DataFrame(arr10)

media = df10.mean()
mediana = df10.median()
promedio = df10.mean()

## 11) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10, luego crear otro dateframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 y anadirlo al primer Dataframe
arr11_1 = np.random.randint(1,10,60).reshape(10, 6)
df11_1 = pd.DataFrame(arr11_1)

arr11_2 = np.random.randint(1,10,60).reshape(10, 6)
df11_2 = pd.DataFrame(arr11_2)

df11= df11_1.append(df11_2)


## 12) Crear un Dataframe con 10 registros y 6 columnas llenas de strings. Luego, unir la columna 1 y 2 en una sola, la 3 y 4, y la 5 y 6 concatenando su texto.
arr_s = pd.util.testing.rands_array(3, 60).reshape(10,6)
df12 = pd.DataFrame(arr_s)

df12_con    = pd.DataFrame(df12[0] + df12[1])
df12_con[1] = df12[2] + df12[3]
df12_con[2] = df12[4] + df12[5]

## 13) Crear un Dataframe con 10 registros y 6 columnas llenas de números randomicos del 1 al 10 enteros, obtener la frecuencia de repeticion de los numeros enteros en cada columna
arr13 = np.random.randint(0,10,60).reshape(10, 6)
df13 = pd.DataFrame(arr13)

for columna in df13.columns:
    print("Columna " + str(columna))
    print(df13[columna].value_counts())

## 14) Crear un Dataframe con 10 registros y 3 columnas, A B C, llenas de números randomicos del 1 al 10 enteros. Crear una nueva columna con el calculo por fila (A * B ) / C
arr14 = np.random.randint(1,10,30).reshape(10, 3)
df14 = pd.DataFrame(arr14, columns = ['A', 'B', 'C'])
resultados = []

for indice in df14.index:
    resultados.append((df14['A'][indice] * df14['B'][indice]) / df14['C'][indice] )
    
df14['Resultados'] = resultados