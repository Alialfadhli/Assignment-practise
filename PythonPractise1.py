import csv

respect = {'last':"opp",'first':"cll"}
with open("ali.csv",'w') as f:
          Fname = ["first","last"]

writer = csv.DictWriter(f, Fname)

writer.writeheader()
writer.writerow({'first':'ali','last': 'you'})
writer.writerow({'first':'no','last':'sl'})
writer.writerow(respect)