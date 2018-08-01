def run_fib(n):
  """Generate Fibonacci numbers"""
  fib1 = 1
  fib2 = 1
  number = 0
  fibnumbers = []
  if n == 1: return [1]
  elif n == 2: return [1, 1]
  for i in range (0, n - 2):
    number = fib1+fib2
    fib2 = fib1
    fib1 = number

    fibnumbers.append(number)
    i += 1
  return [1, 1] + fibnumbers
    
def factors_of_multiple(n, factor):
  """Count the number of times a multiple of a given factor is divisible by the factor"""
  count = 0
  while n%factor == 0:
    n = n/factor
    count += 1
  return count


def list_frequency (factor, n):
  "Print line number, Fibonacci position, number of times each factor divides its multiple, and Fibonacci number"""
  a = run_fib(n)
  line_number = 0
  for i in range(len(a)):
    
    if a[i]%factor == 0:
      line_number+=1
      print(line_number, i+1, factors_of_multiple(a[i], factor), a[i])

#Generate information for a factor n, up to the nth Fibonacci number
list_frequency(2, 500)
