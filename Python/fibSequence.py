def fib(n):
  """
  This function takes in an integer n and returns the nth term
  of the fib series
  """
  
  if n==1: return 0
  elif n==2: return 1
  else: return fib(n-1) + fib(n-2)

def fibSequence(num):
  """
  This function takes in an integer num and prints out the first
  num terms of the fib series
  """
  if type(num) != int or num<1:
    print("Enter a positive integer greater than 0")
    return 0 #to exit the function
    
  for i in range(1, num+1):
    print(fib(i), end=" ")
    
(fibSequence(3))