from typing import ClassVar


class Student:
    def __init__(self, name, div, std):
        self.name = name
        self.div = div
        self.std = std


class Result(Student):
    def __init__(self, name, div, std, date, grade, percent):
        # super()
        # Student.__init__(self, name, div, std)
        self.date = date
        Student.__init__(self, name, div, std)
        Teacher.__init__(self, grade, percent)
        self.show()

    def show(self):
        print(f"{self.name}'s all data: ")
        print("Name = ", self.name)
        print("Division = ", self.div)
        print("Standard = ", self.std)
        print("Date = ", self.date)
        print("Grade = ", self.grade)
        print("Percentage = ", self.percent)


class Teacher:
    def __init__(self, grade, percent):
        self.grade = grade
        self.percent = percent


c = Result("sumit", "a", "x", "12/4/2019", "O", "90%")
c.show()
