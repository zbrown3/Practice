with open('keats_sonnet.txt') as keats_sonnet:
  for line in keats_sonnet.readlines():
    print(line)

#The above script creates a temporary file object called keats_sonnet that points to the file keats_sonnet.txt.
#It then iterates over each line in the document and prints the entire file out.