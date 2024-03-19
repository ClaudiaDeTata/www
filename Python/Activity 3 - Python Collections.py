"""

Write a Python program to find the maximum and minimum value of a list.

Test Data:

Sample List:

[25, 14, 56, 15, 36, 56, 77, 18, 29, 49]

Expected Output:

Original List: [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]

Maximum value for the above list = 77

Minimum value for the above list = 14

Important:
Don't forget to comment your code.

"""
# declaring collection
theList = [25, 14, 56, 15, 36, 56, 77, 18, 29, 49]
# using sort built-in function to sort the elements in the list
theList.sort()
# printing original list, max and min values
print('Original list:', theList)
print('Maximum value for the above list =', max(theList))
print('Minimum value for the above list =', min(theList))