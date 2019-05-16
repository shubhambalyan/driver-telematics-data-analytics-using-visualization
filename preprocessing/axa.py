import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import *
import scipy.spatial
from os import walk

avg_speed=np.zeros((200,1), dtype=float)
finalCsv=np.zeros((547200,7), dtype=float)
max_speed=np.zeros((200,1), dtype=float)
acc_1s=np.zeros((200,1), dtype=float)
acc_2s=np.zeros((200,1), dtype=float)
dacc=np.zeros((200,1), dtype=float)
count=0

f = []
for (dirpath, dirnames, filenames) in walk("/home/sresht/Desktop/kaggle/drivers"):
    f.extend(dirnames)
    break

for i in range(len(f)):
	f[i]=int(f[i])

yo = 0
f = np.sort(f)
f=np.array(f)

for opo in f:
	i=0
	for i in xrange(1,201):
		a="/home/sresht/Desktop/kaggle/drivers/"+str(opo)+"/"+str(i)+".csv"
		df=pd.read_csv(a,sep=',')
		df = np.array(df)
		euc = np.zeros((len(df),1), dtype=float)
		acc_1=np.zeros((len(df),1), dtype=float)
		acc_2=np.zeros((len(df),1), dtype=float)
	   	for j in xrange(1,len(df)):
			l=scipy.spatial.distance.euclidean(df[j-1:j], df[j:j+1])
			euc[j]=round(l,2)
		df=c_[df,euc]


		for k in xrange(1, len(df)):
			t=df[k,2]-df[k-1,2]
			acc_1[k]=t 
		df=c_[df,acc_1]

		for m in xrange(2, len(df)):
			t=df[m,2]-df[m-2,2]
			acc_2[m]=t 	

		df=c_[df,acc_2]
		df=pd.DataFrame(df)

		acc_tot_2=np.zeros((len(df),1), dtype=float)
		acc_tot_1=np.zeros((len(df),1), dtype=float)
		dacc_tot=np.zeros((len(df),1), dtype=float)
		p=0
		we=0
		oo=0
		
		for gg in xrange(1,len(df)):
			if(euc[gg]!=0 and euc[gg-1]==0):
				acc_tot_1[p]=acc_1[gg]
				acc_tot_2[we]=acc_2[gg]
				p=p+1
				we=we+1

		for dd in xrange(0,len(df)-1):
			if(euc[dd]!=0 and euc[dd+1]==0):
				dacc_tot[oo]=acc_1[dd]
				oo=oo+1
			
		
		op = sum(acc_tot_1[:p])
		accc1=float(sum(acc_tot_1[:p]))/float(p)
		accc2=float(sum(acc_tot_2[:we]))/float(we)
		daccc=float(sum(dacc_tot[:oo]))/(float(oo)+1)
		z= len(np.where(euc == 0)[0])
		
		avg_speed[i-1] = sum(euc)/(len(euc)-z)
		max_speed[i-1] = max(euc)
		acc_1s[i-1] = float(accc1)
		acc_2s[i-1] = float(accc2)
		dacc[i-1]= float(daccc)
		

	finalCsv[yo:yo+200,0]=opo
	finalCsv[yo:yo+200,1]=range(1,201)
	finalCsv[yo:yo+200,2]=np.reshape(avg_speed, (200))
	finalCsv[yo:yo+200,3]=np.reshape(max_speed, (200))
	finalCsv[yo:yo+200,4]=np.reshape(acc_1s, (200))
	finalCsv[yo:yo+200,5]=np.reshape(acc_2s, (200))
	finalCsv[yo:yo+200,6]=np.reshape(dacc, (200))

	yo=yo+200
	print opo



finalCsv=pd.DataFrame(finalCsv)
finalCsv.to_csv("/home/sresht/Desktop/kaggle/drivers_eu/finalCsv.csv")