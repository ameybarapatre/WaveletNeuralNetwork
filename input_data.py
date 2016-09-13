import pandas as pd
from  datetime import *
import time
import matplotlib.pyplot as plt
import numpy as np

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
for nm , grp in traffic.groupby(['ROAD','LI']).get_group(('Eastern Express Highway','502-03126')).groupby('CONTRI'):
    grp['JF'].astype(float).plot()
    data=grp.copy();
    i=i+1
    """Calculating time taken to cover the road at current speed """
    data['TT'] = np.divide(data['LEN'], data['SP'])
    with open('easternexp.csv', 'a') as f:
        data.to_csv(f, header=False)

plt.show()


