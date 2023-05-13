
class Student:
    def __init__(self):
        self.Name = input("Enter Name: ")
        self.roll = int(input("Enter roll no: "))
        self.std = input("Enter standard: ")
        self.showData()

    def showData(self):
        print("Your Data:")
        print("Student Name: ", self.Name)
        print("Student Roll No: ", self.roll)
        print("Standard: ", self.std)


# a = Student()

# invoking class by list of objects
# list1 = [a, b, c]

# for x in list1:
#     x = Student()
