import numpy as np
full_array=np.full((5,5),4)
print(full_array)

ones_array=np.ones((3,3),"int")
print(ones_array)

ones_array[1,1]=100
print(ones_array)

full_array[1:4,1:4]=ones_array
print(full_array)