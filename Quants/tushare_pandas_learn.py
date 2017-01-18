import tushare as ts

hq = ts.get_today_all()
hq = hq[['code','name','changepercent','trade']]
mins = hq.trade>0.00
maxs = hq.trade<=5
allselect = mins & maxs 
data = hq[allselect].sort('trade')

code_list = []
for c in data['code']:
    #if c[0] != "0":
	code_list.append(c)

print(code_list)

#test
