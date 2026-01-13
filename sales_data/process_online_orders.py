import numpy as np

data=np.loadtxt("sales_data\\online_orders.csv",delimiter=",",skiprows=1,dtype=str)
print(data)

print("Shape of dataset:", data.shape)

#1 Total number of orders
total_orders = data.shape[0]
print("Total Orders:", total_orders)

#2️ Average unit price
unit_price = data[:, 4].astype(int)
avg_unit_price = np.average(unit_price)
print("Average Unit Price:", avg_unit_price)

#3️ Total revenue per order

quantity = data[:, 3].astype(int)
unit_price = data[:, 4].astype(int)
discount = data[:, 5].astype(int)

discount_per_order= quantity * unit_price * discount/100
print("discount per order:\n", discount_per_order)

revenue_per_order=data[:,4].astype(int)-discount_per_order
print("revenue per order :\n",revenue_per_order)