"""
Write a Python program that accepts three numbers and prints "All numbers are equal" if all three numbers are equal, "All numbers are different" if all three numbers are different and "Neither all are equal or different" otherwise.

Test Data:

Input first number: 2
Input second number: 3
Input third number: 4

Expected Output :

All numbers are different.

Important:
Don't forget to comment your code.

"""
# prompting the user to input 3 numbers
num1 = int(input("Please input the first number: "))

num2 = int(input("Please input the second number: "))

num3 = int(input("Please input the third number: "))

# if statement to check the 3 conditions
if num1 == num2 and num2 == num3 and num1 == num3 :
  print("All numbers are equal")
elif num1 != num2 and num2 != num3 and num1 != num3 :
  print("All numbers are different")
else :
  print("Neither all are equal or different")
