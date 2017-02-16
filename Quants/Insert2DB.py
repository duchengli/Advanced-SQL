from sqlalchemy import create_engine
import tushare as ts
import pymssql
import csv

engine = create_engine('mssql+pymssql://sa:dl820113@127.0.0.1:1433/TUSHARE')

def insert2db(code):
	try:
		df=ts.get_hist_data(code,start='2015-01-01',retry_count=50,pause=0)
		df['code']=code
		df.to_sql('Hist_Daily_Data',engine,if_exists='append')
		print('股票代码'+j+'已经插入数据库')
	except:
		pass

csv_reader=csv.reader(open('c:/slist.csv'))
slist=set(row[0] for row in csv_reader)

for j in slist:
	if j!='code':
		insert2db(j)