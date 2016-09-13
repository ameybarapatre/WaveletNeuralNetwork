import pandas as pd
from  datetime import *
import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing

i=0
traff = pd.read_csv('./data/easternexp.csv', sep=',')
traffic=traff.copy()

"""plots of data of one of the contributing roads of Eastern Express Highway before and after standardization"""
data = traffic.groupby(['CONTRI']).get_group(('Pokharan No 1 Road/Hutatma Maruti Kumar Path')).copy()[['TT','JF','CF']]
fig, axes = plt.subplots(nrows=1, ncols=2)
data.plot(ax=axes[0])
data_scaled = preprocessing.scale(data)
print(data_scaled.mean(axis=0),data_scaled.std(axis=0))

pd.DataFrame(data=data_scaled,index=data.index, columns=['TT', 'JF', 'CF']).plot(ax=axes[1])
plt.show()

""" Standardisation of data of each contributing road of Eastern Express Highway"""

for nm , grp in traffic.groupby(['ROAD','LI']).get_group(('Eastern Express Highway','502-03126')).groupby('CONTRI'):
    data=grp.copy()
    i=i+1
    data_scaled = preprocessing.scale(data[['TT','JF','CF']])

    scaled = pd.DataFrame(data=data_scaled,index=data.index, columns=['TT', 'JF', 'CF'])
    data['TT']=scaled['TT']
    data['JF']=scaled['JF']
    data['CF']=scaled['CF']
    print(data_scaled.std(axis=0),data_scaled.mean(axis=0))
    with open("stdin.csv", 'a') as f:
      data.to_csv(f, header=False)



