"""

Write a Python program to create the multiplication table (from 1 to 10) of a number.

Expected Output:

Input a number: 6

6 x 1 = 6 

6 x 2 = 12 

6 x 3 = 18 

6 x 4 = 24 

6 x 5 = 30 

6 x 6 = 36 

6 x 7 = 42 

6 x 8 = 48 

6 x 9 = 54 

6 x 10 = 60

Important:
Don't forget to comment your code.

"""

# prompting the user to input the number
num1 = int(input("Please choose the magic number: "))

# for loop using the range() function to iterate variable x until 10 
for x in range(1, 11):
  # printing the multiplication between the number chosen by the user and the variable x and its result
  print(num1, 'x', x, '=', num1*x)