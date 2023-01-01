## Lecture 2

# We will work with numeric data in this lecture
num = 3
# Python has a type function to know the type of the variable
number_type = type(num)
print(number_type)

# A float number is slightly different 
num_float = 3.14
number_float_type = type(num_float)
print(number_float_type)

# Arithmetic operators
# Addition
num_add = 3 + 2
print(num_add)
# Subtraction
num_sub = 3 - 2
print(num_sub)
# Multiplication
num_mult = 3 * 2
print(num_mult)
# Division
num_div = 3 / 2
print(num_div)
print(type(num_div))
# Floor division
num_floor_div = 3 // 2
print(num_floor_div)
print(type(num_floor_div))
# Exponent
num_exp = 3 ** 2
print(num_exp)
# Modulus 
num_mod = 3 % 2 
print(num_mod)
# We can use mod 2 to check if a number is odd or even

# BODMAS applies here
print(3 * 2 + 1)
print(3 * (2 + 1))

# Incrementing
# Start with a number
i = 1
print(i)
i = i + 1
print(i)
# or we can do it in a shorthand way
i += 1
print(i)
# We can increment by other values as well
i += 10
print(i)

# Absolute function
# This removes the sign from the number just like in mathematics
abs_number = abs(-2)
print(abs_number)

# Rounding 
# This function rounds the number conventionally
round_number = round(3.14159)
print(round_number)
# We can even round to a specific decimal place
round_to_first_dec = round(3.14159, 1)
print(round_to_first_dec)

# Booleans for the first time
# The comparisons will give a boolean output
num_1 = 3
num_2 = 2

print(num_1 == num_2)
print(num_1 != num_2)
print(num_1 > num_2)
print(num_1 < num_2)

# Variables that look like a number but is a string
num_3 = '100'
num_4 = '200'
# If we add directly, it will just concatenate
print(num_3 + num_4)
# We will have to somthing known as casting
# We can use the int() or float() function
print(int(num_3) + int(num_4))
print(float(num_3) + float(num_4))