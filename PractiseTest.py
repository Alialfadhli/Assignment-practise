import csv
respected = {"FirstName:Mohammed","LastName:Almeer"}

with open("Faculty_CE.csv",'w') as f:
    Fnames=["FacultyName","ExtensionNumber"]

    writer=csv.DictWriter(f, fieldnames=Fnames)

    writer.writeheader()
    writer.writerow({'FacultyName':'X', 'ExtensionNumber':'Y'})
    writer.writerow(respected)