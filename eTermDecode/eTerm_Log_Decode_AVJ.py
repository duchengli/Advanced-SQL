import csv

rawdatas=[]
results={}
dir1=''
date1=''
flt1=''
time1=''
ori=''
des=''
ac1=''

csvfile=open('d:\\fdl.csv','w',newline='')
writer=csv.writer(csvfile)
writer.writerow([u'Flt_Date',u'Flt_No',u'Dep',u'Arr',u'Aircraft',u'Seat','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'])

def cls_decode(cls_text):#按A-Z顺序输出
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
        if not (line.startswith('>PN') or line.startswith('>CP') or line.startswith('SID:') or line.startswith('>FDL') or line.startswith('----') or len(line)<=1):
            if not (line.strip().endswith('+') or line.strip().endswith('-')):
                rawdatas.append(line.strip())
            else:
                rawdatas.append(line.strip()[:-1])
                    
for k in range(len(rawdatas)):
    if len(rawdatas[k].strip().split(' '))>1:
        if rawdatas[k].strip().split()[1]=='LIST':
            dir1=rawdatas[k].strip().split()[0]
            date1=rawdatas[k].strip().split()[5]
            bgn1=k
            
            for n in range(k+2,k+100):
                if n>len(rawdatas)-1:
                    end1=n                    
                    break                    
                if len(rawdatas[n].strip().split(' '))>1:
                    if rawdatas[n].strip().split()[1]=='LIST':                        
                        end1=n
                        break
                if len(rawdatas[n])>12:
                    if rawdatas[n].strip().startswith('FLIGHT TOTAL'):
                        end1=n
                        break
                      
            for i in range(bgn1,end1):
                try:
                    if not rawdatas[i][1].isnumeric() and rawdatas[i][3:4].isnumeric():
                        #print(k,n,i,rawdatas[i])
                        if rawdatas[i][2]==' ':#三位航班号
                            flt1=rawdatas[i].strip().split()[0]+rawdatas[i].strip().split()[1]
                            time1=rawdatas[i].strip().split()[2]
                            ori=rawdatas[i].strip().split()[3].replace('+','')
                            des=rawdatas[i].strip().split()[4]
                            ac1=rawdatas[i].strip().split()[5]
                        else:
                            flt1=rawdatas[i].strip().split()[0]
                            time1=rawdatas[i].strip().split()[1]
                            ori=rawdatas[i].strip().split()[2].replace('+','')
                            des=rawdatas[i].strip().split()[3]
                            ac1=rawdatas[i].strip().split()[4]
                            #print(bgn1,end1,i,flt1,time1,ori,des,ac1)
                        #接着解析子仓位
                        fltc=rawdatas[i].strip().split()[-1]
                        alloc=fltc.split('//')[0]
                        if len(fltc.split('//'))>1:
                            cls=fltc.split('//')[1]                            
                            if not rawdatas[i].strip().endswith('//'):                        
                                for p in range(i,i+4):#子仓位分多行列示时需要进行合并
                                    if not rawdatas[p].strip().endswith('//') and p>i and len(rawdatas[p].strip().split('/'))>0:
                                        cls=cls+rawdatas[p].strip().split()[-1]
                                    if rawdatas[p].strip().endswith('//'):
                                        if cls!=rawdatas[p].strip().split()[-1]:
                                            cls=cls+rawdatas[p].strip().split()[-1]
                                            break
                                    
                        results[(date1,flt1,ori,des)]=[ac1,alloc,cls]
                        #接着处理经停航班
                        for q in range(i+1,i+6):
                            if (not rawdatas[q][1].isnumeric()) and rawdatas[q][2:5].isnumeric():
                                break
                            if rawdatas[q][3]==" " and rawdatas[q][7:9]=="  " and (not rawdatas[q][0].isnumeric()):
                                ori=rawdatas[q].strip().split()[0]
                                des=rawdatas[q].strip().split()[1]
                                ac1=rawdatas[q].strip().split()[2]
                                fltc=rawdatas[q].strip().split()[-1]
                                alloc=fltc.split('//')[0]
                                if len(fltc.split('//'))>1:
                                    cls=fltc.split('//')[1]
                                    if not rawdatas[q].strip().endswith('//'):
                                        for r in range(q,q+4):
                                            if not rawdatas[r].strip().endswith('//') and r>q and len(rawdatas[r].strip().split('/'))>0:
                                                cls=cls+rawdatas[r].strip().split()[-1]
                                            if rawdatas[r].strip().endswith('//'):
                                                if cls!=rawdatas[r].strip().split()[-1]:
                                                    cls=cls+rawdatas[r].strip().split()[-1]
                                                    break
                            results[(date1,flt1,ori,des)]=[ac1,alloc,cls]                
                        
                except:
                    print(str(i)+' row is error')
                    print(bgn1,end1,dir1,date1,flt1,time1,ori,des)
                    continue

for result in results:
    tmp_list=[]
    tmp_list=[result[0],result[1],result[2],result[3],results[result][0],results[result][1]]
    for sub_class in cls_decode(results[result][2]):
        tmp_list.append(sub_class)
    #print(tmp_list)    
    writer.writerow(tmp_list)
csvfile.close()
                    
                    
                    
                     
                        
                        
                    
        
    
    


    
