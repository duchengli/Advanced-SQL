import csv
import re
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
writer.writerow([u'Flt_No',u'Flt_Date',u'Seg',u'STD',u'STA',u'Aircraft','P','F','A','O','G','E','Y','B','M','U','H','Q','V','W','S','T','L','X','N','K'])

def cls_decode(cls_text):
	cls_inf=[]
	tmp_status=[]
	for char in 'PFAOGEYBMUHQVWSTLXNK':
		for cls_status in cls_text.strip().split():
			if len(cls_status)!=0:
				if char==cls_status[0]:
					tmp_status=cls_status[1]
		cls_inf.append(tmp_status)
	return cls_inf     

fhand=open('c:\eTerm3\MYLOG.LOG')
for line in fhand:
	if not line.startswith('                                                                                '):
		if not (line.upper().startswith('>PN') or line.startswith('>CP') or line.startswith('SID:') or line.upper().startswith('>AVJ') or line.startswith('----') or len(line)<=1 or line.startswith('**NO') or line.strip().startswith('**') or line.startswith(time.strftime('%Y',time.localtime(time.time())))):
			rawdatas.append(line.strip())

for k in range(len(rawdatas)):
	if not rawdatas[k][-6:].isdigit() and not (' ' in rawdatas[k][-6:]):
		bgn1=k
		flt_no=rawdatas[k].strip().split()[0]
		
		for n in range(k+1,k+100):
			if n>len(rawdatas)-1:
				end1=n
				break
			if not rawdatas[n][-6:].isdigit() and not (' ' in rawdatas[n][-6:]):
				end1=n
				break
		#print(bgn1,end1)
		for i in range(bgn1+1,end1-1):
			try:
				if len(rawdatas[i])>=40:
					if re.search('^\d+\s+',rawdatas[i]):#前面有1,2,3等编号的航段
						flt_date=rawdatas[i].strip().split()[1]
						seg=rawdatas[i].strip().split()[2]
						std=rawdatas[i].strip().split()[3]
						sta=rawdatas[i].strip().split()[4]
						arc=rawdatas[i].strip().split()[5]
					else:#前面没有1,2,3等航段编号的航段
						flt_date=rawdatas[i].strip().split()[0]
						seg=rawdatas[i].strip().split()[1]
						std=rawdatas[i].strip().split()[2]
						sta=rawdatas[i].strip().split()[3]
						arc=rawdatas[i].strip().split()[4]
					#print([flt_no,flt_date,seg,std,sta,arc])
					if re.search('(\S\S\s){3,}',rawdatas[i]).group()[0]=='^':
						cls=re.search('(\S\S\s){3,}',rawdatas[i]).group()[3:]
					else:
						cls=re.search('(\S\S\s){3,}',rawdatas[i]).group()
					
					for p in range(i+1,min(i+3,len(rawdatas))):
						if len(rawdatas[p])<=20:
							cls=cls+rawdatas[p]
					#print([flt_no,flt_date,seg,std,sta,arc,cls])
					results[(flt_no,flt_date,seg)]=[std,sta,arc,cls]
			except:
				print(['Error!',i])

for result in results:
	tmp_list=[]
	tmp_list=[result[0],result[1],result[2],results[result][0],results[result][1],results[result][2]]
	for sub_class in cls_decode(results[result][3]):
		if sub_class==[] or sub_class=='S' or sub_class=='Q' or sub_class=='L':
			tmp_list.append('')
		else:
			tmp_list.append(sub_class)
	writer.writerow(tmp_list)
csvfile.close()



			
            