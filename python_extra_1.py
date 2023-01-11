# Talking about variable scope
'''
LEGB
Local, Enclosing, Global, Built-in
'''

# A global variable
x = 'global x'

# A local variable
def test():
    y = 'local y'
    print(y)
    # Printing the global variable from within a function
    print(x)

test()



