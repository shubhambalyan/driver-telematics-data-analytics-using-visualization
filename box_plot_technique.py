import pandas as pd
import csv
from pylab import *
import numpy as np

lol=np.zeros((547200,1), dtype=float)
a="/Desktop/Project/final.csv" #file-location
df=pd.read_csv(a,sep=',')
max_speed = df['max_speed']
acc_1s = df['acc_1s']
acc_2s = df['acc_2s']
dacc = df['dacc']
trn_spd = df['trn_spd_1']
trn_spd_2 = df['trn_spd_2']
avg_speed = df['avg_speed']

trn_spd = np.array(trn_spd)
max_speed = np.array(max_speed)
acc_1s = np.array(acc_1s)
acc_2s = np.array(acc_2s)
dacc = np.array(dacc)
trn = np.array(trn_spd_2)
avg_speed = np.array(avg_speed)

trn_spd_1 = avg_speed
l = avg_speed[277600:277800]
plot(l, 'ro')
show()
co = 0
ll=20
hh=80
while (co<547200):
	l=np.percentile(trn_spd_1[co:co+200], ll)
	h=np.percentile(trn_spd_1[co:co+200], hh)
	iqr = np.zeros(((200),1), dtype=float)
	oiqr = np.zeros(((200),1), dtype=float)
	piqr = np.zeros(((200),1), dtype=float)
	j=0
	t=0
	m=0
	for i in range(len(trn_spd_1[co:co+200])):
		if(l<trn_spd_1[i] and trn_spd_1[i]<h):
			iqr[i]=1
			t=t+1
		elif (l-(1.5*(h-l))<trn_spd_1[i] and trn_spd_1[i]<l) or (h+(1.5*(h-l))<trn_spd_1[i] and trn_spd_1[i]<h):
			iqr[i]=2
			j=j+1
		else:
			iqr[i]=0
			m=m+1

	lol[co:co+200,0] =np.reshape(iqr, (200))
	co = co+200
