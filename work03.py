import csv

with open('occupations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    d = {}
    for row in reader:
        d[ row['Job Class'] ] = float (row['Percentage'])

for job in d:
    print (job , d[job])    



    
