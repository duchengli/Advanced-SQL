import pandas as pd
import numpy as np
from pandas import DataFrame,Series
import re
import json

db = json.load(open('d:/pydata-book/ch07/foods-2011-10-03.json'))

info_keys = ['description', 'group', 'id', 'manufacturer']
info = DataFrame(db, columns=info_keys)
info_keys = ['description', 'group', 'id', 'manufacturer']
info = DataFrame(db, columns=info_keys)

nutrients = []
for rec in db:
    fnuts = DataFrame(rec['nutrients'])
    fnuts['id'] = rec['id']
    nutrients.append(fnuts)
nutrients = pd.concat(nutrients, ignore_index=True)
nutrients = nutrients.drop_duplicates()

col_mapping = {'description' : 'food','group' : 'fgroup'}
info = info.rename(columns=col_mapping, copy=False)

col_mapping = {'description' : 'nutrient','group' : 'nutgroup'}
nutrients = nutrients.rename(columns=col_mapping, copy=False)

ndata = pd.merge(nutrients, info, on='id', how='outer')
print(ndata.head())
print('\n')
print(ndata.info())