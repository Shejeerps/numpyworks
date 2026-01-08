# array creation method
# np.array()
# np.zeros(())
# np.ones(())
# np.full(())
# np.random.rand()
# np.random.randint(low,high,(size))

import numpy as np

zeros_array=np.zeros((3,4),"int")
print(zeros_array)

ones_array=np.ones((2,4),"int")
print(ones_array)

seven_array=np.full((7,7),7)
print(seven_array)

random_array=np.random.rand(4,5)
print(random_array)

random_int_array=np.random.randint(1,30,(4,4))
print(random_int_array)