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
print(clean_tz)
	

