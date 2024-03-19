"""

Write a Python program to sum values of a list.

Test Data:

Sample List:

[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

Expected Output:

The sum is 55.

Important:
Don't forget to comment your code.

"""

# declaring the collection
theList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# initializing the sum variable starting from 0
sum = 0
# for loop iterating through every value of the list
for x in theList:
  # variable sum updated by adding each value of the list
  sum += x
 
# printing the result of the sum of the values in the list 
print('The sum is',sum,'.',end='')