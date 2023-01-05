## Lecture 5

# Conditionals 
# A little bit of knowledge for future use
# Comparators
# Equal:                ==
# Not Equal:            !=
# Greater Than:         >
# Less Than:            <
# Greater or Equal:     >=
# Less or Equal:        <=
# Object identity:      is

# Logical operators in Python
# and
# or
# not

# If, else and elif statements
if True:
    print('Conditional was True!')
# If the the conditional is False, then 
# anything after the if statement will 
# not be printed
if False:
    print('Conditional was False!')

# Create a variable
language = 'Python'
# Understanding if, elif and else statements
if language == 'Python':
    print('The language is Python')
elif language == 'Java':
    print('The language is Java')
elif language == 'JaveScript':
    print('The language is JavaScript')
else:
    print('Language is not Python')

# Understanding logical operators 
user = 'Admin'
logged_in = False
# use of the 'and' logical operator
if user == 'Admin' and logged_in:
    print('Admin Page')
else:
    print('Bad Creds')
# New variables
player = 'Lionel Messi'
status = 'GOAT'
# Understanding the 'or' operator
if player == 'Lionel Messi' or status == 'GOAT':
    print('Lionel Messi is the GOAT')
else:
    print('You are mistaken')
# More variables
name = 'Mahmud Suhaimi'
existance = False
# Understanding the 'not' operator
if not existance:
    print('Please exist')
else:
    print('Welcome Mahmud Suhaimi')

# Objects that are the same but not same in memory
# We use the 'is' comparator for objects that are 
# the same in memory
a = [1, 2, 3]
b = a
print(id(a))
print(id(b))
print(a == b)
print(a is b)
# The same as saying 
print(id(a) == id(b))

# False values
    # False
    # None
    # Zero of any numeric type
    # Any empty sequence. For example, '', (), [],
    # Any empty mapping. For example, {},
# False
condition = False
if condition:
    print('Evaluated to True')
else:
    print('Evaluated to False')
# None
x = None
if x:
    print('x is True')
else: 
    print('x is False')
# Zero
y = 0
if y:
    print('x is not zero')
else:
    print('y is zero')
# Empty list, tuple, dictionary or string
z = ''
if z:
    print('z is not empty')
else:
    print('z is empty')