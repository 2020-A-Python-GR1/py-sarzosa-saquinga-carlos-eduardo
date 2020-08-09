# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 14:18:30 2020

@author: cesarzosa
"""

import xlsxwriter
import pandas as pd


path_save = "./artwork.pickle"
df = pd.read_pickle(path_save)
sub_df = df.iloc[49980:50519, :].copy()

num_artistas = sub_df['artist'].value_counts()
rango_celdas = 'B2:B{}'.format(len(num_artistas.index) + 1)

workbook = xlsxwriter.Workbook('chart.xlsx')
worksheet = workbook.add_worksheet()
bold = workbook.add_format({'bold': 1})


headings = ['Artistas', 'Top']
data = [
    num_artistas.index,
    num_artistas.values,
]


worksheet.write_row('A1', headings, bold)
worksheet.write_column('A2', data[0])
worksheet.write_column('B2', data[1])


chart = workbook.add_chart({'type': 'pie'})

chart.add_series({
    'name': 'Artist',
    'categories': '=Sheet1!$A$2:$A$11'.format(len(num_artistas.index)+1),
    'values': '=Sheet1!$B$2:$B$11'.format(len(num_artistas.index)+1),
    'data_labels': {'percentage': True},
    }) 


chart.set_title({'name': 'Top 10 Artistas'})
chart.set_style(26)
worksheet.insert_chart('D2', chart, {'x_offset': 25, 'y_offset': 10})


workbook.close()