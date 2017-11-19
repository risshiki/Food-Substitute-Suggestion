
import numpy as np
from csv import DictReader
import csv


with open("Dataset.csv") as f:
    X = [row["Fats"] for row in DictReader(f)]

f.close()


with open("Dataset.csv") as f:
    Y = [row["Carbohydrates"] for row in DictReader(f)]

f.close()

with open("Dataset.csv") as f:
    Z = [row["Protein"] for row in DictReader(f)]

f.close()



X = [float(i) for i in X]  
Y = [float(i) for i in Y]
Z = [float(i) for i in Z]
final_clusters = []
for i in range(0,len(X)):
    final_clusters.append(int(X[i]//4 * 108 + Y[i]//9*10 + Z[i]//9))

check_val = set(final_clusters)
print(len(final_clusters))
##print(min(final_clusters))
##print(max(final_clusters))
##print(len(check_val))

header = ["Food Item","Type","Category","Fats","Carbohydrates","Protein","Total Calories"]
x = 0

for k in check_val:
    final_list = []
    with open("Dataset.csv") as f:
        next(f)
        i = 0
        for l in  csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
                                
            if i > 3000:
                break
            
            if final_clusters[i] == k:
                final_list.append(l)
            i += 1
    f.close()

    ##print(final_list)


 
    with open("Cluster"+ str(k) +".csv",'w') as f:
         
        wr = csv.writer(f, dialect = "excel")
        wr.writerow(header)
        wr.writerows(final_list)
    f.close()

    
    


