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
# sys.path.append('/home/suhaimi/Desktop/py_modules')
# No need to do the last line if you do it for the whole computer by 
# adding it as an environment variable in the bashrc for linux
# and there is a particular way to do it for windows
import module_1 as m1
print()

# I will give the bash line here
# export PYTHONPATH="/home/suhaimi/Desktop/py_modules"

# Importing other modules
import random
import math
import datetime
import calendar
import os

# A random list to read
courses = ['History', 'Math', 'Physics', 'CompSci']

# Using the random module
random_course = random.choice(courses)
print('The random course is: ',random_course)
print()

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

print()

# Using the math module
rads = math.radians(90)
print('The angle in radians is: ', rads)
print('The sin of the angle is: ', math.sin(rads))

print()

# Using the datetime module
today = datetime.date.today()
print('The date today is: ', today)

print()

# Using the calendar module
year = 2020
is_it_leap = calendar.isleap(year)
print(year, ' is a leap year: ', is_it_leap)

print()

# Using the os module
# This give us access to the underlying os that is in use
# If it is linux, then linux and if it's windows then windows
# Current work directory
print(os.getcwd())

print()

# We can see the location of the module using the dunderfile method
print('The location of the os module is: ',os.__file__)

# Importing a joke module
import antigravity
