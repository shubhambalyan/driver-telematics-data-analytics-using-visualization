import numpy as np
import pandas as pd
from scipy import *
import scipy.spatial
from os import walk

finalCsv2=np.zeros((547200,1), dtype=float)
acc_1s=np.zeros((200,1), dtype=float)

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
		df = np.array(df[::1])
		euc = np.zeros((len(df),1), dtype=float)
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
			
		acc_tot_1=np.zeros((len(df),1), dtype=float)

		for gg in xrange(1,len(df)):
			if(euc[gg]!=0 and euc[gg-1]==0):
				acc_tot_1[p]=acc_1[gg]
				p=p+1

		accc1=float(sum(acc_tot_1[:p]))/float(p)

		acc_1s[i-1] = float(accc1)
		
	finalCsv2[yo:yo+200,0]=np.reshape(acc_1s, (200))
	
	yo=yo+200
	print opo

finalCsv2=pd.DataFrame(finalCsv2)
finalCsv2.to_csv("/home/sresht/Desktop/kaggle/drivers_eu/acc_2s.csv")