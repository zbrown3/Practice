add_two = lambda my_input: my_input + 2

print(add_two(3))
print(add_two(100))
print(add_two(-2))

"""
A lambda function is a one-line shorthand for function.  
The function is stored in a variable called add_two
The lamdbda keyword declares that this is a lambda function
my_input is a parameter used to hold the value passed to add_two
In the lambda function version, we are returning my_input + 2 without the use of a return keyword.
"""

check_if_A_grade = lambda grade: 'Got an A!' if grade >= 90 else 'Did not get an A.'
"""
lambda grade: declares a lambda function with the paramater grade
Return 'Got an A!' if this statement is true:  grade >= 90
Else return 'Did not get an A.'
"""