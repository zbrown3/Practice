can_we_count_it = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
for i in can_we_count_it:
  if hasattr(i,"count") == True:
    print(str(type(i)) + " has the count attribute!")
  else:
    print(str(type(i)) + " does not have the count attribute :(")

# hasattr(object, “attribute”) checks an object to see if an attribute exists.  Returns True or False.
# getattr(object, “attribute”, default) returns default argument if attribute doesn't exist.