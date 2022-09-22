import csv

f=open("test.csv","r")
reader=csv.reader(f)
for row in reader:
    for item in row:
        print(item)
f.close()
        
        