import csv

with open("ali.csv",'r') as f:
    D = csv.reader(f)
    for row in D:
        print(row)
        
