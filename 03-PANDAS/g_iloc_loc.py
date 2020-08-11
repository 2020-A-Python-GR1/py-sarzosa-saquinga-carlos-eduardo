# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 08:00:34 2020

@author: cesarzosa
"""

import pandas as pd

path_save = "./data/artwork.pickle"

df = pd.read_pickle(path_save)

# loc

filtrado_horizontal = df.loc[1035]  # Serie
print(filtrado_horizontal )
print(filtrado_horizontal ['artist'])
print(filtrado_horizontal .index)  # Indices columnas


serie_vertical = df['artist']
print(serie_vertical)
print(serie_vertical.index)  # Indices son los Indices

# Filtrado por Indice
df_1035 = df[df.index == 1035]

# Filtrar por Valor
segundo = df.loc[1035]  # Filtrar por indice (1)

# Filtrar por Lista
segundo = df.loc[[1035,1036]]  # Filtrar por arr indice

# Filtrar por Rango
segundo = df.loc[3:5]  # Filtrando desde X indice
                       # Hasta Y indice

# Filtrar por Arreglo True o False
segundo = df.loc[df.index == 1035]

segundo = df.loc[1035, 'artist']  # 1 Indice
segundo = df.loc[1035, ['artist', 'medium']]   # Varios Indices


# iloc -> Acceder grupo filas y columnas indices en 0
tercero = df.iloc[0]
tercero = df.iloc[[0,1]]
tercero = df.iloc[0:10]
tercero = df.iloc[df.index == 1035]

tercero = df.iloc[0:10, 0:4] # Filtrado indices
                             # Por rango de indice 0:4