from typing import SupportsAbs


class Student:
    pass


a = Student()

# declaring class members outside
a.Name = "Sudeep"
a.Id = 32
print(a.Name)
print(a.Id)

# magic method it displays data in dict formate
print(a.__dict__)

# another object
b = Student()
b.Name = "Akash"
b.age = 19
b.Id = 33
print(b.__dict__)
