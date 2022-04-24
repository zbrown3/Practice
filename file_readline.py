with open('millay_sonnet.txt') as sonnet_doc:
  first_line = sonnet_doc.readline()
  second_line = sonnet_doc.readline()
  print(second_line)

#This script creates a file object called sonnet_doct that points to the file millay_sonnet.txt.
#It then reads in the first line using sonnet_doc.readline() and saves that to the variable first_line.
#It then saves the second line into the variable second_line and then prints it out.