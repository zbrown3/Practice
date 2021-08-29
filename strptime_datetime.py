from datetime import datetime
parsed_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y') # used to create a variable and setup a custom format for datetime.  First argument is the custom date, second is the python format using variables found at https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
print(parsed_date.year)