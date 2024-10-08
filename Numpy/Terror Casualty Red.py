# Find the casualty in the Red Corridor States ? Mainly Red corridor states include Jharkhand, Odisha, Andhra Pradesh, and Chhattisgarh.
# Note: Casualty=Killed +Wounded
# Print count of Casualty as integer value.

import numpy as np
import csv
with open('terrorismData.csv',encoding="utf8") as file_obj:
    file_data = csv.DictReader(file_obj,skipinitialspace=True)
   
    state = []
    killed = []
    wounded = []
   
    for row in file_data:
        if row['Country'] == 'India':
            state.append(row['State'])
            killed.append(row['Killed'])
            wounded.append(row['Wounded'])
          
    np_state   = np.array(state)
    np_killed  = np.array(killed)
    np_wounded = np.array(wounded)   
    
    np_killed[np_killed == ''] = '0.0'
    np_wounded[np_wounded == ''] = '0.0'
       
    np_killed  = np.array(np_killed,dtype=float)
    np_killed  = np.array(np_killed,dtype=int)
    np_wounded = np.array(np_wounded,dtype=float)
    np_wounded = np.array(np_wounded,dtype=int)
    np_casualty = np_killed + np_wounded
    
    bool_red = (np_state == 'Jharkhand') | (np_state == 'Odisha') | (np_state == 'Andhra Pradesh') | (np_state == 'Chhattisgarh')
   
    np_cas_filter  = np_casualty[(bool_red)]
    cas_count = np.sum(np_cas_filter)
