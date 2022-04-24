def print_available(color):
  global paint_gallons_available
  paint_gallons_available = {
    'red': 50,
    'blue': 72,
    'green': 99,
    'yellow': 33
  }
  print('There are ' + str(paint_gallons_available[color]) + ' gallons available of ' + color + ' paint.')


print_available('red')
for color in paint_gallons_available:
  print(color)

"""
Python provides the global statement to allow the modification of global names from a local scope.
The global statement can be used even if the name has not been defined in the global namespace.  
Using the global statement would create the new variable in the global namespace.
"""