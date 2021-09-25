def factorial(n):
  product = 1
  if n < 0:
    ValueError("Inputs 0 or greater only")
  if n <= 1:
    return 1
  else:
    for i in range(1, n + 1):
      product *= i
    return product

print(factorial(3))
print(factorial(0))
print(factorial(5))