from functools import reduce

int_list = [3, 6, 9, 12]

reduced_int_list = reduce(lambda x, y: x * y, int_list)

print(reduced_int_list)


"""
reduce() function must be imported from the functools module to use it.
reduce() returns a single value.  To get to this single value, reduce() cumulatively applies a passed function to each sequential pair of elements in an iterable.
In the example the reduce() function takes 2 arguments: a lambda function and a list of integers.
The lambda function takes 2 numbers, x and y and multiplies them together.
The reduce() function applies the lambda function to the first two elements in the list, 3 and 6, to get a product of 18.
Next, 18 was multiplied by the following element in the list, 9, to get 162.
Continuing on, 162 was multiplied by the next element, 12, to get 1944.
The last final value 1944 is what was returned by reduce()
"""