# Given file "terrorismData.csv"
# It is an open-source database including information on terrorist attacks around the world from 1970 through 2017. This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period


import numpy as np
import csv
data = csv.DictReader(open('terrorismData.csv'), skipinitialspace=True)

day=[]
attack=[]
 
for row in data:
  attack.append(row['AttackType'])
  day.append(row['Day'])

np_day=np.array(day)
np_attack=np.array(attack)

np_day[np_day=='']='0'

np_day=np.array(np_day,dtype=float)
sum=0
for i in np_day:
  if int(i)<21 and int(i)>=10:
    sum=sum+1
print(sum)
