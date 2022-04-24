with open('generated_file.txt', 'w') as gen_file:
  gen_file.write("What an incredible file!")

#Here we pass the argument 'w' to open() in order to indicate to open the file in write-mode.  The default argument is 'r' for read-mode
#This code creates a new file in the same folder as the program and gives it the text "What an incredible file!
#If file name already exists then it will be completely overwritten and erase whatever it's contents were before.