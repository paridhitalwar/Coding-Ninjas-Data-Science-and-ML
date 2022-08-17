# Find top 5 Indian Cities which has most number of casualties ?
# Print top 5 cities along with total casualties in that city. Print count of Casualty as integer value.
# Note: Ignoring the City which is Unknown.
# Casualty = Killed + Wounded.

import numpy as np
import csv
with open('terrorismData.csv',encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj,skipinitialspace=True)
   
    city = []
    killed = []
    wounded = []
   
    for row in file_data:
        if row['Country'] == 'India' and row['City'] != 'Unknown':
            city.append(row['City'])
            killed.append(row['Killed'])
            wounded.append(row['Wounded'])
          
    np_city   = np.array(city)
    np_killed  = np.array(killed)
    np_wounded = np.array(wounded)   
    
    np_killed[np_killed == ''] = '0.0'
    np_wounded[np_wounded == ''] = '0.0'
       
    np_killed  = np.array(np_killed,dtype=float)
    np_killed  = np.array(np_killed,dtype=int)
    np_wounded = np.array(np_wounded,dtype=float)
    np_wounded = np.array(np_wounded,dtype=int)
    np_casualty = np_killed + np_wounded
    
    np_city_u   = np.unique(np_city)
    cas_u    = []
    for ind_city in np_city_u:
        tot_cas = np.sum(np_casualty[(np_city == ind_city)])
        cas_u.append(tot_cas)
    np_cas_u    = np.array(cas_u)
    ind = np_cas_u.argsort()
    ind = ind[::-1]
    ind = ind[:5]
    for i in ind:
        print(np_city_u[i],np_cas_u[i])
