import numpy as np

data=np.genfromtxt("titanic_case_study\\passenger_data.csv",delimiter=",",skip_header=1,filling_values=0,dtype="str")

#total number of passengers

print(data.shape)

# total number of survivals

survivals=data[:,1]
print(survivals)

count_of_survivals=np.sum(survivals=="1")
print("total survived",count_of_survivals)

# total number of death
count_of_death=np.sum(survivals=="0")
print("total death",count_of_death)

# survival rate

survived_unsurvived=data[:,1].astype("int")
survived=survived_unsurvived[survived_unsurvived==1]
print(f"total number of survived{survived.size}")
survival_rate=(survived.size/survived_unsurvived.size)*100
print(f"surrvived rate={survival_rate}")

survival_rate=np.average(count_of_survivals)
print("survived rate = ",survival_rate)

death_rate=np.average(count_of_death)
print("death rate =",death_rate)

# total number of males

gender=data[:,3]
print("total genders=",gender)

total_males=np.sum(gender=="male")
print("total male ",total_males)

total_females=np.sum(gender=="female")
print("total female",total_females)

survived_males=data[(data[:,3]=="male")&(data[:,1].astype("int")==1)]
total_survived_males=np.sum(survived_males=="1")
print("survived males ",total_survived_males)
survived_males_rate=(total_survived_males/total_males)*100
print("survived male rate  ",survived_males_rate)

survived_females=data[(data[:,3]=="female")&(data[:,1].astype("int")==1)]
total_survived_females=np.sum(survived_females=="1")
print("total survived females ",total_survived_females)
survived_females_rate=(total_survived_females/total_females)*100
print("survived female rate ",survived_females_rate)

# ages max,min,avr
ages=data[:,4].astype("int")
print("maximum age ",np.max(ages))
print("minimum age ",np.min(ages))
print("average of ages ",np.average(ages))

#fare max,min,avr

fares=data[:,-2].astype("float")
print("maximum fare ",np.max(fares))
print("minimum fare ",np.min(fares))
print("average of fares ",np.average(fares))

#sort by fare (np.argsort())

print(data[np.argsort(data[:,-2].astype("float"))])

