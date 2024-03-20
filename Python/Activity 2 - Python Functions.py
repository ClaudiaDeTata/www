"""

Write a Python function to calculate the factorial of a number (a non-negative integer n ). The function accepts the number as an argument.

Note:
The factorial of a number is the product of all the integers from 1 to that number and it is represented by n!

For example, the factorial of 6! is 1*2*3*4*5*6 = 720. 

The factorial is not defined for negative numbers, and the factorial of zero is one, 0! = 1.

Important:
Don't forget to comment your code.

"""
# function declaration - the function will return one if the inputted number is zero and calculate the factorial num for the remaining numbers
def factorialNum(num):
  if num == 0:
    return 1
  else :
    return num * factorialNum(num - 1) 

# prompting the user to input a number
num = int(input("Please input a number: "))
# printing the output
print(factorialNum(num))
