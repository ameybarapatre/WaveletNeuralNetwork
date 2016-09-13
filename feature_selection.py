from sklearn.ensemble import ExtraTreesClassifier
import pandas as pd
from  datetime import *
import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing
datain = pd.read_csv('./data/stdin.csv', sep=',')
dataout = pd.read_csv('./data/TJF.csv',sep=',')

data = datain.groupby(['CONTRI']).get_group(('Advokate Almeda Marg')).copy()
print(data.shape)
print(dataout.shape)

clf = ExtraTreesClassifier()
clf = clf.fit(data[['JF','SP']], np.asarray(dataout['JF'], dtype="|S6"))
print(clf.feature_importances_)