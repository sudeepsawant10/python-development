"""
1 parent - 2 parent-child
"""


class Student:
    def __init__(self, name, div, std, no_sub):
        self.name = name
        self.div = div
        self.std = std
        self.no_sub = no_sub


class Teacher(Student):
    def Total(self):
        Student.__init__(self, name, div, std)
        self.marks = []

        for x in range(1, self.no_sub + 1):
            m = int(input("Enter marks: "))
            self.marks.append(m)
        self.total = sum(self.marks)
        self.percent = (self.marks//self.no_sub)


class Result(Teacher):
    def show(self):
        print(f"{self.name}'s all data: ")
        print("Name = ", self.name)
        print("Division = ", self.div)
        print("Standard = ", self.std)
        print("Number of subjects = ", self.no_sub)
        print("Total marks = ", self.marks)
        print("Percentage = ", self.percent)

o1 = Result()
