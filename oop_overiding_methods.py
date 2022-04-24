class Employee():
  new_id = 1
  def __init__(self):
    self.id = Employee.new_id
    Employee.new_id += 1

  def say_id(self):
    print("My id is {}.".format(self.id))

class Admin(Employee):
  # Write your code below
  def say_id(self):
    print("I am an Admin")

e1 = Employee()
e2 = Employee()
e3 = Admin()
e3.say_id()

"""
An overridden method in a subclass is one that has the same definition as the parent class but contains different behavior.

"""