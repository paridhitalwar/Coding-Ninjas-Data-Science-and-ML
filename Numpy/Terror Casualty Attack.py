# As we knew the Kargil ( in Jammu and Kashmir) War that took place between May 1999 and July 1999 (3 Months) ,so there was a huge conflict in Kashmir Valley during this period.
# In this dataset, there is no information regarding the war between the two countries to find out the casualty during the war.
# So find out the attack in this period in which maximum casualties happened.
# Print the count of casualties (as integer), city in which that attack happened and name of attack group.
# Note : Casualty = Killed + Wounded.Fill the empty value in killed or wounded feature to 0.

import numpy as np
import csv

with open('terrorismData.csv','r',encoding="utf8") as obj:
    file_data = csv.DictReader(obj,skipinitialspace = True)
    
    killed = []
    wounded = []
    month = []
    city = []
    group=[]
    for row in file_data:
        if row['Country'] == 'India' and row['Year'] == '1999' and row['State'] == 'Jammu and Kashmir':
            killed.append(row['Killed'])
            wounded.append(row['Wounded'])
            month.append(row['Month'])
            city.append(row['City'])
            #print(row)
            group.append(row['Group'])
            
np_killed = np.array(killed)
np_wounded = np.array(wounded)
np_month = np.array(month,dtype = int)
np_city = np.array(city)
np_group = np.array(group)
