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