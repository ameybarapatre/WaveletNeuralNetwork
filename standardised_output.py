import pandas as pd
from  datetime import *
import time
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing

i=0
traff = pd.read_csv('./data/TJF.csv', sep=',')
traffic=traff.copy()
""" Normalizing Jamfactor to 0 to 1 range"""
def normalize(dt):
    return dt/10
traffic['JF']= traffic['JF'].apply(normalize)

plt.show()


with open("stdout1.csv", 'w') as f:
    traffic.to_csv(f, header=False)


