import numpy as np

# np.loadtext(file_path,delimeter=,skiprows=,datatype)

data=np.loadtxt("sales_data\\sales.csv",delimiter=",",skiprows=1,dtype=str)
print(data)

#total_units_sold

unit_sold=data[:,3].astype("int")
print(np.sum(unit_sold),"total units sold")

print(np.max(unit_sold),"maximum units sold")

print(np.min(unit_sold),"minimum units sold")

print(np.average(unit_sold),"average units sold")

revenue=data[:,3].astype("int")*data[:,4].astype("int")
print(revenue)

total_revenue=np.sum(revenue)
print(total_revenue,"total revenue")

#unit sold > 8

print(data[data[:,3].astype("int")>8])
      
# category == electronics

print("electronics",data[data[:,2]=="Electronics"])

# product discount 100 rs

data[:,4]=data[:,4].astype("int")-100
print("discount_price",data)

# total revenue of north
sales_report_north_region=data[data[:,-1]=="North"]
print("north_report",sales_report_north_region)

revenue_north=data[:,-1]
print(revenue_north)

total_revenue_north=np.sum(revenue_north)
print(total_revenue_north,"total revenue of north")


