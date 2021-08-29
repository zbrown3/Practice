#Methods are functions that are defined as a part of a class.  The first argument is always the object that is calling the method.  Always name the first argument "self", methods always have at least this one argument.
#Methods always pass the first argument as the object.

class Circle:
  pi = 3.14
  def area(self,radius):
    return self.pi * radius ** 2

circle = Circle()

pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(5730)
#Self does not need to be passed as an argument as it is implicitly passed.