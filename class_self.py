class SearchEngineEntry:
  secure_prefix = "https://" #class variable
  def __init__(self, url): #constructor
    self.url = url
 
  def secure(self): #method
    return "{prefix}{site}".format(prefix=self.secure_prefix, site=self.url)
 
codecademy = SearchEngineEntry("www.codecademy.com") #class object instantiated using constructor
wikipedia = SearchEngineEntry("www.wikipedia.org")
 
print(codecademy.url)
print(codecademy.secure())

print(wikipedia.url)
print(wikipedia.secure())
