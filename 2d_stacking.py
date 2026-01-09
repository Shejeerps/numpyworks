import numpy as np
two_dimensional_array1=[
    [1,2],
    [3,4]
]

two_dimensional_array2=[
    [10,20],
    [30,40]
]

v_stack=np.vstack((two_dimensional_array1,two_dimensional_array2))
print(v_stack)

h_stack=np.hstack((two_dimensional_array1,two_dimensional_array2))
print(h_stack)