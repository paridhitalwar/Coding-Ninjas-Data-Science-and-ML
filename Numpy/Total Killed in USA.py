# Given file "terrorismData.csv"
# It is an open-source database including information on terrorist attacks around the world from 1970 through 2017. This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period
# Problem Statement :
# Find total number of people killed from USA?
# Note: Some columns of killed are empty so replace them by 0.
# Print count of Killed as integer value.

import numpy as np
import csv
data = csv.DictReader(open('terrorismData.csv'), skipinitialspace=True)
killed=[]
usa=[]
country=[]
for row in data:
  killed.append(row['Killed'])
  country.append(row['Country'])

np_killed=np.array(killed)
np_country=np.array(country)
np_killed[np_killed=='']='0'

bool_arr = np_country == 'United States'

ans=np_killed[bool_arr]
ans=np.array(ans,dtype=float)
for i in ans:
    total=np.sum(ans)
print(int(total))
