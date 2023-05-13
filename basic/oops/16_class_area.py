
class Area:
    def circle(self, r):
        return 3.14*r*r


a = Area()
n = int(input("Enter Radius: "))
print(a.circle(n))
