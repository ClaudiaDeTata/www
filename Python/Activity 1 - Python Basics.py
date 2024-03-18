
"""
Write a Python program to print the result of the following operations.

Test Data:

a. -5 + 8 * 6 

b. (55+9) % 9 

c. 20 + -3*5 / 8 

d. 5 + 15 / 3 * 2 - 8 % 3

Expected Output:

43 

1 

18.125 

13.0

Important:
Don't forget to comment your code.
"""

# variables declaration
a = 5
b = 8
c = 6 
# expression a resolution
print( -a + b * c)

# variables declaration
a = 55
b = 9
# expression b resolution
print((a + b) % b)

# variables declaration
a = 3
b = 5
# expression c resolution
print((b * 4) + -a * b / (a + b))

# variables declaration
a = 3
b = 2
# expression d resolution
print((a + b) + ((a + b)* a) / a * b - (a * b + b) % a)


