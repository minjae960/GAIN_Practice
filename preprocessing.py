# pm data preprocessing to get rid of NA

import pandas as pd

pm = pd.read_csv('data/pm_raw.csv')

pm = pm.dropna()
pm = pm.drop(columns=['date', 'location', 'lat', 'lon'])

pm.to_csv('data/pm.csv', index=False)

pm = pd.read_csv('data/pm.csv')



import pandas as pd
import random
import numpy as np

pm = pd.read_csv('data/pm.csv')

rows = len(pm.index)
missing_rate = 0.2
data = 'ion'

num_rows = int(rows*missing_rate)
random_row = random.sample(range(rows), num_rows)

pm_col = pm.columns.tolist()

col_dic = {'ocec': ['OC', 'EC'],
           'ele': ['Si', 'S', 'K', 'Ca', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Ni', 'Cu', 'Zn', 'As', 'Se', 'Br', 'Ba', 'Pb'],
           'ion': ['SO42.', 'NO3.', 'Cl.', 'Na.', 'NH4.', 'K.', 'Mg2.', 'Ca2.'],
           'ocec+ele': ['OC', 'EC', 'Si', 'S', 'K', 'Ca', 'Ti', 'V', 'Cr', 'Mn', 'Fe', 'Ni', 'Cu', 'Zn', 'As', 'Se',
                        'Br', 'Ba', 'Pb'],
           'ocec+ion': ['OC', 'EC', 'SO42.', 'NO3.', 'Cl.', 'Na.', 'NH4.', 'K.', 'Mg2.', 'Ca2.'],
           'ele+ion': ['SO42.', 'NO3.', 'Cl.', 'Na.', 'NH4.', 'K.', 'Mg2.', 'Ca2.', 'Si', 'S', 'K', 'Ca', 'Ti', 'V',
                       'Cr', 'Mn', 'Fe', 'Ni', 'Cu', 'Zn', 'As', 'Se', 'Br', 'Ba', 'Pb'],
           'all': ['OC', 'EC', 'SO42.', 'NO3.', 'Cl.', 'Na.', 'NH4.', 'K.', 'Mg2.', 'Ca2.', 'Si', 'S', 'K', 'Ca', 'Ti',
                   'V', 'Cr', 'Mn', 'Fe', 'Ni', 'Cu', 'Zn', 'As', 'Se', 'Br', 'Ba', 'Pb']
           }

for i in col_dic[data]:
    for r in random_row:
        pm.at[r, i]=np.nan

pm.to_csv('data/pm_ion.csv', index=False)