from pandas import Series, DataFrame
import pandas as pd
import numpy as np

sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
states = ['California', 'Ohio', 'Oregon', 'Texas'] #Ordered

obj3 = Series(sdata)
obj4 = Series(sdata, index=states)
#print(obj3+obj4)

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data,index=['one', 'two', 'three', 'four', 'five'])
#print(frame)
frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
frame2['debt'] = val
#print(frame2)

pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}

frame3 = DataFrame(pop)
frame3.index.name = 'year'; frame3.columns.name = 'state'
#print(frame3.values)


obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
#print(obj)
obj2 = obj.reindex(['a','b','c','d','e'],fill_value=0)
obj3 = Series(['blue', 'purple', 'yellow'],index=[0,2,4])
#
#print(obj3.reindex([0,1,2,3,4,5],method='ffill'))

frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],columns=['Ohio', 'Texas', 'California'])
#$print(frame)
frame2 = frame.reindex(columns=['Texas', 'Utah', 'California'])
#print(frame2)

data = DataFrame(np.arange(16).reshape((4, 4)),index=['Ohio', 'Colorado', 'Utah', 'New York'],columns=['one', 'two', 'three', 'four'])
#print(data)
#print(data.drop(['one','two'],axis=1))
print(data[:2])