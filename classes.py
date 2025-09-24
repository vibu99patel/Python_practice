# class is blueprint
class Point:
    # constructor
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print("move")

    def draw(self):
        print("draw")


# object is instance of class
point1 = Point()  # creating an object
# setting attributes (without constructor)
point1.x = 10
point1.y = 20
print(point1.x)
point1.draw()

# using constructor
point2 = Point(1, 2)
print(point2.x)


