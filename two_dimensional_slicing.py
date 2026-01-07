import numpy as np
array=np.array([
    [33,31,27],
    [31,30,29],
    [33,32,34]
])

print(array.ndim)
print(array.size)
print(array.shape)

#fetch 0 th row
print(array[0])

#fetch 1st row
print(array[1])

#slicing row
#fetch 1st and 2nd row
print(array[0:2])

#fetch 0th colomn and 1st colomn
print(array[:,0:2])

#fetch 1st colomn only
print(array[:,1:2])

#fetch 0th and 2nd row
print(array[::2])#[start:stop:step]

print(array[1:3,1:3])

print(array[2,1])