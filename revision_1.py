## Revision 1
# I will revise the first three lectures here

## Strings
name = 'Mahmud Suhaimi Ibrahim'
university = 'IIUM'
gender = 'non-conforming'
# Print the two strings
print(name, university)
# We can use certain operators to concatenate strings
print(name + ', ', gender)

# A few string methods
# lower, upper and capitalize
lower_name = name.lower()
upper_name = name.upper()
capitalize_gender = gender.capitalize()
print(lower_name)
print(upper_name)
print(capitalize_gender)
# count and find
# count
count_a = name.count('a')
count_u = name.count('u')
print(count_a)
print(count_u)
# find
find_a = name.find('a')
find_M = name.find('M')
find_m = name.find('m')
print(find_a, find_M, find_m)

# replace method to replace part of a string
replaced_name = name.replace('Ibrahim', 'Islam')
print(replaced_name)

# String formatting
# There are many methods, I will use the newest one
# It is known as f-strings
overall_string = f"""My name is {name}. My gender is {gender}. 
I study at {university}"""
# Print to show example
print(overall_string)

## Integers and floats
# Of course when comes to integers and floats, one of the most 
# important thing is operators
# First define two integers
x = 3
y = 2
# Two floats as well
p = 5.3
q = 2.7

# Addition
print(x + y)
print(p + q)
print(x + p) # This will return a float

# Subtraction
print(y - x)
print(p - q)

# Multiplication
print(p*x*q)

# Division
print(q/x)

# Exponent
print(q**p)

# Modulus
# This is used to check if a number is even or odd
# Also can be used to check if a number is 0 or 1
print(x%y)

# BODMAS or rules of operations definitely apply here
print(y - x / x + y)
print((y - x)/(x + y))

# Division has a tendency of returning a float
# If you want division to return an integer, there are two 
# functions that you can use
# int() function
# This floors the value
print(int(y/x))
# round() function
# This rounds up
print(round(y/x))
# You can also use the round function to round to a certain 
# decimal place
print(round(y/x, 2))

# Comparators
# These will compare two numbers
# Using these will result in a boolean value of True or False
# A few examples
print(y > x)
print(y != x)

# Other use of the float and int functions
# In Python, we can use these functions to conver 'number' strings
# into integers and floats
x = '123'
print(int(x))
print(float(x))