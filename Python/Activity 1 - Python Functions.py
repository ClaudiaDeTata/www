"""

Write 2 Python functions to: 

show the list content. 
find the max value in the list.
Sample List : [10, 2, 3, 4, 7]

Expected Output :

The content of the list is: [10, 2, 3, 4, 7]

The max value in the list: 10

Important:
Don't forget to comment your code.

"""

# declaring the list
my_list = [10, 2, 3, 4, 7]

# declaration of function passing the list as argument
def show_list(my_list):
  # use of the return statement to let the function return the list values
  return my_list

# printing the output
print("The content of the list is: ", show_list(my_list))

# finding the max value in the list
maxNum = max(my_list)

# declaration of a function passing the max value as argument
def find_max_value(maxNum):
  return maxNum

# printing the output
print("The max value in the list: ", find_max_value(maxNum))