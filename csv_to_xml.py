import csv
            
f = open('carbon intensity.csv')
csv_f = csv.reader(f)   
data = []

for row in csv_f: 
   data.append(row)
f.close()

print data[1:]
