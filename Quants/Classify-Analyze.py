import csv
import tushare as ts

def ztb(code):
	try:
		tmps=ts.get_hist_data(code,start='2017-01-01',retry_count=10,pause=1)['p_change']
		return len(tmps[tmps>=9.99])
	except:
		print(code)

csvfile=open('d:\\ztb.csv','w',newline='')
writer=csv.writer(csvfile)
writer.writerow([u'板块名称',u'涨停板次数'])				
tmpdict={}
csv_reader=csv.reader(open('c:/industry_classified.csv'))
concept=set(row[3] for row in csv_reader)

for j in concept:
	if j!='c_name':
		tmp=set()
		cnt=0
		csv_reader=csv.reader(open('c:/industry_classified.csv'))
		tmp=set(row[1] for row in csv_reader if row[3]==j)
		for k in tmp:
			cnt=cnt+ztb(k)
		print(j,cnt)
		writer.writerow([j,cnt])