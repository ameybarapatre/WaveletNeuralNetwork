import pandas as pd
from  datetime import *
import time
import numpy as np
import matplotlib.pyplot as plt

i=0
traff = pd.read_csv('anndata.csv', sep=',', parse_dates=['TIME'], dayfirst=True)
traffic=traff[:6255].copy()
def minutes(dt):

    fmt = '%Y-%m-%d %H:%M:%S'
    d1 = datetime.strptime('2016-06-11 10:12:02', fmt)
    d2 = datetime.strptime(str(dt), fmt)

    d1_ts = time.mktime(d1.timetuple())
    d2_ts = time.mktime(d2.timetuple())

    return int(d2_ts - d1_ts) / 60

traffic['TIME']= traffic['TIME'].apply(minutes)
traffic = traffic.set_index('TIME')

data = traffic.groupby(['CONTRI','LI']).get_group(('Cadbury Company Chowk/Eastern Express Highway','502+03206')).copy()
data['JF'].astype(float).plot()
with open('TJF.csv','a') as f :
    data.to_csv(f,header=False)
plt.show()