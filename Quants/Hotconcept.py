import csv
import tushare as ts

def ztb(code):
	try:
		tmps=ts.get_hist_data(code,start='2017-01-01',retry_count=10,pause=2)['p_change']
		return len(tmps[tmps>=9.99])
	except:
		print(code)

tmpdict={}
csv_reader=csv.reader(open('c:/slist20170214.csv'))
concept=set(row[3] for row in csv_reader)

for j in concept:
	if j!='c_name':
		tmp=set()
		cnt=0
		csv_reader=csv.reader(open('c:/slist20170214.csv'))
		tmp=set(row[1] for row in csv_reader if row[3]==j)
		for k in tmp:
			cnt=cnt+ztb(k)
		print(j,cnt)