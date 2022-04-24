from functools import reduce

letters = ['r', 'e', 'd', 'u', 'c', 'e']

# your code below:

# remember to import the reduce function

# store the result of your reduce function in the variable word
word = reduce(lambda i, j: i + j, letters)

# print word
print(word)
