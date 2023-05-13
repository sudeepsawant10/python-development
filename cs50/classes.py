class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def hello(self):
        print("Hello!")


p = Point(3, 5)
print(p)
print(p.x)
print(p.y)
p.hello()
