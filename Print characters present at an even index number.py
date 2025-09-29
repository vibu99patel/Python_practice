input_str = input("Enter word: ")

print(f"original string is {input_str}")
print("printing only even index chars")

for index, ch in enumerate(input_str):
    if index % 2 == 0:
        print(ch)

