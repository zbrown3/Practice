import csv

big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False},
            {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False},
            {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False},
            {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}]

with open('output.csv', 'w') as output_csv:
    fields = ['name', 'userid', 'is_admin'] #list of column header names
    output_writer = csv.DictWriter(output_csv, fieldnames=fields) #passes fields to be used as column headers

    output_writer.writeheader() #writes all fields passing to fieldnames as column headers
    for item in big_list: #iterates through list of dictionaries and writes values as rows
        output_writer.writerow(item)
