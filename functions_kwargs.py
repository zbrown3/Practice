def arbitrary_keyword_args(**kwargs):
    print(type(kwargs))
    print(kwargs)
    # See if there's an 'anything_goes' keyword arg and print it
    print(kwargs.get('anything_goes'))


arbitrary_keyword_args(this_arg='wowzers', anything_goes=101)

#**kwargs allows us to define functions with unlimited keyword arguments.
#**kwargs takes the form of a dictionary and be used with standard dictionary functions.

def print_data(**data):
    for arg in data.values():
        print(arg)


print_data(a='arg1', b=True, c=100)

#Iteration can be used with kwargs via .values() method

def print_data(positional_arg, **data):
    print(positional_arg)
    for arg in data.values():
        print(arg)


print_data('position 1', a='arg1', b=True, c=100)

#kwargs can also be combined with positional arguments but positional arguments must come first in our function definition.