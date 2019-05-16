import numpy as np
import pandas as pd
from scipy import *
import scipy.spatial
from os import walk

finalCsv2=np.zeros((547200,1), dtype=float)
max_speed=np.zeros((200,1), dtype=float)

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
		
	   	for j in xrange(1,len(df)):
			l=scipy.spatial.distance.euclidean(df[j-1:j], df[j:j+1])
			euc[j]=round(l,2)
		df=c_[df,euc]
		p=0
		we=0
		oo=0
			
		max_speed[i-1] = max(euc)
		
	finalCsv2[yo:yo+200,0]=np.reshape(max_speed, (200))
	
	yo=yo+200
	print opo

finalCsv2=pd.DataFrame(finalCsv2)
finalCsv2.to_csv("/home/sresht/Desktop/kaggle/drivers_eu/max_speed.csv")