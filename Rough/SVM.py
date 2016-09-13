import pandas as pd
from  datetime import *
import numpy as np
import time ,math
import matplotlib.pyplot as plt
from sklearn.svm import SVR
from sklearn.metrics import mean_squared_error
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

"""for nm , grp in traffic.groupby(['ROAD','LI']).get_group(('Eastern Express Highway','502-03126')).groupby('CONTRI'):
    grp['JF'].astype(float).plot()
    i=i+1
    print nm
plt.show()"""

diff = traffic.groupby(['ROAD','LI','CONTRI']).get_group(('Eastern Express Highway','502-03126','Pokharan No 1 Road/Hutatma Maruti Kumar Path'))['JF'][0:200].astype(float).copy()
time = traffic.groupby(['ROAD','LI','CONTRI']).get_group(('Eastern Express Highway','502-03126','Pokharan No 1 Road/Hutatma Maruti Kumar Path'))['TIME'][0:200].astype(float).copy()
traffic = traffic.set_index('TIME')

Y = np.atleast_1d(diff.as_matrix())
X = np.atleast_2d(time.as_matrix()).T

x = np.atleast_2d(np.linspace(0, 2000,20000)).T

svr_rbf = SVR(kernel='rbf', C=1e3, gamma=0.009)
y_rbf = svr_rbf.fit(X, Y).predict(x)

ds = np.gradient(y_rbf)
#print ds
#plt.plot(x, y_rbf ,label="SVM JF")
#plt.plot(x,ds,label="JF Gradient")

#traffic.groupby(['ROAD','LI','CONTRI']).get_group(('Eastern Express Highway','502-03126','Pokharan No 1 Road/Hutatma Maruti Kumar Path'))['JF'][0:200].astype(float).plot()

data = traffic.groupby(['ROAD','LI','CONTRI']).get_group(('Eastern Express Highway','502-03126','Pokharan No 1 Road/Hutatma Maruti Kumar Path')).copy()

data['TT'] =np.multiply(data['LEN'], np.divide(np.subtract(data['FS'],data['SP']) , np.multiply(data['FS'], data['SP'])))
dt = data['TT'].copy().as_matrix()
dt = [w*math.exp(5) for w in dt]
dt=dt[0:200]

svr_rbf_t = SVR(kernel='rbf', C=1e3, gamma=0.01)
y_rbf_t = svr_rbf_t.fit(X, dt).predict(x)
plt.plot(x,y_rbf_t,label="SVM Time ")
plt.plot(X,dt,label="Time")

#plt.plot(x,np.gradient(y_rbf_t),label="Time Gradient")
#og = traffic.groupby(['ROAD','LI','CONTRI']).get_group(('Eastern Express Highway','502-03126','Pokharan No 1 Road/Hutatma Maruti Kumar Path'))['JF'][0:200].astype(float).as_matrix()
#plt.plot(X,np.gradient(og))
#print len(ds),len(og)
#mean_squared_error(np.gradient(og), ds)
plt.legend(loc="best")
plt.show()
