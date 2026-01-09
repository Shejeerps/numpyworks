import numpy as np

sales_report=np.array([
    [
        [10,11],
        [12,13]
    ],
    [
        [100,110],
        [120,130]

    ]
    ])

print(sales_report.ndim)
print(sales_report.shape)
print(sales_report[1,0,0])
sales_report[1,1,1]=14
print(sales_report)