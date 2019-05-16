from sklearn.cluster import KMeans
import pandas as pd
import numpy as np
import random
import sklearn
from pylab import *

#np.random.seed(42)
a="/Desktop/Project/cluster_data.csv"
df=pd.read_csv(a,sep=',')
data_array = np.array(df)
data_array=data_array[:-1,:][277600:277800]
#attri=len(data_array[:-1,:][0])
#random.seed(1234)
kk=KMeans(n_clusters=2)
kk.fit(data_array)
label=kk.labels_
v=kk.cluster_centers_
plot(label, 'ro')
show()
