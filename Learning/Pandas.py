# from pandas import Series, DataFrame
# import pandas as pd
# import numpy as np
#
# sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# states = ['California', 'Ohio', 'Oregon', 'Texas'] #Ordered
#
# obj3 = Series(sdata)
# obj4 = Series(sdata, index=states)
# #print(obj3+obj4)
#
# data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],'year': [2000, 2001, 2002, 2001, 2002],'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# frame = DataFrame(data,index=['one', 'two', 'three', 'four', 'five'])
# #print(frame)
# frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
# val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
# frame2['debt'] = val
# #print(frame2)
#
# pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
#
# frame3 = DataFrame(pop)
# frame3.index.name = 'year'; frame3.columns.name = 'state'
# #print(frame3.values)
#
#
# obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
# #print(obj)
# obj2 = obj.reindex(['a','b','c','d','e'],fill_value=0)
# obj3 = Series(['blue', 'purple', 'yellow'],index=[0,2,4])
# #
# #print(obj3.reindex([0,1,2,3,4,5],method='ffill'))
#
# frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],columns=['Ohio', 'Texas', 'California'])
# #$print(frame)
# frame2 = frame.reindex(columns=['Texas', 'Utah', 'California'])
# #print(frame2)
#
# data = DataFrame(np.arange(16).reshape((4, 4)),index=['Ohio', 'Colorado', 'Utah', 'New York'],columns=['one', 'two', 'three', 'four'])
# #print(data)
# #print(data.drop(['one','two'],axis=1))
# #print(data[:2])
#
# df = DataFrame([[1.4, np.nan], [7.1, -4.5],[np.nan, np.nan], [0.75, -1.3]],index=['a', 'b', 'c', 'd'],columns=['one', 'two'])
# #print(df.describe())
# obj = Series(['a', 'a', 'b', 'c'] * 4)
# #print(obj)
# #print(obj.describe())
#
# import tushare as ts
# import pandas as pd
#
# price = ts.get_k_data('601111').drop('code',axis=1)
#
# price.set_index('date', inplace=True)
# #print(price.head())
# returns = price.pct_change().dropna()
# #print(returns.corr())
#
# data = Series(np.random.randn(10),index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],[1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
# #print(data['b':'c'])#按第一层索引提取
# #print(data[:, 2])#按第二次索引提取
# #print(data.unstack())
# frame = DataFrame(np.arange(12).reshape((4, 3)),index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],columns=[['Ohio', 'Ohio', 'Colorado'],['Green', 'Red', 'Green']])
# frame.index.names = ['key1', 'key2']
# frame.columns.names = ['state', 'color']
# #print(frame.sum(level='key2'))
from pandas import Series,DataFrame
import pandas as pd
import numpy as np

s1 = Series([0, 1], index=['a', 'b'])
s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
s3 = Series([5, 6], index=['f', 'g'])
#print(pd.concat([s1,s2,s3],axis=1))
s4 = pd.concat([s1 * 5, s3])
#print(s1)
#print(s3)
#print(pd.concat([s1,s4],axis=1,join_axes=[['a','c','e','f']]))
#print(pd.concat([s1, s1, s3], keys=['one', 'two', 'three']))
#print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']))

df1 = DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],columns=['one', 'two'])
df2 = DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],columns=['three', 'four'])
#print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2']))
print(pd.concat({'level1': df1, 'level2': df2}, axis=1))