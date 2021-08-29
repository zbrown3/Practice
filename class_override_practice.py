class SortedList(list):
  def append(self,value):
    super().append(value)
    self.sort()

#creates SortedList as a subclass of the built-in Python List and adds sorting functionality