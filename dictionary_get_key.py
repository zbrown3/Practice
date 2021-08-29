user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder", 100000) #returns value of key argument provided.  Can provide one argument but also provide a second which is a value to return if key is not found.
stack_id = user_ids.get("superStackSmash", 100000)
print(stack_id)
print(tc_id)