#Chapter2
# path = 'd:/pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

import json
from collections import Counter

path = 'd:/pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'
records = [json.loads(line) for line in open(path)]

#for k,v in records[0].items():
#    print(k+':'+str(v))

time_zones = [rec['tz'] for rec in records if 'tz' in rec]
counts = Counter(time_zones)
#print(counts.most_common(10))


from pandas import DataFrame, Series
import pandas as pd; import numpy as np
frame = DataFrame(records)
#print(frame['tz'].dropna().shape)
#print(frame['tz'].isnull().sum())
clean_tz = frame['tz'].fillna('Missing')
clean_tz[clean_tz == ''] = 'Unknown'
#print(clean_tz.value_counts()[:10])

results = Series([x.split()[0] for x in frame.a.dropna()])
#print(results.value_counts()[:10])
cframe = frame[frame.a.notnull()]
operating_system = np.where(cframe['a'].str.contains('Windows'),'Windows', 'Not Windows')
by_tz_os = cframe.groupby(['tz', operating_system])
agg_counts = by_tz_os.size().unstack().fillna(0)
indexer = agg_counts.sum(1).argsort()
count_subset = agg_counts.take(indexer)[-10:]
#print(count_subset)

import pandas as pd

unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
users = pd.read_table('d:/pydata-book-master/ch02/movielens/users.dat', sep='::', header=None, names=unames,engine='python')
rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
ratings = pd.read_table('d:/pydata-book-master/ch02/movielens/ratings.dat', sep='::', header=None, names=rnames,engine='python')
mnames = ['movie_id', 'title', 'genres']
movies = pd.read_table('d:/pydata-book-master/ch02/movielens/movies.dat', sep='::', header=None, names=mnames,engine='python')
data = pd.merge(pd.merge(ratings, users), movies)
print(data.describe())
# # from pandas import Series, DataFrame
# # import pandas as pd
# # import numpy as np
# #
# # sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
# # states = ['California', 'Ohio', 'Oregon', 'Texas'] #Ordered
# #
# # obj3 = Series(sdata)
# # obj4 = Series(sdata, index=states)
# # #print(obj3+obj4)
# #
# # data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],'year': [2000, 2001, 2002, 2001, 2002],'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
# # frame = DataFrame(data,index=['one', 'two', 'three', 'four', 'five'])
# # #print(frame)
# # frame2 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'], index=['one', 'two', 'three', 'four', 'five'])
# # val = Series([-1.2, -1.5, -1.7], index=['two', 'four', 'five'])
# # frame2['debt'] = val
# # #print(frame2)
# #
# # pop = {'Nevada': {2001: 2.4, 2002: 2.9}, 'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
# #
# # frame3 = DataFrame(pop)
# # frame3.index.name = 'year'; frame3.columns.name = 'state'
# # #print(frame3.values)
# #
# #
# # obj = Series([4.5, 7.2, -5.3, 3.6], index=['d', 'b', 'a', 'c'])
# # #print(obj)
# # obj2 = obj.reindex(['a','b','c','d','e'],fill_value=0)
# # obj3 = Series(['blue', 'purple', 'yellow'],index=[0,2,4])
# # #
# # #print(obj3.reindex([0,1,2,3,4,5],method='ffill'))
# #
# # frame = DataFrame(np.arange(9).reshape((3, 3)), index=['a', 'c', 'd'],columns=['Ohio', 'Texas', 'California'])
# # #$print(frame)
# # frame2 = frame.reindex(columns=['Texas', 'Utah', 'California'])
# # #print(frame2)
# #
# # data = DataFrame(np.arange(16).reshape((4, 4)),index=['Ohio', 'Colorado', 'Utah', 'New York'],columns=['one', 'two', 'three', 'four'])
# # #print(data)
# # #print(data.drop(['one','two'],axis=1))
# # #print(data[:2])
# #
# # df = DataFrame([[1.4, np.nan], [7.1, -4.5],[np.nan, np.nan], [0.75, -1.3]],index=['a', 'b', 'c', 'd'],columns=['one', 'two'])
# # #print(df.describe())
# # obj = Series(['a', 'a', 'b', 'c'] * 4)
# # #print(obj)
# # #print(obj.describe())
# #
# # import tushare as ts
# # import pandas as pd
# #
# # price = ts.get_k_data('601111').drop('code',axis=1)
# #
# # price.set_index('date', inplace=True)
# # #print(price.head())
# # returns = price.pct_change().dropna()
# # #print(returns.corr())
# #
# # data = Series(np.random.randn(10),index=[['a', 'a', 'a', 'b', 'b', 'b', 'c', 'c', 'd', 'd'],[1, 2, 3, 1, 2, 3, 1, 2, 2, 3]])
# # #print(data['b':'c'])#按第一层索引提取
# # #print(data[:, 2])#按第二次索引提取
# # #print(data.unstack())
# # frame = DataFrame(np.arange(12).reshape((4, 3)),index=[['a', 'a', 'b', 'b'], [1, 2, 1, 2]],columns=[['Ohio', 'Ohio', 'Colorado'],['Green', 'Red', 'Green']])
# # frame.index.names = ['key1', 'key2']
# # frame.columns.names = ['state', 'color']
# # #print(frame.sum(level='key2'))
# from pandas import Series,DataFrame
# import pandas as pd
# import numpy as np
# 
# s1 = Series([0, 1], index=['a', 'b'])
# s2 = Series([2, 3, 4], index=['c', 'd', 'e'])
# s3 = Series([5, 6], index=['f', 'g'])
# #print(pd.concat([s1,s2,s3],axis=1))
# s4 = pd.concat([s1 * 5, s3])
# #print(s1)
# #print(s3)
# #print(pd.concat([s1,s4],axis=1,join_axes=[['a','c','e','f']]))
# #print(pd.concat([s1, s1, s3], keys=['one', 'two', 'three']))
# #print(pd.concat([s1, s2, s3], axis=1, keys=['one', 'two', 'three']))
# 
# df1 = DataFrame(np.arange(6).reshape(3, 2), index=['a', 'b', 'c'],columns=['one', 'two'])
# df2 = DataFrame(5 + np.arange(4).reshape(2, 2), index=['a', 'c'],columns=['three', 'four'])
# #print(pd.concat([df1, df2], axis=1, keys=['level1', 'level2']))
# #print(pd.concat({'level1': df1, 'level2': df2}, axis=1))
# 
# df = DataFrame({'key1' : ['a', 'a', 'b', 'b', 'a'],'key2' : ['one', 'two', 'one', 'two', 'one'],'data1' : np.random.randn(5),'data2' : np.random.randn(5)})
# grouped = df['data1'].groupby(df['key1'])
# #print(df['data1'].groupby([df['key1'], df['key2']]).mean().unstack())
# #states = np.array(['Ohio', 'California', 'California', 'Ohio', 'Ohio'])
# #years = np.array([2005, 2005, 2006, 2005, 2006])
# #print(df['data1'].groupby([states, years]).mean())
# #for name, group in df.groupby('key1'):
# #    print(name)
# #    print(group)
# 
# # for (k1, k2), group in df.groupby(['key1', 'key2']):
# #     print(k1, k2)
# #     print(group)
# 
# # grouped = df.groupby(df.dtypes, axis=1)
# # print(dict(list(grouped)))
# 
# # print(df.groupby(['key1', 'key2'])[['data2']].mean())
# 
# people = DataFrame(np.random.randn(5, 5),columns=['a', 'b', 'c', 'd', 'e'],index=['Joe', 'Steve', 'Wes', 'Jim', 'Travis'])
# people.ix[2:3, ['b', 'c']] = np.nan
# #print(people)
# mapping = {'a': 'red', 'b': 'red', 'c': 'blue','d': 'blue', 'e': 'red', 'f' : 'orange'}

# by_column = people.groupby(mapping, axis=1)
# #print(by_column.sum())

# from datetime import datetime
# from pandas import Series
# import numpy as np
#
# dates = [datetime(2011, 1, 2), datetime(2011, 1, 5), datetime(2011, 1, 7),datetime(2011, 1, 8), datetime(2011, 1, 10), datetime(2011, 1, 12)]
# ts = Series(np.random.randn(6), index=dates)
#
# print(ts)