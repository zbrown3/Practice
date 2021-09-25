def fibonacci(n):
  fib_list = [0,1]
  count = 2
  if n < 0:
    ValueError("Input 0 or greater only!")
  if n <= 1:
    return n
  else:
    while count <= n:
      fib_list.append(fib_list[-1] + fib_list[-2])
      count += 1
    return fib_list[-1]


# test cases
print(fibonacci(3))
print(fibonacci(7))
print(fibonacci(0))