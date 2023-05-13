
class Triangle:
    def sides(self):
        self.a = 10
        self.b = 20

    def display(self):
        # print("a = %d % b = %d", (self.a, self.b)) # it will not work
        print(f"a={self.a} and b = {self.b}")

# Object d passed as an argument to a function. This will access data of object d

# def perimeter(obj):
#     peri = obj.a + obj.b
#     print("Perimenter = ", peri)

# Another Method


def perimeter(obj):
    d1 = Triangle()
    d1.a = d.a * 2
    d1.b = d.b * 2
    peri = d1.a + d1.b
    return d1


d = Triangle()
d.sides()
d.display()
# perimeter(d)
t = perimeter(d)
t.display()  # we can display using t bcoz we have created Triangle object and returnning to t
