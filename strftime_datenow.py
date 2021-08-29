from datetime import datetime
date_string = datetime.strftime(datetime.now(), '%b %d, %Y') #first argument takes a datenow format, second argument creates a custom string format using variables found at https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior
print(date_string)