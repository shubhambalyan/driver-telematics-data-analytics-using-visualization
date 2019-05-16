import csv
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import *
import scipy.spatial
from os import walk
from pandas import DataFrame

finalCsv2=np.zeros((547200,1), dtype=float)
avg_trn_spd_1s=np.zeros((200,1), dtype=float)

def unit_vector(vector):
    """ Returns the unit vector of the vector.  """
    return vector / np.linalg.norm(vector)

def angle_between(v1, v2):
    """ Returns the angle in radians between vectors 'v1' and 'v2'::

            >>> angle_between((1, 0, 0), (0, 1, 0))
            1.5707963267948966
            >>> angle_between((1, 0, 0), (1, 0, 0))
            0.0
            >>> angle_between((1, 0, 0), (-1, 0, 0))
            3.141592653589793
    """

    v1_u = unit_vector(v1)
    v2_u = unit_vector(v2)
    angle = np.arccos(np.dot(v1_u, v2_u))
    if np.isnan(angle):
        if (v1_u == v2_u).all():
            return 0.0
        else:
            return np.pi
    return angle
 
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
		df = pd.DataFrame(df)
		df2 = df[::2]
		df2 = np.array(df2)
		euc = np.zeros((len(df2),1), dtype=float)
		turn = np.zeros((len(df2),1), dtype=float)
		angle = np.zeros((len(df2),1), dtype=float)
		trn_spd = np.zeros((len(df2),1), dtype=float)
		toto=0
		j=0
		for toto in xrange(1,len(df2)):
			l=scipy.spatial.distance.euclidean(df2[toto-1:toto], df2[toto:toto+1])
			euc[toto]=round(l,2)
		for j in xrange(1,len(df2)-1):
			a=df2[j-1]
			b=df2[j]
			c=df2[j+1]
			v1 = b-a
			v2 = c-b
			
			
			#pangle = math.acos(dotproduct(v1, v2) / (length(v1) * length(v2)))
			#print pangle
			angle[j] = 180-(angle_between(tuple(v1), tuple(v2))*180/np.pi)
			if((angle[j]>0 and angle[j]<135) or (angle[j]>225 and angle[j]<360)):
				trn_spd[j] = (euc[j-1]+euc[j+1]+euc[j])/3


		z= len(np.where(trn_spd == 0)[0])
		avg_trn_spd_1s[i-1] = sum(trn_spd)/(len(trn_spd)-z)

	finalCsv2[yo:yo+200,0]=np.reshape(avg_trn_spd_1s, (200))
	
	yo=yo+200
	print opo

finalCsv2=pd.DataFrame(finalCsv2)
finalCsv2.to_csv("/home/sresht/Desktop/kaggle/drivers_eu/angle2.csv")