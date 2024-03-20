"""

Write a Python function that takes a number as a parameter and check the number is prime or not. 

Note: 

Prime numbers are the numbers that are only divisible by themselves and 1, in other words, if we try to divide them by another number, the result is not a whole number. 

So, if we divide the number by anything other than 1 or itself, we will get a remainder that is not zero. 

Negative numbers can not be prime.

Important:
Don't forget to comment your code.

"""
# declaration of primeNum function which finds out if a number is prime
def primeNum(num) :
  # check if the number is < than two
  if num < 2:
    return False
  # for loop to check the range of numbers between two and a hypotetical num
  for i in range(2, num):
    # if the remainder of the division between num and the variable i is zero, the number is not prime, otherwise it is
    if num % i == 0:
      return False
  else: 
    return True

# printing the output
print(primeNum(num))