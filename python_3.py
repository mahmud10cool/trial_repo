# This lecutre is about lists, tuples and sets

# Lists
courses = ['History', 'Maths', 'Physics', 'CompSci']
length_list = len(courses)

# Make another list for future use
nums = [1, 5, 2, 4, 3]

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
print(nums)
# Another method to sort (reverse in this case) a list
# This method sorts alphabetically
# reverse = True means in descending order
courses.sort(reverse=True)
nums.sort(reverse=True)
print(courses)
print(nums)
# Instead of methods we can use the sorted function
# However we have to place the result into a variable like any other function
sorted_courses = sorted(courses)
print(sorted_courses)

# A few other built-in list functions
max_value = max(nums)
min_value = min(nums)
sum_nums = sum(nums)
print(max_value, min_value, sum_nums)

# Searching for index of item in the list
location = courses.index('CompSci')
print(location)

# If we want to check whether item is in the list at all
# We can use the 'in' statement
# It will return a True or False
is_there_in_courses = 'Art' in courses
print(is_there_in_courses)

# Looping through the values in our list
# We can use the 'for' loop
# We can use the 'enumerate' function to get the index and the item value
for index, item in enumerate(courses, start=1):
    print(index, item)

# If we want to turn our list into a bunch of strings with comma separation
course_str = ', '.join(courses)
print(course_str)
# We could do hyphen separation in the same way
course_hyphen =' - '.join(courses)
print(course_hyphen)

# Making a new list to put the separated strings back into a list
# This split method should really fall under lecture 1. Because it has 
# more to do with strings than lists
# It splits a string based on the given input parameter
new_list = course_hyphen.split(' - ')
print(new_list)

# Mutable
list_1 = ['History', 'Maths', 'Physics', 'CompSci']
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'Art'

print(list_1)
print(list_2)

## Tuples
# We can't append or remove anything from a Tuple
# That is why it is known as immutable
# Immutable
tuple_1 = ('History', 'Math', 'Physics', 'CompSci')
tuple_2 = tuple_1
print(tuple_1)
print(tuple_2)

## Sets
# Order of sets are not fixed, they change in every iteration
# They throw out duplicates
cs_courses = {'History', 'Math', 'Physics', 'CompSci', 'History', 'Math'}
art_courses = {'History', 'Math', 'Art', 'Design'}
print(cs_courses)
print('Math' in cs_courses)
# Another thing that sets can do very efficiently is that they can 
# compare values with other sets 
# To see what values they have in common, we can use the intersection method
print(cs_courses.intersection(art_courses))
# To see what values they have different, we can use the difference method
print(cs_courses.difference(art_courses))
# To combine the values of the two sets, we can use the union method
print(cs_courses.union(art_courses))

## How to create empty set, lists and tuples
# Empty lists
empty_list_1 = []
empty_list_2 = []

# Empty tuples
empty_tuple = ()
empty_tuple = tuple()

# Empty sets
# We cannot just put empty curly braces
# That would create a dict, not a set
# Wrong way
empty_set = {} # Not a set. This is a dict
# Right way, this is an empty set
empty_set = set() 



