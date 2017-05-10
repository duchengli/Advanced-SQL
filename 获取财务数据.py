#获取各股的财务数据，用于选择成长股

#import csv
import tushare as ts
import pandas as pd

def get_growthdata(year,quarter):
	col_name = str(year)+'0'+str(quarter)
	retry_time = 50
	for i in range(retry_time):
		try:
			df = ts.get_growth_data(year,quarter)
			df.rename(columns = lambda x:x.replace('mbrg','mbrg'+col_name), inplace = True)
			#df.set_index('code', inplace = True)
			#return df['mbrg'+col_name]
			return df.loc[:,['code','mbrg'+col_name]]
			break
		except:
			if i < retry_time-1:
				continue
			else:
				print('can not fetch data')

base_df = get_growthdata(2016,4)
for year in range(2007,2017):
	for month in range(1,5):
		if year==2016 and month==4:
			pass
		else:
			base_df=pd.merge(base_df,get_growthdata(year,month),left_on='code',right_on='code')
