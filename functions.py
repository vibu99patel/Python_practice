# define function first and then call
# no parameter
def greet():
    print("Hi there!")
    print("Welcome aboard")


# parameter
def greet_user(name):
    print(f"Hi {name}!")
    print("Welcome aboard")


print("Start")
greet()
greet_user("John Smith")
print("Finish")

# positional arguement comes first then keyword arguments
