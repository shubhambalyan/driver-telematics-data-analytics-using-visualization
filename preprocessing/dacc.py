import numpy as np
import pandas as pd
from scipy import *
import scipy.spatial
from os import walk

finalCsv2=np.zeros((547200,1), dtype=float)
deacc=np.zeros((200,1), dtype=float)

f = []
for (dirpath, dirnames, filenames) in walk("/home/sresht/Desktop/kaggle/drivers"):
    f.extend(dirnames)
    break

for i in range(len(f)):
	f[i]=int(f[i])

yo = 0
f = np.sort(f)
f=np.array(f)

yo = 0

for opo in f:
	i=0 
	for i in xrange(1,201):
		a="/home/sresht/Desktop/kaggle/drivers/"+str(opo)+"/"+str(i)+".csv"
		df=pd.read_csv(a,sep=',')
		df = np.array(df)
		euc = np.zeros((len(df),1), dtype=float)
		dacc_tot=np.zeros((len(df),1), dtype=float)
		acc_1=np.zeros((len(df),1), dtype=float)

	   	for j in xrange(1,len(df)):
			l=scipy.spatial.distance.euclidean(df[j-1:j], df[j:j+1])
			euc[j]=round(l,2)
		df=c_[df,euc]
		p=0
		we=0
		oo=0

		for k in xrange(1, len(df)):
			t=df[k,2]-df[k-1,2]
			acc_1[k]=t 
		df=c_[df,acc_1]


		for dd in xrange(0,len(df)-1):
			if(euc[dd]!=0 and euc[dd+1]==0):
				dacc_tot[oo]=acc_1[dd]
				oo=oo+1

		accc1=float(sum(dacc_tot[:oo]))/(float(oo)+1)

		deacc[i-1] = float(accc1)
		
	finalCsv2[yo:yo+200,0]=np.reshape(deacc, (200))
	
	yo=yo+200
	print opo

finalCsv2=pd.DataFrame(finalCsv2)
finalCsv2.to_csv("/home/sresht/Desktop/kaggle/drivers_eu/dacc.csv")