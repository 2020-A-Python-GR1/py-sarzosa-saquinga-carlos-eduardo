import numpy as np
import pandas as pd

# 1) Examen

# 2) Crear un vector de ceros de tamaño 10
arreglo1 =  np.zeros(10)
print(arreglo1)

# 3) Crear un vector de ceros de tamaño 10 y el de la posicion 5 sea igual a 1
arreglo2 =  np.zeros(10)


# 4) Cambiar el orden de un vector de 50 elementos, el de la posicion 1 es el de la 50 etc.
arreglo3 = np.arange(1,51)
arreglo4 = sorted(arreglo3, reverse= True)
print(arreglo4)

# 5) Crear una matriz de 3 x 3 con valores del cero al 8
arreglo5 = np.arange(9).reshape(3,3)
print(arreglo5)

# 6) Encontrar los indices que no sean cero en un arreglo
arreglo6 = [1,2,0,0,4,0]
arreglo61 = np.nonzero(arreglo6)
print(arreglo61)

#7) Crear una matriz de identidad 3 x 3
arreglo7 = np.eye(3)
print(arreglo7)

# 8) Crear una matriz 3 x 3 x 3 con valores randomicos
arreglo8 = np.random.random((3,3,3))
print(arreglo8)

# 9) Crear una matriz 10 x 10 y encontrar el mayor y el menor
arreglo9 = np.random.random((10,10))
arreglo91 = arreglo9.min()
arreglo92 = arreglo9.max()
print("Min:", arreglo91, "Max:",arreglo92)

# 10) Sacar los colores RGB unicos en una imagen (cuales rgb existen ej: 0, 0, 0 - 255,255,255 -> 2 colores)


# 11) ¿Como crear una serie de una lista, diccionario o arreglo?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))

serie1 = pd.Series(mylist)
serie2 = pd.Series(myarr)
serie3 = pd.Series(mydict)


# 12) ¿Como convertir el indice de una serie en una columna de un DataFrame?
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)
# Transformar la serie en dataframe y hacer una columna indice



# 13) ¿Como combinar varias series para hacer un DataFrame?
import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))

df = pd.DataFrame(columns = ['A', 'B'])
df['A'] = ser1
df['B'] = ser2


#14) ¿Como obtener los items que esten en una serie A y no en una serie B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

sr3 = pd.Series(np.union1d(ser1, ser2))
sr4 = pd.Series(np.intersect1d(ser1, ser2))

resultado = sr3[~sr3.isin(sr4)]


# 15) ¿Como obtener los items que no son comunes en una serie A y serie B?
ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])

sr3 = pd.Series(np.union1d(ser1, ser2))
sr4 = pd.Series(np.intersect1d(ser1, ser2))


# 16) ¿Como obtener el numero de veces que se repite un valor en una serie?
ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))


# 17) ¿Como mantener los 2 valores mas repetidos de una serie, y a los demas valores cambiarles por 0 ?
np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))


# 18) ¿Como transformar una serie de un arreglo de numpy a un DataFrame con un shape definido?
ser = pd.Series(np.random.randint(1, 10, 35))
shape(7,5)


# 19) ¿Obtener los valores de una serie conociendo la posicion por indice?
ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]
# a e i o u


# 20) ¿Como anadir series vertical u horizontalmente a un DataFrame?
ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))

df3 = df.append(pd.Series(ser1, index=['col1','col2']), ignore_index=True)
df4 = df.append(pd.Series(ser2, colums=['col1','col2']), ignore_index=True)


# 22)¿Como importar solo columnas especificas de un archivo csv?
path = "./data/BostonHousing.csv"

columnas = ['crim', 'zn', 'indus']

df2 = pd.read_csv(
    path,
    nrows=10,
    usecols= columnas
    )


