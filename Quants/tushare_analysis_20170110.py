#-*- coding:utf-8 -*-
import tushare as ts
import pandas as pd

tmp_df=ts.get_today_all()
hq_df=tmp_df[['code','name','changepercent','trade','volume','turnoverratio','amount','per','mktcap','nmc']]

mins=hq_df.trade>0.00
maxs=hq_df.trade<=5.00
maxnmc=hq_df.nmc<=780000

allselect = mins & maxs &maxnmc
data = hq_df[allselect]

code_list = []
for c in data['code']:
#	histdata=ts.get_hist_data(code=c,start='2014-12-01',end='2017-01-11')
	code_list.append(c)

print(code_list)
#sh_hist_data=ts.get_hist_data(code='sh',start='2014-12-01',end='2016-12-01')
#sh_hist_data=sh_hist_data[['open','high','close','low','volume','price_change','p_change']].sort_index()

#datelist = pd.date_range(pd.datetime.today(), periods=730).tolist()

