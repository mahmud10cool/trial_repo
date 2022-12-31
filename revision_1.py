# First let us start with strings
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


