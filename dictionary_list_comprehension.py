drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)
drinks_to_caffeine = {key: value for key, value in zipped_drinks}
print(drinks_to_caffeine)
