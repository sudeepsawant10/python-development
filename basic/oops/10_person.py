
from typing import AsyncGenerator


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Employee(Person):
    def __init__(self, name, age, salary):
        Person.__init__(self, name, age)  # call parent constructor
        # super().__init__(name, age)
        self.salary = salary

    def print_details(self):
        print("Name = ", self.name)
        print("Age = ", self.age)
        print("Salary = ", self.salary)


a = input("Enter name: ")
b = input("Enter age: ")
c = int(input("Salary: "))
s = Employee(a, b, c)
s.print_details()
