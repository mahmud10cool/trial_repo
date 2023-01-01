## Lecture 1

# We separate words using underscore 
# Make variable names that make sense
# Put double quotes if you want to put single quote in the string
# Or you can put a backslash \ to identify the single quote 
my_message = "Bobby's world"

# Put three quotations marks for multiple line strings
multi_line_message = """This is a multi line string. 
So please understand"""

# We can find the length of the message using the len() function
length_message = len(my_message)

print(my_message)
print(multi_line_message)
print(length_message)

# Indexing
# You can use my_message[position - 1] to find the character in that position
# Example:
character_1 = my_message[1-1]
character_2 = my_message[2-1]
# and so on and so forth
# I will print to demonstrate
print(character_1)
print(character_2)

# If I want to see a range of characters, I can use a semicolon
character_1_to_6 = my_message[0:5]
# Print to show the example
print(character_1_to_6)
# If I want to start from the beginning the '0' is unnecessary
# But if I want a specific message (slicing) then I will have to put both indices
character_9_to_13 = my_message[8:13]
# Print for demo
print(character_9_to_13)
# Notice I included 13 here because Python slices where you tell it stop without
# including the character itself in that position

# Methods
# Functions and methods are basically the same thing
# Methods are functions that belongs to an object
# Not going into the details right now
# First example is to make all the characters lower case
# Example
lowercase_message = my_message.lower()
print(lowercase_message)

# Now moving on to another example
# This time counting the number of occurences of a word/character in a string
count_world_message = my_message.count('world')
print(count_world_message)

count_b_message = my_message.count('b')
print(count_b_message)

# To find the index of a character or word in a string
# We can use the find method
find_world = my_message.find('world')
print(find_world)
# The result will be the starting position of the first occurence of the word/character

# To replace a word or character; we can use the replace method
new_message = my_message.replace('world', 'universe')
print(new_message)

# Concatenating
# Means to put together things in a series or chain
greeting = 'Hello'
name = 'Mahmud Suhaimi'
# Use the + symbol to add up strings
message = greeting + ', ' + name
print(message)
# Sometimes the + sign is not a good idea
# If it is really long or many concatenations
# We can use a formatted string for this case
# Python has many ways to do this
# format method is one of them
# f-strings is my preferred method
second_message = '{}, {}. Welcome!'.format(greeting, name)
print(second_message)
# Example of f-string
# This looks the best
third_message = f'{greeting}, {name}. Welcome!'
print(third_message)
# There used to be another style with percentage operators
# I will give an example here but please don't use it
fourth_message = '%s, %s. Welcome!' %(greeting, name)
print(fourth_message)

# A trick to learn something new on python
# The dir() function shows all the methods that are accessible to us
methods_available = dir(name)
# print(methods_available)
# We can use the help() function to find the details of the method
# Example
# string_help = help(str)
# We can find more information about a particular string method
# lower_help = help(str.lower)
