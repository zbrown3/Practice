with open('generated_file.txt', 'a') as gen_file:
  gen_file.write("... and it still is")

#passing 'a' as the second argument for open() opens the file in append mode.
#Opening the file in append-mode, with 'a' as an argument to open(), means using the file object's .write() method appends whatever is passed to the end of the file in a new line.