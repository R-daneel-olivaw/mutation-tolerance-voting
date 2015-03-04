import csv

print('testing')

with open('D:\Lectures\Winter2015\CS886\Project\sushi3_preflib\sushi3_preflib\ED-00015-00000001.soc') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row)