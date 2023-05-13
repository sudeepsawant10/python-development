
class Student:
    Name = "Abc"
    age = 23
    Rollno = 45


b = Student()
print(b.__dict__)  # empty {} we havn't assing values to object
print(b.Name)
print(b.age)

b.Name = "Xyz"
print(b.__dict__)
