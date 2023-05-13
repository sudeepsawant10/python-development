"""
Base class => Parent class
Derived class => Child class
"""


class Parent:
    def getData(self):
        self.name = input("Name: ")
        self.surname = input("Surname:")

    def show(self):
        print("Name = ", self.name)
        print("Surname = ", self.surname)


class Child(Parent):
    def getname(self):
        self.child_name = input("Name: ")

    def show_name(self):
        print("Child = ", self.child_name)
        print("Surname = ", self.surname, self.name, self.surname)


c = Child()
c.getData()
c.show()
c.show_name()
