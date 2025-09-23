for x in range(4):
    for y in range(3):
        print(f'{x},{y}')

# example:
print('\n')
numbers = [2,2,2,2,5]
for i in numbers:
    print('x' * i)
print('\n')

#with nested loop
for x_count in numbers:
    output = ''
    for count in range(x_count):
        output += 'x'
    print(output)
