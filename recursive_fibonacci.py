def fibonacci(n):
  # base cases
  if n == 1:
    return n
  if n == 0:
    return n
  
  # recursive step
  print("Recursive call with {0} as input".format(n))
  return fibonacci(n - 1) + fibonacci(n - 2)