# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:07:37 2020

@author: csarzosa
"""

import pandas as pd

path = "./data/artwork.csv"

df1 = pd.read_csv(
    path,
    nrows=10)

columnas = ['id', 'artist', 'title', 'medium', 'year',
            'acquisitionYear', 'height', 'width', 'units']

df2 = pd.read_csv(
    path,
    nrows=10,
    usecols= columnas
    )

df3 = pd.read_csv(
    path,
    usecols= columnas,
    index_col='id')


path_save = "./data/artwork.pickle"

df3.to_pickle(path_save)

df5 = pd.read_pickle(path_save)

