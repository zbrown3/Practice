def calc_paint_amount(width, height):

  square_feet = width * height
  # Write your code below!
  def calc_gallons():
    return square_feet / 400
  return calc_gallons()


print('Number of paint gallons needed: ')
print(str(calc_paint_amount(30,20)))

"""
Enclosing scope allows any value defined in an enclosing function to be accessed in nested functions below it.
The flow of scope access only flows upwards.  This means that the deepest level has access to every enclosing namespace above it but not the other way around.
Immutable objects, such as strings or numbers can be accessed in nested functions but cannot be modified.
"""