# -*- coding: utf-8 -*-
"""
Created on Tue Aug 11 07:34:12 2020

@author: cesarzosa
"""

import pandas as pd

path_save = "./data/artwork.pickle"

df = pd.read_pickle(path_save)

serie_artistas_dup = df['artist']

artistas = pd.unique(serie_artistas_dup)

print(type(artistas)) # numpy array

print(artistas.size)
print(len(artistas))

# Filtro la Serie en una columna y filtro los valores requeridos
blake = df['artist'] == 'Blake, William'  #Serie
print(blake.value_counts())  #Contar Datos

df_blake = df[blake] #DataFrames


