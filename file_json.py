import json

with open('purchase_14781239.json') as purchase_json:
    purchase_data = json.load(purchase_json) #parses purchase_json using json.load(), creating a python dictionary out of the file.

print(purchase_data['user'])
# Prints 'ellen_greg'