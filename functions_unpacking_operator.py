def my_function(*args):
  print(args)

#The unpacking operator (*) allows us to give our functions a variable number of arguments by peforming what's known as postional argument packing.
#The unpacking operator creates a tuple consisting of each argument that is passed.

def shout_strings(*args):
  for argument in args:
    print(argument.upper())


shout_strings('Working on', 'learning', 'argument unpacking!')


def truncate_sentences(length, *sentences):#unpacking operator can also be combined with other positional arguments
  for sentence in sentences:
    print(sentence[:length])


truncate_sentences(8, "What's going on here", "Looks like we've been cut off")