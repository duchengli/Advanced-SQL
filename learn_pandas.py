#-*- coding:utf-8 -*-

import tushare as ts
import pandas as pd

def buildLaggedFeatures(s,lag=2,dropna=True):

	if type(s) is pd.DataFrame:
		new_dict={}
		for col_name in s:
			new_dict[col_name]=s[col_name]
			# create lagged Series
			for l in range(1,lag+1):
				new_dict['%s_lag%d' %(col_name,l)]=s[col_name].shift(l)
		res=pd.DataFrame(new_dict,index=s.index)

	elif type(s) is pd.Series:
		the_range=range(lag+1)
		res=pd.concat([s.shift(i) for i in the_range],axis=1)
		res.columns=['lag_%d' %i for i in the_range]
	else:
		print('Only works for DataFrame or Series')
		return None
	if dropna:
		return res.dropna()
	else:
		return res


#df = ts.get_k_data('601111',start='2014-01-01', end='2014-12-31')
#df1=df.set_index('date')
#date = df.ix['600848']['timeToMarket']
#print(df1)

s2=s=pd.DataFrame({'a':[5,4,3,2,1], 'b':[50,40,30,20,10]},index=[1,2,3,4,5])
res2=buildLaggedFeatures(s2,lag=2,dropna=False)