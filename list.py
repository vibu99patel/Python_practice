names = ['john', 'mosh', 'bob', 'sarah']

print(names[0])   # first item
print(names[-1])  # last item
print(names[2:])  # range of items  (makes copy of the modify list)
print(names[0:3]) # first 3 items

names[0] = 'moon'
print(names)

# find max num in list
num = [3, 6, 2, 8, 4, 10]
max_num = num[0]
for i in num:
    if i > max_num:
        max_num = i
print(max_num)