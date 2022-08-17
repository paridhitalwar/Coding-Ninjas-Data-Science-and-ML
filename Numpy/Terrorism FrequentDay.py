# Find the most frequent day of attack in a terrorismDataset ?
# Note: Here np.unique can be used.
# Print count of frequent day and number of attack as Integer value.
import csv
import numpy as np
with open("terrorismData.csv",encoding="utf8") as file_obj:
    file_data=csv.DictReader(file_obj,skipinitialspace=True)
    attack=[]
    for row in file_data:
        attack.append(row['Day'])
    attack=np.array(attack,dtype=int)
    a,counts=np.unique(attack,return_counts=True)
    x=counts.argmax()
    print(a[x],counts[x])
