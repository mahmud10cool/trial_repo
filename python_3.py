# This lecutre is about lists, tuples and sets
courses = ['History', 'Maths', 'Physics', 'CompSci']
length_list = len(courses)

# We can use indexing here as well
first_item = courses[0]
print(first_item)
# We can access two of the values in the list
# Assign the index to a variable 'n' for better understanding
n = 2
# The code below will only select the items until 'n-1'
range_items = courses[0:n]
print(range_items)

# There are three ways to add data into a list
# 1. Append, 2. Insert, 3. Extend
# There are more ways but they will not be covered here
# 1st way (The item will be added to the end of the list and there will be no way to choose the location)
courses.append('Art')
print(courses)
# 2nd way (I can choose the location where I will insert the new item with this method)
courses.insert(3, 'Art')
print(courses)
# 3rd way (This adds a new list to the current list)
courses_2 = ['Biology', 'Education']
courses.extend(courses_2)
print(courses)

# Removng items from the list
# Method 1
courses.remove('Maths')
print(courses)
# Method 2
# This method removes the last item from the list
# It is basically the opposite of append
courses.pop()
print(courses)

# Sorting the list
# If we want to reverse our list
# We can use the reverse method
courses.reverse()
print(courses)