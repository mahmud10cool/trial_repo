## Lecture 6

# This lecture will deal with for and while loop

## for loops
nums = [1, 2, 3, 4, 5]

for num in nums:
    print(num)

# break and continue keywords
# break completely breaks out of a loop
# continue moves on to the next iteration of the loop

nos = [4, 5, 7, 3, 9, 0]
# The break statement
for no in nos:
    if no == 3:
        print('Found!')
        break
    print(no)

# The continue statement
for no in nos:
    if no == 7:
        print('Found!')
        continue
    print(no)

# create some space in the results 
print('\n')

# loop within a loop
numbers = [1, 2, 3, 4, 5, 6, 7]

for x in numbers:
    for letter in 'abc':
        print(x, letter)

# note: should be careful with nested loops

# create some space in the terminal for beauty reasons
print('\n')

# sometimes you will want to go through a loop a certain number of times
# there is a function known as the range function to help with this
# this function will print until the number but not including
for i in range(1, 11):
    print(i)

# again another space for beauty reasons
print('\n')

## while loops
# this will keep going until a condition is met or broken
x = 0

while x < 10:
    print(x)
    x += 1

print('\n')

# infinite loop with break statement
x = 0

while True:
    if x == 5:
        break
    print(x)
    x += 1