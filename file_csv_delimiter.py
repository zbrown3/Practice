import csv

with open('addresses.csv', newline='') as addresses_csv:
    address_reader = csv.DictReader(addresses_csv, delimiter=';')
    for row in address_reader:
        print(row['Address'])

#if comma isn't used as the delimiter then we call csv.DictReader we pass in the delimiter parameter which is the string that's used to delineate separate fields.
