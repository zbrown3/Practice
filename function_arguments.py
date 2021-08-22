def trip_planner(first_destination, second_destination, final_destination="Codecademy HQ"):
  print("Here is what your trip will look like!")
  print("First, we will stop in " + first_destination + ", then " + second_destination + ", and lastly " + final_destination)
trip_planner("France", "Germany", "Denmark") #arguments are mapped to the paramaters based on positions
trip_planner("Denmark", "France", "Germany") 
trip_planner(first_destination="Iceland", final_destination="Germany", second_destination="India") #keyword argument where each argument is passed directly to parameter regardless of position.
trip_planner("Brooklyn", "Queens") #if parameter has a default argument then default will automatically be used in the function 
