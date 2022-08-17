# It is an open-source database including information on terrorist attacks around the world from 1970 through 2017. This dataset includes systematic data on domestic as well as international terrorist incidents that have occurred during this time period
# Find the number of attack held between 1 Jan 2010 and 31 Jan 2010?(including both date).
# Note Ignore the case where day is 0
# Print count of NumberOFAttack as integer value.

import numpy as np
import csv

day = []
with open('terrorismData.csv',encoding='ISO-8859-1') as data:
    reader = csv.DictReader(data)
    for row in reader:
        if row['Year'] is not None and row['Year'] != '' and int(row['Year']) == 2010:
            if row['Month'] is not None and row['Month'] != '' and int(row['Month']) ==1:
                if row['Day'] is not None and row['Day'] != '' and int(row['Day']) >=1 and int(row['Day']) <= 31:
                    day.append(row)
    print(np.count_nonzero(day))
