first = 'john'
last = 'smith'
msg = first + '[' + last + '] is a coder'
print(msg)

f_msg = f'{first} [{last}] is a coder'  # {} is placeholder for variable
print(msg)

course = 'Python for beginners'
print(len(course))  # length
print(course.upper())  # it creates copy to display uppercase doesn't modify the original string
print(course.find('P'))  # find() is case-sensitive
print(course.replace('beginners', 'absolute beginners'))  # to replace words
print('Python' in course)  # to find the existence
print(course)
