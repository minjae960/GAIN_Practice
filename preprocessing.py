# pm data preprocessing to get rid of NA

import pandas as pd

pm = pd.read_csv('data/pm_raw.csv')

pm = pm.dropna()
pm = pm.drop(columns=['date', 'location', 'lat', 'lon'])

pm.to_csv('data/pm.csv', index=False)