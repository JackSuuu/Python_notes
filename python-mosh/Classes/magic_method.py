class Point:
    def __init__(self, x, y):  # constructors
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point({self.x}, {self.y})")


point = Point(10, 20)
other = Point(1, 2)
print(point)
print(point == other)
print(point > other)
print(point + other)
