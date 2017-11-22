import pandas as pd
import numpy as np
from pandas import DataFrame,Series

df = DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],'key2' : ['one', 'two', 'one', 'two', 'one'],'data1' : np.random.randn(5),'data2' : np.random.randn(5)})
print(df.groupby('key1')['data1'].mean())
print('\n')
print(df.groupby('key1')[['data2']].mean())
print('\n')
print(df.groupby('key1')[['data1','data2']].mean())