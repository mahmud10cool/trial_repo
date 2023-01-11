# This program is about slicing lists and strings
# I have done a little bit of this before
# But it will be a good revision

my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def choose_index(x):
    # Print out the value in that position or index
    return my_list[x]

print()

# Take in a value from the user
# index = input('Please choose the index: ') 
index = 5

# Now there is a problem
# The input will be in the form of a string but the index must be an int
# There are a couple of ways to solve this

# Way 1 (Commented)
# index_int = int(index or "0")
# print('The value in the chosen index is: ', choose_index(index_int))

# Way 2 (This way takes into account if there is a completely invalid input)
# Exceptions will be dealt with in detail in a later program
try:
    index_int = int(index)
    print('The value in the chosen index is: ', choose_index(index_int))
except ValueError:
    print('Error! You made a mistake. The default value is: ', choose_index(0))

print()

# Extract a certain range from the list
# Remember that it is all the values except for the last one
# End is non-inclusive
print('Range from 0 to 4: ', my_list[0:5])
print('Range from 3 to 7: ', my_list[3:8])
print('Range from 0 to 9: ', my_list[0:10])
print('Range from 1 to end: ', my_list[5:])

# I can even choose a negative index
# The negative index will represent the positive index subtracted by 10
# So -7 represents 3 because 3-10 = -7
print('Range from 2 to 6: ', my_list[-8:-3])

print()

# Steps to skip certain values
# The step is the last value, NOT the value in the middle
print('Range from 0 to 9, step = 2: ',my_list[0:9:2])
# I can use negative steps to go in reverse
print('Range from 0 to 9, step = -2: ',my_list[9:0:-2])