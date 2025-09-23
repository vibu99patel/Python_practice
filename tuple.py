numbers = (1, 2, 3)
print(numbers[1])

# can't change or add to a tuple
# you can only use:
# count() the occurrences
# and index() to find index of the item occurrences

# unpacking
coordinates = (1, 2, 3)
# 1 way
x = coordinates[0]
y = coordinates[1]
z = coordinates[2]
print(x)
# other way
x, y, z = coordinates
print(x)
