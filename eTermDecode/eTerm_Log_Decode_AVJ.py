import csv
from datetime import  *  
import time 

rawdatas=[]
results={}
dir1=''
date1=''
flt1=''
time1=''
ori=''
des=''
ac1=''

csvfile=open('d:\\AVJ.CSV','w',newline='')
writer=csv.writer(csvfile)
writer.writerow([u'Flt_Date',u'Flt_No',u'Dep',u'Arr',u'Aircraft','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])

def cls_decode(cls_text):
	cls_inf=[]
	for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
		tmp_pax=0
		for cls_pax in cls_text.strip().split('/'):
			if len(cls_pax)!=0:
				if char==cls_pax[0]:
					tmp_pax=tmp_pax+int(cls_pax[1:])
		cls_inf.append(tmp_pax)
	return cls_inf     

fhand=open('c:\eTerm3\MYLOG.LOG')
for line in fhand:
	if not line.startswith('                                                                                '):
		if not (line.upper().startswith('>PN') or line.startswith('>CP') or line.startswith('SID:') or line.upper().startswith('>AVJ') or line.startswith('----') or len(line)<=1 or line.startswith('**NO') or line.strip().startswith('**') or line.startswith(time.strftime('%Y',time.localtime(time.time())))):
			rawdatas.append(line.strip())

for rawdata in rawdatas:
	if not rawdata[-6:].isdigit() and not (' ' in rawdata[-6:]):
		print(rawdata)
            