
import numpy as np
from csv import DictReader
import csv

with open("Dataset.csv") as f:
    food_name = [row["Name"] for row in DictReader(f)]

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

Z = [i*2.25 for i in Z]

cluster_table= []

for i in range(0,len(X)):
    magic_string = int(X[i]//5) + int(Y[i]//5) + int(Z[i]//5)
    final_clusters.append(magic_string)
    cluster_table[food_name[i]] = magic_string

    
check_val = set(final_clusters)
print(len(final_clusters))
##print(min(final_clusters))
##print(max(final_clusters))
##print(len(check_val))

reverse_cluster_table = {}


for key, value in cluster_table.items():	
	if value not in reverse_cluster_table: 
		reverse_cluster_table[value] = [key]
	else:
		reverse_cluster_table[value].append(key)

##
##for key, value in reverse_cluster_table.items():	
##    print(key)

final_cluster_table = {}
for key,value in cluster_table.items():
    final_cluster_table[key] = reverse_cluster_table[value]

print(final_cluster_table("BUTTER,WITH SALT"))

##
##print(final_cluster_table["TURKEY,YOUNG HEN,MEAT ONLY,COOKED,ROASTED"])
##for key,value in final_cluster_table.items():
##    print(key)
##    print(value)

##
##print(final_cluster_table.items())

##
##header = ["Food Item","Type","Category","Fats","Carbohydrates","Protein","Total Calories"]
##x = 0

##for k in check_val:
##    final_list = []
##    with open("Dataset.csv") as f:
##        next(f)
##        i = 0
##        for l in  csv.reader(f, quotechar='"', delimiter=',', quoting=csv.QUOTE_ALL, skipinitialspace=True):
##                                
##            if i > 3000:
##                break
##            
##            if final_clusters[i] == k:
##                final_list.append(l)
##            i += 1
##    f.close()
##
##    ##print(final_list)
##
##
## 
##    with open("Group_"+ str(k) +".csv",'w') as f:
##         
##        wr = csv.writer(f, dialect = "excel")
##        wr.writerow(header)
##        wr.writerows(final_list)
##    f.close()
##
    
    


