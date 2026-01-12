import numpy as np

# np.where(condition,true_value,false_value)

ages=np.array([19,20,21,18,23,25])

print(np.where(ages>=20,"adults","teen"))

# task1
# print[even,odd,even.odd....]

array=np.array([2,3,4,5,6,7,8])

print(np.where(array%2==0,"even","odd"))

#task2
# print[+ve,-ve,+ve,-ve...]

array=np.array([-1,2,3,-4,5,6])

print(np.where(array>0,"+ve","-ve"))