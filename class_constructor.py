class Circle:
  pi = 3.14
  
  # Add constructor here:
  def __init__(self, diameter): #dunder method
    print("New circle with diameter: {}".format(diameter))
  
teaching_table = Circle(36)

#Constructors are methods used to prepare an object that is being instantiated.