class Student:
  def __init__(self,name,year):
    self.name = name
    self.year = year
    self.grades = []
  def add_grade(self,grade):
    if type(grade) == Grade:
      self.grades.append(grade)




roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
  minimum_passing = 65
  def __init__(self,score):
    self.score = score
  
  def is_passing(self,score):
    if score > 65:
      return "{} has a passing score.".format(self)

pieter.add_grade(Grade(100))
