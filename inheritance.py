class Manmmal:
    def walk(self):
        print("walk")


class Dog(Manmmal):
    pass  # if we don't want to create new method


class Cat(Manmmal):
    def meow(self):
        print("Meow!")


dog1 = Dog()
dog1.walk()

cat1 = Cat()
cat1.walk()
cat1.meow()



