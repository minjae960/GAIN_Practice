# pm data preprocessing to get rid of NA

import pandas as pd

file_name = 'pm_wthr'

pm = pd.read_csv('data/{}_raw.csv'.format(file_name))

pm = pm.dropna()
pm = pm.drop(columns=['date'])

pm.to_csv('data/{}.csv'.format(file_name), index=False)