# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 09:29:40 2020

@author: cesarzosa
"""

import pandas as pd
import numpy as np
import os
import sqlite3


path_save = "./data/artwork.pickle"

df = pd.read_pickle(path_save)

sub_df = df.iloc[49980:50519,:].copy()

# Tipos Archivos
# JSON
# Excel
# SQL


# Excel
path_excel = "./data/artwork.xlsx"

# Con el indice como columna
sub_df.to_excel(path_excel)

# Sin el indice como columna
sub_df.to_excel(path_excel, index = False)

columnas = ['artist', 'title', 'year']

sub_df.to_excel(path_excel, columns = columnas)



path_excel_mt = "./data/artwork_mt.xlsx"

writer = pd.ExcelWriter(path_excel_mt, engine= 'xlsxwriter')

sub_df.to_excel(writer, sheet_name = 'Primera')

sub_df.to_excel(writer, sheet_name = 'Segunda')

sub_df.to_excel(writer, sheet_name = 'Tercera')

writer.save()


# Formato Condicional

path_excel_colores = "./data/artwork_colores.xlsx"

writer = pd.ExcelWriter(path_excel_colores, engine = 'xlsxwriter')

num_artistas = sub_df['artist'].value_counts()

# Series
num_artistas.to_excel(writer, sheet_name = 'Artistas')

# Seleccionando la hoja de trabajo
hoja_artistas = writer.sheets['Artistas']

rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1)
print(rango_celdas)

# Formato
formato_artistas = {
    "type": "2_color_scale",
    "min_value": "10",
    "max_value": "99",
    "max_type": "percentile"
    }

hoja_artistas.conditional_format(rango_celdas, formato_artistas)

writer.save()





# ----- SQL ----- #
with sqlite3.connect("bdd_artist.bdd") as conexion:
    sub_df.to_sql('py_artistas', conexion)
    
    
# ----- JSON ----- #
sub_df.to_json('artistas.json')
sub_df.to_json('artistas_tabla.json', orient = 'table')


