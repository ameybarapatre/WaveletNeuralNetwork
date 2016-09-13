import numpy as np
x = np.array([[0, 1], [0, 5], [0, 2], [0, 3]])
x = x[:,np.newaxis,:]
print(x)

y = np.array([[1, 1], [1, 2], [1, 3], [1, 4]])
y =y[np.newaxis,:,:]
print(y)
z= np.array([[1, 1], [2, 2], [3, 3], [4, 4]])

print('ans')
o = np.subtract(x,y)
print(o)
print('div')
print(np.divide(o,z))
print('prod')
print(np.prod(np.divide(o,z),axis=2))