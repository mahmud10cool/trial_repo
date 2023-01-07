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
print("The wrong way: ")
print("Hello World")
print("Hello World")
print("Hello World")
print("Hello World")
# Imagine if there is a small typo in one of the print statements
# You would have to change each of them individually
# But now you can change them once, and it should change for all of them
print("\nThe right way")
hello_func()
hello_func()
hello_func()
hello_func()
