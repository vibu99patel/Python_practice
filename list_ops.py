numbers = [5, 2, 1, 7, 4]
numbers.append(20)  # adds it to the end
print(numbers)
numbers.insert(0, 10)  # to add it to specific position
print(numbers)
numbers.remove(5) # to delete an item
print(numbers)
numbers.clear() # to remove all items
print(numbers)
numbers = [5, 2, 1, 7, 4]
numbers.pop() # to delete last item
print(numbers)

print(numbers.count(5)) # to count the occurrence
print((numbers.sort())) # to sort in ascending
print(numbers)
print(numbers.reverse()) # to sort in descending
print(numbers)

numbers = [5, 2, 1, 7, 4]
numbers2 = numbers.copy()
print(numbers2)

# remove duplicates
num = [2, 2, 4, 6, 3, 4, 6, 1]
unique = []
for number in num:
    if number not in unique:
        unique.append(number)

print(unique)