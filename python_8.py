## Lecture 8

# This lecture is about importing modules and exploring the standard library
# I will import my own made up module first
# The module is save as python_8a.py

# The code below is to import the module
# I am using the asterisk to import everything from the module
from python_8a import *
# Don't use the asterisk if possible
# Because then it is hard to track down a problem

# Importing the system to find the location of all the modules
import sys
# I will import a module that is not on the list
# I will place it in my desktop, change it as you wish
sys.path.append('/home/suhaimi/Desktop/py_modules')
import module_1 as m1

# A random list to read
courses = ['History', 'Math', 'Physics', 'CompSci']

# Using a function from the module
index = find_index(courses, 'Math')
# Print the output
print('The index of the item in the list is: ',index)

# Printing the test variable that I put in the module
print(test)

# The location where python looks for modules
# print('\nThe directory of the modules is: ')
# print(sys.path)

print()

# Using the new module I made in the external folder
sum = m1.add_func(2,3)
print('The sum is: ', sum)

print()

your_name = m1.name_func('Mahmud Suhaimi')
print(your_name)



