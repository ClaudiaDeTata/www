"""

Write a Python program to get the Fibonacci series between 0 to 50. 

Note : 

The Fibonacci Sequence is the series of numbers : 0, 1, 1, 2, 3, 5, 8, 13, 21, .... 

Every next number is found by adding up the two numbers before it.

Important:
Don't forget to comment your code.

"""

# initializing the first two numbers of the Fibonacci sequence, declaring them in the variables a and b
a = 0
b = 1

# while loop that iterates until b is < or = to 50 and prints the next number if b is > or = to 0
while b <= 50 :
  if b >= 0:
    print(b)
  # calculation of the variable c that helps calculating the rest of the values
  c = a + b
  a = b
  b = c