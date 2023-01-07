## Lecture 7

# This lecture is about functions
def hello_func():
    print("Hello World")
    
# One of the greatest benefits of functions 
# Is that you can put a block of code with a specific function
# in a specific place. If the function is being is called multiple
# times and has a small error, it is easier to change a function
# rather than change the block of code multiple times.

# Space in the terminal for aesthetic reasons
print()

# Ex.
# The wrong way showed is not keeping your code dry
print("The wrong way: ")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
# Imagine if there is a small typo in one of the print statements
# You would have to change each of them individually
# But now you can change them once, and it should change for all of them
# Keeping your code DRY
print("\nThe right way: ")
hello_func()
hello_func()
hello_func()
hello_func()

print()

# Instead of printing, we will use return here
# It is something completely different 
def new_func():
    return 'Function using return statement'
new_func()
print(new_func())
# For a function, after you build it, you are mainly concerned about the 
# input and the output

print()

# A built in function is an example of when we don't really care what is 
# inside the function. I will use the len function to demonstrate
print(len('Hello World'))

print()

# We can use functions/methods on returned values from functions
# Example
print(len(new_func()))
print(new_func().upper())

print()

# Now we learn how to pass arguments to our function
def greet_func(greeting):
    return '{} Function.'.format(greeting)

print(greet_func('Assalamualaikum'))
print(greet_func('Bonjour'))

print()

# We can create functions with default values so just in case an argument is
# missing, we will default to that value
# Example
def def_func(age, name = 'Mahmud'):
    return f'My name is {name} and I am {age} years old'

print(def_func(23, 'Alberta'))
print(def_func(25))