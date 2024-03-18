"""

Write a Python program that accepts three numbers from the user and prints "Increasing order" if the numbers are in the increasing order, "Decreasing order" if the numbers are in the decreasing order, and "Neither increasing or decreasing order" otherwise.

Test Data:

Input first number: 1524
Input second number: 2345
Input third number: 3321

Expected Output :

Increasing order.

Important:
Don't forget to comment your code.

"""

# prompting the user to input three numbers
num1 = int(input("Please input the first number: "))

num2 = int(input("Please input the second number: "))

num3 = int(input("Please input the third number: "))

# if statement to check three conditions (increasing, decreasing or neither)
if num1 < num2 and num2 < num3 and num1 < num3 :
  print("Increasing order.")
elif num1 > num2 and num2 > num3 and num1 > num3 :
  print("Decreasing order.")
else:
  print("Neither increasing or decreasing order.")