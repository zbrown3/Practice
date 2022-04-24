names = ["margarita", "Linda", "Masako", "Maki", "Angela"]

M_names = filter(lambda name: name[0] == "M" or name[0] == "m", names)

print(list(M_names))


"""
The goal of the filter() function is to filter values out of an iterable.
The filter() function applies a passed filtering function to each element in the passed iterable.
The filtering function should be a function that returns a boolean value: True or False.
The returned filter object will hold only those elements fo the passed iterable for which the filtering function return True.
In the example, filter() takes two parameters:  the lambda filtering function and the list, names.
The filter() function then iterates through names and applies the lambda function to each item in the list.
For each item in the list, if the condition in the lambda function evaluates to True, the item is added to a filter object.
The filter object is returned and when converted to a list and printed.
"""