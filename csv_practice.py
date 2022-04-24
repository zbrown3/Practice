import csv

county_list = []
with open('practice.csv', newline='') as csv_practice:
    csv_rows = csv.DictReader(csv_practice)
    for i in csv_rows:
        county_list.append(i['County'])

print(county_list)