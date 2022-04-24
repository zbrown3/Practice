import csv

list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
    user_reader = csv.DictReader(users_csv)
    for row in user_reader:
        list_of_email_addresses.append(row['Email'])

#In the above code we import csv library, which gives us the tools to parse the CSV file.  We then create the empty list which is later populated with email addresses from the CSV.
#Then the file is opened with the temporary variable.  The additional keyword newline='' is passed to open() so that we don't mistake a line break in one of our data fields as a new row.
#csv.DictReader(users.csv) converts the lines of our CSV file to Python dictionairies.  The keys of the dictionary are the entries in the first line of the CSV file.
# We can then iterate through the rows of our user_reader object to access all of the rows in the CSV as dictionaries except the first row.
#We then access the 'Email' key of each of these rows and grab the email address in that row and append it to our list.