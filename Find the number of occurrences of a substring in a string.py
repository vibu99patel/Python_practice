str_x = "Emma is good developer. Emma is a writer"
substring = "Emma"
count = 0
words = str_x.split(" ")

for word in words:
    if word == substring:
        count += 1

print(f"Emma appeared {count} times")

