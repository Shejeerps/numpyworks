import numpy as np

prices=np.array([100,250,400,500])

discount_prices= prices*50/100
print(discount_prices)

new_prices=prices*150/100
print(new_prices)


arr1=np.array([[1,2],
               [3,4]])
arr2=np.array([[10,20],
               [30,40]])
print(arr1+arr2)