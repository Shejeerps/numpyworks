import numpy as np

leads = np.array([
    # s  m    t  w   th
    [12, 18, 10, 15, 5],   # facebook
    [20, 25, 22, 18, 8],   # insta
    [18, 30, 25, 22, 10],  # youtube
    [25, 28, 30, 26, 12],  # refferal
    [30, 35, 28, 32, 15],  # walkin
    [40, 45, 38, 40, 20],  # reddit
    [35, 50, 42, 45, 25]   # camp
    
])


# total leads generated each days

print(np.sum(leads,axis=0))

# total leads from each sources

print(np.sum(leads,axis=1))

# highest lead day

daywise_total=np.sum(leads,axis=0)
print(np.argmax(daywise_total))

# average leads per source

print(np.average(leads,axis=1))

# average leads per day

print(np.average(leads,axis=0))

# highest lead source

sourcewise_total=np.sum(leads,axis=1)
print(np.argmax(sourcewise_total))



