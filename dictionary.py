# key: value pairs
# no duplicate key allowed

customer = {
    "name": "John Smith",
    "age": 30,
    "is_verify": True
}

# to access
print(customer["name"]) # if key doesn't exist, then gives error
print(customer.get("name"))  # if key doesn't exist, then it says "none"

# exercise
phone = input("Phone: ")
digit_map = {
    "1": "one",
    "2": "two",
    "3": "three",
    "4": "four"
}
output = ""
for ch in phone:
    output += digit_map.get(ch, "!") + ' '

print(output)

