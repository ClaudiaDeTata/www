"""

Write a Python program to calculate the average value of a list elements.

Test Data:

Sample List:

[20, 30, 25, 35, -16, 60, -100]

Expected Output:

Average value of the list elements is : 7.7.

Important:
Don't forget to comment your code.

"""

# declaring collection
theList = [20, 30, 25, 35, -16, 60, -100]
# initializing the value of sum starting at zero
sum = 0
# for loop iterating through the values of the list
for x in theList:
  # updating sum by adding each element of the list 
  sum += x 
  # calculating the average
  avg = sum/len(theList)
  # rounding the average to one decimal place
  rounded_avg = round(avg, 1)

# printing the result
print('Average value of the list of elements is:', rounded_avg, '.',end='')