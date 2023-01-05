## Lecture 4

# Dictionaries
# We have two important arguments
# Key and a value
# We follow the key with a semicolon and then put the value
# Kind of like the word followed by the meaning
student = {'name': 'John', 'age': 25, 'courses': ['Math', 'CompSci']}
# If we want to print the value (meaning) behind any of the keys (words)
# Then we just print the dictionary with the key being the index
print(student['name'])
print(student['courses'])
# Another way to get the value behind the key is to use the get method
print(student.get('age'))
# With this method, if we put an invalid key, instead of returning an error 
# it will return a none
print(student.get('phone'))
# We can put a default output for non-existent or empty keys
# We do that by putting another argument separated by a comma
print(student.get('gender', 'The key is invalid'))

# Adding a key with a value
student['phone'] = '555-5555'
print(student['phone'])
print(student)

# Updating a key
# This can be done using two methods
student['name'] = 'Mahmud'
print('\nUpdate 1:')
print(student)
# or
# The argument has to be in the form of a dictionary
student.update({'name': 'Suhaimi', 'age': 26})
print('\nUpdate 2:')
print(student)

# Removing a key
# First way
del student['age']
print('\n Age removed:')
print(student)
# Second way
phone = student.pop('phone')
print('\nPhone removed:')
print(student)
print('\nPhone popped:')
print(phone)

# To find the number of keys in the dictionary
# We can use the len function
print('\nLength of the dictionary')
print(len(student))

# To see all of the keys, we can use the key method
print('\nThe keys of the dictionary:')
print(student.keys())

# To see all of the values of the dictionary, we can use
# the values method
print('\nAll the values of the dictionary:')
print(student.values())



