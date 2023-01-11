# This is a file/program to support lecture 8
# It is a module

print('Imported python_8a')

test = 'My name is Mahmud Suhaimi Ibrahim'

def find_index(to_search, target):
    # Find the index of a value in a sequence
    for i, value in enumerate(to_search):
        if value == target:
            return i
        
    return -1