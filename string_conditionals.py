def contains(big_string,little_string):
  return little_string in big_string

def common_letters(string_one,string_two):
  new_list = []
  for i in string_one:
      if (i in string_two) and not (i in new_list):
        new_list.append(i)
  return new_list
print(common_letters("Manhattan", "San Francisco"))