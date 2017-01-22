#-*- coding:utf-8 -*-
import json
from collections import Counter

path='d:/pydata-book-master/ch02/usagov_bitly_data2012-03-16-1331923249.txt'

records=[json.loads(line) for line in open(path)]
time_zones=[rec['tz'] for rec in records if 'tz' in rec]

def get_counts(sequence):
	counts={}
	for x in sequence:
		if x in counts:
			counts[x]=counts[x]+1
		else:
			counts[x]=1
	return counts
	
counts=get_counts(time_zones)
#print(counts['America/New_York'])
#print(len(time_zones))

def top_counts(count_dict,n=10):
	value_key_pairs=[(count,tz) for tz,count in count_dict.items()]
	value_key_pairs.sort()
	return value_key_pairs[-n:]
#print(top_counts(counts))

counts=Counter(time_zones)
#print(counts.most_common(10))

from pandas import DataFrame,Series
import pandas as pd;import numpy as np
frame=DataFrame(records)
#print(frame['tz'].value_counts())
clean_tz=frame['tz'].fillna('Missing')
clean_tz[clean_tz=='']='Unknown'
tz_counts=clean_tz.value_counts()
#print(tz_counts)
#print(clean_tz)

results=Series([x.split()[0] for x in frame.a.dropna()])
#print(results.value_counts()[:10])

unames=['user_id','gender','age','occupation','zip']
users=pd.read_table('D:/pydata-book-master/ch02/movielens/users.dat',sep='::',header=None,names=unames,engine='python')
rnames=['user_id','movie_id','rating','timestamp']
ratings=pd.read_table('D:/pydata-book-master/ch02/movielens/ratings.dat',sep='::',header=None,names=rnames,engine='python')
mnames=['movie_id','title','genres']
movies=pd.read_table('D:/pydata-book-master/ch02/movielens/movies.dat',sep='::',header=None,names=mnames,engine='python')
#print(users[:5])
#print(ratings[:5])
#print(movies[:5])

data=pd.merge(pd.merge(ratings,users),movies)
#print(data.head(5))
mean_ratings=pd.pivot_table(data, values='rating', index=['title'],columns=['gender'], aggfunc='mean')
print(mean_ratings.head(10))


