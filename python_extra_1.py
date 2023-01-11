# Talking about variable scope
'''
LEGB
Local, Enclosing, Global, Built-in
'''

# A global variable
x = 'global x'

# A local variable
def test():
    # Put global x in the function
    # If I change the value of x from within the function now
    # The value of x will change globally because of the command below
    global x
    # Make a local y
    y = 'local y'
    print(y)
    # Printing the global variable from within a function
    print(x)

test()

# Printing the global variable from outside the function
# To show that it is a global variable
print(x)



