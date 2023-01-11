# Talking about variable scope
'''
LEGB
Local, Enclosing, Global, Built-in
'''

# Importing the builtin modules to see the built-in variables
import builtins

# Checking all the builtin variables
# print(dir(builtins))
# print()

# Note: Python gives us access to overwrite all these builtin variables and functions

m = min([5, 1, 4, 2, 3])
print(m)

# A global variable
x = 'global x'

# A local variable
def test(z):
    # Put global x in the function
    # If I change the value of x from within the function now
    # The value of x will change globally because of the command below
    global x
    # Make a local y
    y = 'local y'
    print(y)
    # Printing the global variable from within a function
    print(x)
    # Using the local variable z
    print(z)

test('local z')

print()

# Printing the global variable from outside the function
# To show that it is a global variable
print(x)

print()

# Nested functions
# We can understand the enclosing scope using this
def outer():
    x = 'outer x'

    def inner():
        # The commented code below will affect the outer x, the one in the enclosing function
        # nonlocal x
        # If there is a local x to the inner function, the function will use that
        # If it doesn't then it will use the outer x
        # It does not have that either, then it will use the global value
        x = 'inner x'
        print(x)

    inner()
    print(x)

outer()


