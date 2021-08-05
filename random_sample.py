import numpy as np
import random
import pandas as pd

unif_matrix = np.full((10, 29), 1)

random_row = random.sample(range(10), 3)

data_x_col = pd.read_csv('data/pm.csv').columns.tolist()

col_dic = {'ocec': ['OC', 'EC'], 'ion': ['Si', 'S', 'K', 'Ca', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Ni', 'Cu', 'Zn', 'As', 'Se', 'Br', 'Ba', 'Pb'],
           'com': ['SO42.', 'NO3.', 'Cl.', 'Na.', 'NH4.', 'K.', 'Mg2.', 'Ca2.'], 'pm': ['PM2.5', 'PM10']}

col = []
for k in col_dic['com']:
    index = data_x_col.index(k)
    col.append(index)

for i in col:
    unif_matrix[random_row, i] = 0