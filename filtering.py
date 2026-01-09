import numpy as np

productivity = np.array([
    [8, 7, 8, 6, 7, 8, 9, 8, 7, 8],
    [6, 7, 6, 7, 6, 7, 8, 7, 6, 7],
    [9, 8, 9, 8, 9, 9, 8, 9, 8, 9],
    [5, 6, 5, 6, 5, 6, 6, 5, 6, 5],
    [7, 8, 7, 8, 7, 8, 7, 8, 7, 8],
    [8, 9, 8, 9, 8, 9, 8, 9, 8, 9]
])

print(productivity[productivity<7])

#working hours between 5 to 7
print(productivity[(productivity>=5) & (productivity<=7)])

# print working hours of first employee working hour <8

first_employee_working_hours=productivity[:,0]
print(first_employee_working_hours)

print(first_employee_working_hours[first_employee_working_hours<8])

#print last two employees working hours <7

last_two_employee_working_hour=productivity[:,8:10]
print(last_two_employee_working_hour)

print(last_two_employee_working_hour[last_two_employee_working_hour<7])

# print lessthan 8 value is 0

productivity[productivity<8]=0
print(productivity)
