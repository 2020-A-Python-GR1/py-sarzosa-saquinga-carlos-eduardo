# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 08:47:07 2020

@author: csarzosa
"""

import numpy as np
import pandas as pd

arr_pand = np.random.randint(0,10,6).reshape(2,3)

df1 = pd.DataFrame(arr_pand)

s1 = df1[0]

# Operacion con la Serie

s2 = df1[1]

s3 = df1[2]

df1[3] = s1

df1[4] = s1 * s2


datos_fisicos_uno = pd.DataFrame(
    arr_pand,
    columns = [
        'Estatura (cm)',
        'Peso (kg)',
        'Edad (anios)'],
    index = [
        'Carlos',
        'Sarzosa'])


serie_peso = datos_fisicos_uno['Peso (kg)']
datos_carlos =serie_peso['Carlos']

print(serie_peso)
print(datos_carlos)


df1.index = ['Carlos', 'Sarzosa']
df1.index = ['Eduardo', 'Saquinga']
df1.columns = ['A', 'B','C', 'D', 'E']

