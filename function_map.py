def double(x):
    return x * 2


int_list = [3, 6, 9]

doubled = map(double, int_list)

print(doubled)

"""
map() applies the passed function to each and every element in the iterable and returns a map object.
The returned map object holds the results from applying the mapping function to each element in the pass iterable.
We will usually convert the map into a list to enable viewing and further use.
In the example a function called double() that takes in a value and returns the value doubled.  This function can be used anywhere in our program.
We also defined an iterable (int_list) that we wanted to apply the function to.
We then passed the function reference double as the function argument and  int_list as the iterable to map()
The map() function proceeded to apply double() onto each element in int_list
When we printed the result, we could see that the output of the map() function was a specific type of object called a map object.
If we want to see the actual results of mapping double() to the elements of int_list, we need to convert the map object to a list using the built-in list() function.
"""

doubled = map(lambda input: input * 2, int_list)

print(list(doubled))
"""
Higher-order functions like map() work especially well with lambda functions.
"""

