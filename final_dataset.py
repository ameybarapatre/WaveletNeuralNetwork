import pandas as pd
from  datetime import *
import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
"""Creates final data set by joining standardised input and corresponding target normalized output"""
i=0
traff = pd.read_csv('./data/stdin.csv', sep=',')
traffic=traff.copy()

for nm , grp in traffic.groupby(['ROAD','LI']).get_group(('Eastern Express Highway','502-03126')).groupby('CONTRI'):

    data=grp.copy()[['JF','CF','TT','TIME']]

    if i==0:
        total=data.copy()[['JF','CF','TT','TIME']]
        total = total.set_index(['TIME'])
    else :
        data = data.set_index(['TIME'])
        total = pd.concat([total,data], axis=1)
    i=i+1
    #with open('easternexp.csv', 'a') as f:
    #    data.to_csv(f, header=False)
    print(nm)
#print(total)
total =total.reset_index()
output = pd.read_csv('./data/stdout1.csv',sep=',')
total = pd.concat([total,output['JF']], axis=1)
print(total)
with open('dataset.csv', 'a') as f:
        total.to_csv(f, header=False)
