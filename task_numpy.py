import numpy as np

array = np.array([
    [43,42,45,34,23],
    [23,45,45,34,37],
    [37,38,39,40,45]
])

"""
               maths      english    malayalam      cs        social
vipin           43          42          45          34          23  
hari            23          45          45          34          37
cibin           37          38          39          40          45    

"""
# Display marks of hari
print(array[1])

# Display maths mark of hari
print(array[1,0])

# Display malayalam marks of all students
print(array[:,2])

# Display malayalam and cs marks of all students
print(array[:,2:4])

# Display english and malayalam marks of hari and cibin 
print(array[1:3,1:3])